# 🎙️ Speech-to-Text Whiteboard Web App

A **real-time browser-based whiteboard** that converts spoken words into text — built for classroom teaching, remote collaboration, and live note-taking.

---

## 📌 About the Project

Typing while explaining is inefficient. This app lets teachers, presenters, and remote teams speak naturally and watch their words appear on a shared digital whiteboard instantly — no special hardware needed.

**Real-world use cases:**
- Classroom teaching and lecture capture
- Remote team collaboration
- Accessibility tools for differently-abled users
- Live meeting transcription

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| Speech Recognition | Web Speech API (browser-native) |
| Frontend | HTML5, CSS3, JavaScript |
| Routing | Flask REST endpoints |

---

## ⚙️ How It Works

```
User speaks into microphone
        ↓
Browser Web Speech API captures audio
        ↓
Speech converted to text (client-side)
        ↓
Text sent to Flask backend
        ↓
Displayed on whiteboard in real time
```

---

## 🚀 Getting Started

### Prerequisites
```bash
Python 3.8+
A modern browser (Chrome recommended for Web Speech API support)
```

### Installation
```bash
git clone https://github.com/Subhadevik/WhiteBoard_Speech_Text.git
cd WhiteBoard_Speech_Text
pip install -r requirements.txt
```

### Run the App
```bash
python app.py
```
Open `http://localhost:5000` in **Google Chrome** and allow microphone access.

---

## 📂 Project Structure

```
WhiteBoard_Speech_Text/
│
├── app.py               # Flask backend
├── requirements.txt     # Python dependencies
├── static/              # CSS, JavaScript files
│   └── style.css
└── templates/           # HTML templates
    └── index.html
```

---

## ✨ Features

- ✅ Real-time speech-to-text conversion
- ✅ Clean whiteboard UI — distraction free
- ✅ No external speech API costs (uses browser-native Web Speech API)
- ✅ Modular Flask backend — easy to extend or deploy
- ✅ Responsive design — works on desktop and tablet

---

## 🌐 Browser Compatibility

| Browser | Supported |
|---|---|
| Google Chrome | ✅ Full support |
| Microsoft Edge | ✅ Full support |
| Firefox | ⚠️ Partial |
| Safari | ⚠️ Limited |

---

## 👩‍💻 Author

**Subhadevi Krishnaraj**
- 🔗 [LinkedIn](https://www.linkedin.com/in/subhadevi-krishnaraj)
- 🐙 [GitHub](https://github.com/Subhadevik)
- 📧 subhadevi333@gmail.com
