from nlp_processor import process_text
from voice_output import speak
from actions import get_time, get_date

print("🤖 AURA Voice Test")
print("------------------")

while True:
    text = input("👤 You: ")

    if text.lower() == "exit":
        speak("Goodbye! Have a nice day.")
        break

    intent, response = process_text(text)

    print(f"🧠 Intent: {intent}")

    if intent == "time":
        response = f"The current time is {get_time()}"

    elif intent == "date":
        response = f"Today's date is {get_date()}"

    speak(response)
