from nlp_processor import process_text
from voice_input import listen
from voice_output import speak
from actions import get_time, get_date, open_website


def main():
    speak("Hello! I am AURA, your intelligent voice assistant. How can I help you?")

    while True:
        text = listen()

        if not text:
            continue

        intent, response = process_text(text)

        print(f"🧠 Detected Intent: {intent}")

        if intent == "time":
            response = f"The current time is {get_time()}"

        elif intent == "date":
            response = f"Today's date is {get_date()}"

        elif intent == "open_website":
            if "youtube" in text.lower():
                open_website("https://www.youtube.com")
                response = "Opening YouTube."

            elif "google" in text.lower():
                open_website("https://www.google.com")
                response = "Opening Google."

            elif "github" in text.lower():
                open_website("https://github.com")
                response = "Opening GitHub."

        speak(response)

        if intent == "goodbye":
            break


if __name__ == "__main__":
    main()