import sys
import pyaudiowpatch as pyaudio

sys.modules["pyaudio"] = pyaudio

import speech_recognition as sr


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\n🎤 Listening...")

        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

            print("🔄 Processing your voice...")

            text = recognizer.recognize_google(audio)

            print(f"👤 You: {text}")

            return text

        except sr.WaitTimeoutError:
            print("⏰ No voice detected.")
            return ""

        except sr.UnknownValueError:
            print("❌ Sorry, I could not understand.")
            return ""

        except sr.RequestError:
            print("🌐 Speech recognition service is unavailable.")
            return ""