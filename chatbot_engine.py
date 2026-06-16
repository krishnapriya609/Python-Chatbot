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
        "you",
        "your",
        "yourself",
        "personal",
        "age",
        "phone",
        "password",
        "family",
        "where do you live"
    ]

    for word in personal_keywords:
        if word in message:
            return (
                "I am PyTutor Assistant.\n\n"
                "I cannot share personal details, "
                "but I can help you learn Python programming."
            )

    for intent in data["intents"]:
        patterns = intent.get("patterns", [])
        response = intent.get("response", "")

        for pattern in patterns:
            pattern = preprocess_text(pattern)

            # Improved matching
            if pattern in message or message in pattern:
                return response

    return (
        "Sorry, I don't understand that topic yet.\n\n"
        "Try asking about:\n"
        "- variables\n"
        "- data types\n"
        "- loops\n"
        "- functions\n"
        "- lists\n"
        "- tuples\n"
        "- sets\n"
        "- dictionaries\n"
        "- modules\n"
        "- packages"
    )