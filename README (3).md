# AI_CHATBOT_USING_NLP

COMPANY : CODTECH IT SOLUTIONS

NAME : KHUSHBU KUMARI

INTERN ID : CT04DF2535

DOMAIN : PYTHON PROGRAMMING

DURATION : FOUR WEEKS

MENTOR : NEELA SANTHOSH KUMAR

---



# Simple Python Chatbot using NLTK

This is a basic chatbot project implemented in Python using the Natural Language Toolkit (NLTK). The bot can respond to greetings, farewells, gratitude, and simple identity questions based on predefined intents.

## Features

- Recognizes greetings, goodbyes, thanks, and questions like "what is your name"
- Uses basic natural language preprocessing with tokenization and lemmatization
- Random responses for more natural interaction
- Runs in the command line

## Requirements

- Python 3.x
- NLTK
- NumPy

## Setup

1. **Clone the repository** or copy the script.
2. **Install dependencies** if not already installed:

```bash
pip install nltk numpy
```

3. **Download NLTK resources** (only required once):

```python
import nltk
nltk.download('punkt')
nltk.download('wordnet')
```

4. **Run the chatbot script**:

```bash
python chatbot.py
```

## How It Works

- The bot uses a dictionary of intents and predefined responses.
- User input is tokenized and lemmatized using NLTK.
- The bot checks if any keywords from predefined patterns match the user's input.
- If a match is found, the bot responds with a related message.
- If no match is found, a default response is returned.

## Example

```text
Bot: Hello! Ask me something. Type 'exit' to quit.
You: hi
Bot: Hello!
You: what is your name
Bot: I'm a chatbot built using Python and NLTK!
You: thanks
Bot: You're welcome!
```

## License

This project is open source and free to use.