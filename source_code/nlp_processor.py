import json
import random
import nltk

from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()


# Load dataset
with open("dataset/intents.json", "r", encoding="utf-8") as file:
    data = json.load(file)


patterns = []
tags = []


# Prepare training data
for intent in data["intents"]:
    for pattern in intent["patterns"]:
        patterns.append(pattern.lower())
        tags.append(intent["tag"])


# Convert text into numerical features
vectorizer = TfidfVectorizer(
    tokenizer=nltk.word_tokenize,
    token_pattern=None
)

X = vectorizer.fit_transform(patterns)


# Train intent classification model
model = LogisticRegression(max_iter=1000)
model.fit(X, tags)


def predict_intent(text):
    """
    Predict the user's intent from text.
    """

    text = text.lower()

    text_vector = vectorizer.transform([text])

    predicted_tag = model.predict(text_vector)[0]

    return predicted_tag


def get_response(tag):
    """
    Get a random response for the predicted intent.
    """

    for intent in data["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])

    return "Sorry, I didn't understand that."


def process_text(text):
    """
    Process user text and return intent and response.
    """

    intent = predict_intent(text)
    response = get_response(intent)

    return intent, response