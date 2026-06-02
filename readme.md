# 🎙️ Offline Male Voice Text-to-Speech Converter

A simple and lightweight desktop application built with Python and Tkinter that converts text into speech using offline male voices powered by pyttsx3.

The application allows users to enter text, listen to generated speech, adjust speaking speed, stop playback, and export audio files in WAV format without requiring an internet connection, APIs, subscriptions, or paid services.

---

# ✨ Features

- 🎤 Offline Text-to-Speech Conversion
- 👨 Male Voice Support
- ⚡ Adjustable Speech Speed
- ▶️ Instant Audio Playback
- ⏹️ Stop Playback Anytime
- 💾 Export Audio as WAV File
- 🖥️ Clean and User-Friendly Interface
- 🌐 No Internet Required
- 🆓 Completely Free and Open Source

---

# 📸 Screenshots

## Main Application Window

Place your screenshot in the following folder:

```text
<img width="643" height="512" alt="image" src="https://github.com/user-attachments/assets/4952534b-b6f6-4c19-a4d7-07f6a3397798" />

```

Then add your screenshot below:

![Application Screenshot](screenshots/main-window.png)

---

# 🛠️ Technologies Used

| Technology | Purpose                       |
| ---------- | ----------------------------- |
| Python     | Programming Language          |
| Tkinter    | GUI Framework                 |
| pyttsx3    | Offline Text-to-Speech Engine |
| Pygame     | Audio Playback                |
| Tempfile   | Temporary Audio Storage       |

---

# 📋 Requirements

- Python 3.8+
- Windows, Linux, or macOS

No internet connection is required.

---

# 📦 Installation

## Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/offline-male-tts.git
cd offline-male-tts
```

## Step 2: Create a Virtual Environment (Optional)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

## Step 3: Install Dependencies

```bash
pip install pyttsx3 pygame
```

Or install from requirements.txt:

```bash
pip install -r requirements.txt
```

---

# 📄 requirements.txt

Create a file named:

```text
requirements.txt
```

Add the following:

```txt
pyttsx3
pygame
```

---

# 🚀 Running the Application

Run the following command:

```bash
python main.py
```

The application window will launch automatically.

---

# 🎯 How to Use

## 1. Enter Text

Type or paste the text you want to convert into speech.

---

## 2. Adjust Speech Speed

Use the speed slider to control the speaking rate.

| Speed | Description |
| ----- | ----------- |
| 100   | Slow        |
| 180   | Normal      |
| 250   | Fast        |

---

## 3. Generate Speech

Click the **Speak** button.

The application will:

- Convert text into speech
- Generate a temporary WAV file
- Play the audio automatically

---

## 4. Stop Audio

Click the **Stop** button to stop playback immediately.

---

## 5. Save Audio

Click the **Download WAV** button.

Choose a location and save the generated audio file.

---

# 📂 Project Structure

```text
offline-male-tts/
│
├── main.py
├── README.md
├── requirements.txt
│
├── screenshots/
│   └── main-window.png
│
└── assets/
```

---

# 🎤 Voice Information

The application uses the voices available on your operating system through pyttsx3.

On Windows, it automatically attempts to select a male voice if available.

Voice quality may vary depending on the voices installed on your computer.

---

# ⚠️ Limitations

- Voice quality depends on installed system voices.
- WAV export is supported by default.
- MP3 export requires additional tools such as FFmpeg.
- Voice selection options vary across operating systems.

---

# 🐛 Common Issues

## ModuleNotFoundError

Install the required packages:

```bash
pip install pyttsx3 pygame
```

---

## No Sound

Check:

- System volume
- Speaker output device
- Pygame installation

---

## Voice Not Changing

The available voices depend on your operating system.

Some systems may only provide one voice option.

---

# 🔮 Future Improvements

- Dark Mode UI
- Female Voice Support
- Voice Selection Dropdown
- MP3 Export Support
- Multiple Language Support
- Audio History
- Modern UI Design

---

# 🤝 Contributing

Contributions, bug reports, and feature suggestions are welcome.

Feel free to fork the project and submit a pull request.

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

Rupesh Verma

Frontend Developer | Python Learner | Tech Enthusiast

GitHub:
https://github.com/yourusername

---

# ⭐ Support

If you found this project useful:

- ⭐ Star the repository
- 🍴 Fork the project
- 📢 Share it with others

Happy Coding! 🚀
