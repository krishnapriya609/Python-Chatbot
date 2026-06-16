import json
import re


def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9 ]", "", text)
    return text.strip()


def load_data():
    with open("intents.json", "r", encoding="utf-8") as file:
        return json.load(file)


def get_response(message):
    data = load_data()

    message = preprocess_text(message)

    personal_keywords = [
        "your age",
        "your phone",
        "your password",
        "your family",
        "where do you live",
        "personal details"
    ]

    for keyword in personal_keywords:
        if keyword in message:
            return (
                "I am PyTutor Assistant. "
                "I cannot share personal details, "
                "but I can help you learn Python programming."
            )

    # First: Exact match
    for intent in data["intents"]:
        patterns = intent.get("patterns", [])
        response = intent.get("response", "")

        for pattern in patterns:
            pattern = preprocess_text(pattern)

            if pattern == message:
                return response

    # Second: Partial match only for multi-word patterns
    for intent in data["intents"]:
        patterns = intent.get("patterns", [])
        response = intent.get("response", "")

        for pattern in patterns:
            pattern = preprocess_text(pattern)

            if len(pattern.split()) > 1 and pattern in message:
                return response

    return (
        "Sorry, I don't understand that topic yet.\n\n"
        "Try asking about:\n"
        "- What is Python\n"
        "- Variables\n"
        "- Data Types\n"
        "- Loops\n"
        "- Functions\n"
        "- Lists\n"
        "- Tuples\n"
        "- Sets\n"
        "- Dictionaries\n"
        "- Modules\n"
        "- Packages"
    )