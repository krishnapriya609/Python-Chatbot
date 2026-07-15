import json
import re
import difflib


def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9 ]", "", text)
    text = text.strip()
    return text


def load_data():
    with open("intents.json", "r") as file:
        return json.load(file)


def get_response(message):

    data = load_data()

    message = preprocess_text(message)

    # ==========================
    # PERSONAL QUESTION DETECTION
    # ==========================

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
                "I cannot share personal details,\n"
                "but I can help you learn Python."
            )

    # ==========================
    # STORE ALL PATTERNS
    # ==========================

    pattern_response = {}

    for intent in data["intents"]:

        response = intent["response"]

        for pattern in intent["patterns"]:
            pattern = preprocess_text(pattern)
            pattern_response[pattern] = response

    # ==========================
    # EXACT MATCH
    # ==========================

    if message in pattern_response:
        return pattern_response[message]

    # ==========================
    # SPELLING CORRECTION
    # ==========================

    closest_match = difflib.get_close_matches(
        message,
        pattern_response.keys(),
        n=1,
        cutoff=0.6
    )

    if closest_match:
        return pattern_response[closest_match[0]]

    # ==========================
    # DEFAULT RESPONSE
    # ==========================

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