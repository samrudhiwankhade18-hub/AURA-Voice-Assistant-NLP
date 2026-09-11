from nlp_processor import process_text

print("🤖 AURA NLP TEST")
print("------------------")

while True:
    text = input("👤 You: ")

    if text.lower() == "exit":
        print("🤖 AURA: Goodbye!")
        break

    intent, response = process_text(text)

    print(f"🧠 Intent: {intent}")
    print(f"🤖 AURA: {response}")