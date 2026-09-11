import sys
import pyaudiowpatch as pyaudio

sys.modules["pyaudio"] = pyaudio

import speech_recognition as sr


recognizer = sr.Recognizer()

# Voice detection ko thoda stable banane ke liye
recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = True
recognizer.pause_threshold = 0.8
recognizer.non_speaking_duration = 0.5


def listen():
    try:
        with sr.Microphone() as source:
            print("\n🎤 Listening...")

            # Sirf thoda ambient noise adjustment
            recognizer.adjust_for_ambient_noise(source, duration=0.5)

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

    except OSError as e:
        print(f"🎤 Microphone error: {e}")
        return ""