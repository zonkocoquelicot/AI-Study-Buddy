from flask import Flask, render_template, request, jsonify, session
import requests
import os
from dotenv import load_dotenv
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "studybuddysecret")  # Needed for session/progress
CORS(app)
load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# In-memory progress tracking (for demo)
user_progress = {}

@app.route("/")
def home():
    # Pass theme from session if set, else default to light
    theme = session.get("theme", "light")
    return render_template("index.html", theme=theme)

@app.route("/set-theme", methods=["POST"])
def set_theme():
    data = request.json
    theme = data.get("theme", "light")
    session["theme"] = theme
    return jsonify({"message": f"Theme set to {theme}."})

@app.route("/ask", methods=["POST"])
def ask_question():
    try:
        question = request.json.get("question", "").strip()
        if not question:
            return jsonify({"error": "Question cannot be empty"}), 400
        
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Referer": "http://localhost:5000",
            "X-Title": "AI Study Buddy",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "deepseek/deepseek-r1-0528-qwen3-8b:free",
            "messages": [{"role": "user", "content": question}],
            "temperature": 0.7
        }
        
        print("Sending payload:", payload)  # Debug log
        
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=15
        )
        
        if not response.ok:
            print(f"API Error: {response.text}")
            return jsonify({"error": response.text}), response.status_code
        
        result = response.json()
        answer = result["choices"][0]["message"]["content"]

        # Progress Tracking: count questions asked
        user_id = session.get("user_id", "default")
        user_progress[user_id] = user_progress.get(user_id, 0) + 1

        return jsonify({"answer": answer})
        
    except requests.exceptions.RequestException as e:
        print(f"API Error: {e.response.text if e.response else str(e)}")
        return jsonify({"error": "API request failed"}), 500
    except Exception as e:
        print(f"Unexpected Error: {str(e)}")
        return jsonify({"error": "Server error"}), 500

# --- New Feature: Quiz Generator ---
@app.route("/quiz", methods=["POST"])
def generate_quiz():
    try:
        data = request.json
        topic = data.get("topic", "").strip()
        difficulty = data.get("difficulty", "easy").strip().lower()
        if not topic:
            return jsonify({"error": "Topic is required"}), 400

        prompt = (
            f"Generate a {difficulty} quiz on the topic '{topic}'. "
            "Provide 3 multiple-choice questions with 4 options each and indicate the correct answer."
        )
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Referer": "http://localhost:5000",
            "X-Title": "AI Study Buddy",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "deepseek/deepseek-r1-0528-qwen3-8b:free",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7
        }
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=15
        )
        if not response.ok:
            print(f"API Error: {response.text}")
            return jsonify({"error": response.text}), response.status_code
        result = response.json()
        quiz = result["choices"][0]["message"]["content"]
        return jsonify({"quiz": quiz})
    except Exception as e:
        print(f"Quiz Error: {str(e)}")
        return jsonify({"error": "Quiz generation failed"}), 500

# --- New Feature: Progress Tracking ---
@app.route("/progress", methods=["GET"])
def get_progress():
    user_id = session.get("user_id", "default")
    questions_asked = user_progress.get(user_id, 0)
    return jsonify({"questions_asked": questions_asked})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)