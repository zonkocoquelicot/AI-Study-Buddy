# 🎓 AI Study Buddy — Intelligent Learning Assistant

An AI-powered study companion that answers academic questions, clarifies concepts, and generates quizzes using LLM (DeepSeek via OpenRouter API). 

---

### 🚀 Features

| Feature        |                    Description                             |
|----------------|------------------------------------------------------------|
| Q&A Chat       | Asks academic questions and gets instant explanations      |
| Quiz Generator | Generates quizzes dynamically (topic + difficulty)         |
| Dark/Light Mode| Choose between two UI themes                               |
| Flask Backend  | Handles API calls to OpenRouter DeepSeek models            |
| Frontend UI    | Clean minimal UI built using HTML/CSS/JS (Flask templates) |

---

### 🧠 Tech Stack

| Component | Technology Used                              |
|---------- |----------------------------------------------|
| Backend   | Python, Flask                                |
| AI Model  | DeepSeek + OpenRouter API                    |
| Frontend  | HTML, CSS, JavaScript                        |
| Deployment| Localhost (Future: Streamlit Cloud / Render) |

---

### 🏗 Project Architecture
User → Frontend (templates) → Flask Backend (app.py) → OpenRouter API → DeepSeek LLM

---

### 📂 Folder Structure
AI-Study-Buddy/
│
├── backend/
│ ├── app.py
│ ├── requirements.txt
│ └── templates/ # Frontend HTML/CSS/JS
│
└── docs/
└── AI-Study-Buddy-Mini-Project.pdf # Full documentation report

---

### ▶️ How to Run

1. Clone the repo
   git clone https://github.com/<your-username>/AI-Study-Buddy.git
   cd AI-Study-Buddy/backend

2. Install dependencies
   pip install -r requirements.txt
   
3. Add your `.env` file
   OPENROUTER_API_KEY="your_key_here"

4. Start Flask
   python app.py
---

✅ Open browser → http://localhost:5000/

---

### 🔮 Future Improvements

- Study Plan Generator (based on exam schedule)
- Flashcard learning mode
- Voice Input (speech-to-text & text-to-speech)
- Gamification (user rewards & badges)

---

### ⭐ Author

**zonkocoquelicot**




