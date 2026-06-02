import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pyttsx3
import pygame
import tempfile
import os

pygame.mixer.init()

engine = pyttsx3.init()

current_audio = None


def set_male_voice():
    voices = engine.getProperty("voices")

    for voice in voices:
        name = voice.name.lower()

        if "male" in name or "david" in name or "mark" in name:
            engine.setProperty("voice", voice.id)
            return

    # Fallback
    if voices:
        engine.setProperty("voice", voices[0].id)


def text_to_speech():
    global current_audio

    text = text_box.get("1.0", tk.END).strip()

    if not text:
        messagebox.showwarning(
            "Warning",
            "Please enter some text."
        )
        return

    try:
        temp_file = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".wav"
        )

        current_audio = temp_file.name
        temp_file.close()

        set_male_voice()

        engine.setProperty(
            "rate",
            speed_scale.get()
        )

        engine.save_to_file(
            text,
            current_audio
        )

        engine.runAndWait()

        pygame.mixer.music.load(
            current_audio
        )

        pygame.mixer.music.play()

        status_label.config(
            text="Playing..."
        )

    except Exception as e:
        messagebox.showerror(
            "Error",
            str(e)
        )


def download_audio():
    text = text_box.get("1.0", tk.END).strip()

    if not text:
        messagebox.showwarning(
            "Warning",
            "Please enter text first."
        )
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".wav",
        filetypes=[
            ("WAV Audio", "*.wav")
        ]
    )

    if not file_path:
        return

    try:
        set_male_voice()

        engine.setProperty(
            "rate",
            speed_scale.get()
        )

        engine.save_to_file(
            text,
            file_path
        )

        engine.runAndWait()

        messagebox.showinfo(
            "Success",
            "Audio saved successfully."
        )

    except Exception as e:
        messagebox.showerror(
            "Error",
            str(e)
        )


def stop_speech():
    pygame.mixer.music.stop()

    status_label.config(
        text="Stopped"
    )


root = tk.Tk()
root.title("Male Voice Text To Speech")
root.geometry("650x500")

title = tk.Label(
    root,
    text="Male Voice Text To Speech",
    font=("Arial", 18, "bold")
)

title.pack(pady=10)

text_box = tk.Text(
    root,
    height=10,
    width=65,
    font=("Arial", 12)
)

text_box.pack(pady=10)

speed_frame = tk.Frame(root)
speed_frame.pack()

tk.Label(
    speed_frame,
    text="Speed:"
).pack(side=tk.LEFT)

speed_scale = tk.Scale(
    speed_frame,
    from_=100,
    to=250,
    orient="horizontal",
    length=250
)

speed_scale.set(180)
speed_scale.pack(side=tk.LEFT)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

tk.Button(
    button_frame,
    text="Speak",
    width=15,
    command=text_to_speech
).grid(row=0, column=0, padx=5)

tk.Button(
    button_frame,
    text="Stop",
    width=15,
    command=stop_speech
).grid(row=0, column=1, padx=5)

tk.Button(
    button_frame,
    text="Download WAV",
    width=15,
    command=download_audio
).grid(row=0, column=2, padx=5)

status_label = tk.Label(
    root,
    text="Ready"
)

status_label.pack()

root.mainloop()