# AI Chatbot

A chatbot I built using Python and Flask that connects to Googles Gemini API. You can have a full conversation with it and it remembers what you said earlier in the chat. There's also a reset button to start fresh.

## Stack

- Python + Flask for the backend
- Gemini 2.5 Flash as the AI model
- GROQ as the AI model
- Plain HTML CSS and JS for the frontend

## Setup

You'll need a Gemini API key, get one free from https://aistudio.google.com
Or else you can use GROQ API key as well from https://console.groq.com/home

```bash
git clone https://github.com/yourusername/ai-chatbot.git
python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
```

Get API KEY FROM :
- Gemini: https://aistudio.google.com
- Groq: https://console.groq.com

Create `.env` & paste your API key.

Then just run it:

```bash
python app.py
```

Open `http://localhost:5000` in your browser and it should work.

## How it works

The frontend sends the users message to Flask via a POST request. Flask passes it to Gemini along with the conversation history so the model has context. The response comes back and gets displayed in the chat.
