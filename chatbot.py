import nltk
from nltk.stem import WordNetLemmatizer
import numpy as np
import random

# Sample intents
intents = {
    "greetings": ["hello", "hi", "hey", "good morning", "good evening"],
    "goodbye": ["bye", "see you", "take care"],
    "thanks": ["thank you", "thanks", "thx"],
    "name": ["what is your name", "who are you"],
    "default": ["I'm not sure I understand. Can you rephrase that?"]
}

# Preprocessing
lemmatizer = WordNetLemmatizer()

def preprocess(sentence):
    tokens = nltk.word_tokenize(sentence.lower())
    return [lemmatizer.lemmatize(word) for word in tokens]

# Match intent
def get_response(user_input):
    user_tokens = preprocess(user_input)
    for intent, patterns in intents.items():
        if intent == "default":
            continue
        for pattern in patterns:
            pattern_tokens = preprocess(pattern)
            if set(pattern_tokens).intersection(set(user_tokens)):
                return random.choice(["Hello!", "Hi there!", "Greetings!"]) if intent == "greetings" else \
                       "Goodbye!" if intent == "goodbye" else \
                       "You're welcome!" if intent == "thanks" else \
                       "I'm a chatbot built using Python and NLTK!" if intent == "name" else \
                       "Hmm, okay."
    return intents["default"][0]

# Main loop
print("Bot: Hello! Ask me something. Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break
    response = get_response(user_input)
    print("Bot:", response)
