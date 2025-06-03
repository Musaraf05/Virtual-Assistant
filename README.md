# Virtual-Assistant
# 🧠 ROSTA - Multilingual Virtual Assistant with GUI

**ROSTA (Response Optimist Smart Technological Adaptive System)** is a powerful desktop-based virtual voice assistant application that supports multilingual voice commands (English and Tamil), gesture recognition, and a fully functional GUI. It helps users with daily tasks such as news reading, PDF reading, email sending, weather checking, launching applications, and more.

---

## 📋 Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [Folder Structure](#folder-structure)
- [Tech Stack](#tech-stack)
- [Credits](#credits)

---

## ✨ Features

- Multilingual voice assistant (supports **English** and **Tamil**).
- GUI with animated GIFs using PyQt5.
- Text-to-speech using `pyttsx3` and `gTTS`.
- Speech recognition with `SpeechRecognition`.
- YouTube, Google, Wikipedia search.
- Email and WhatsApp automation.
- Read PDF aloud from user-specified page.
- Online compiler launching by programming language.
- Dictionary & translation (Tamil ↔ English).
- Real-time news, weather, and IP location.
- Open camera and take screenshots.
- Virtual painter and mouse utilities.

---

## ✅ Prerequisites

Ensure the following software and tools are installed:

- Python 3.7 or higher
- pip (Python package installer)
- Virtual environment support (recommended)

---

## ⚙️ Installation

1. **Clone the repository**

```bash
git clone https://github.com/MUSARAF05/rosta-voice-assistant.git
cd rosta-voice-assistant
```

2. **Create a virtual environment** (optional but recommended)

- **Windows:**
```bash
python -m venv env
.\env\Scripts\activate
```

- **macOS/Linux:**
```bash
python3 -m venv env
source env/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not present, install manually:

```bash
pip install opencv-python numpy pyautogui mediapipe pyttsx3 smtplib SpeechRecognition wikipedia webbrowser pywhatkit pyjokes speedtest-cli requests PyQt5 PyDictionary PyPDF2 gTTS playsound googletrans==4.0.0-rc1
```

---

## ▶️ Running the Project

1. Make sure the `ASTORGUI.ui` and its converted Python file (`ASTORGUI.py`) are present.
2. Ensure the necessary GIFs (like `RECO.gif`, `initalising.gif`, `FACE ID.gif`) exist in the correct path.
3. Run the project:

```bash
python MULTI_ROSTA.py
```

> On first launch, the assistant will ask you to choose a language (English or Tamil) and greet you accordingly.

---

## 📂 Folder Structure

```
rosta-voice-assistant/
│
├── MULTI_ROSTA.py                   # Main file (contains GUI + assistant logic)
├── ASTORGUI.ui               # PyQt5 UI file
├── ASTORGUI.py               # Converted Python UI class
├── GUI gif/                  # Folder for animated GIFs
│   ├── RECO.gif
│   ├── initalising.gif
│   └── FACE ID.gif
├── AiVirtualMouse.py         # Virtual mouse module
├── AiVirtualPainter.py       # Virtual painter module
├── requirements.txt          # List of dependencies
└── README.md
```

---

## 🛠️ Tech Stack

- **Python** – Core programming language
- **PyQt5** – GUI development
- **Google Text-to-Speech (gTTS)** – Tamil voice synthesis
- **pyttsx3** – Offline voice synthesis (English)
- **SpeechRecognition** – Voice command input
- **OpenCV** – Camera handling
- **pywhatkit** – YouTube search, WhatsApp automation
- **PyPDF2** – PDF reading
- **PyDictionary** – English dictionary meanings
- **Googletrans** – Language translation
- **requests** – IP address and location handling

---

## 🙏 Credits

- Developed by: **Mohamed Musaraf** 
- Tamil jokes courtesy of various Tamil creators (for educational/demo purposes)
- Voice recognition and synthesis tools powered by Google APIs
