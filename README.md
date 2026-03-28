# ai-chatbot

a chatbot i made that connects to groq and gemini. keeps the full conversation history so it actually remembers what you said earlier. theres a reset button if you want to start over.

built this as my first project using an AI api, wanted to see how the conversation memory worked.

## stack
```
- python + flask
- groq (llama 3.3) or gemini as the model
- plain html css js for the frontend
```
## setup

you need a groq api key, get one free from https://console.groq.com
or a gemini key from https://aistudio.google.com
git clone https://github.com/X-4bys5/ai-chatbot.git
cd ai-chatbot
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

create a .env file and add your key:
GROQ_API_KEY=your_key_here

then run:
python app.py

open http://localhost:5000

## how it works

frontend sends the message to flask, flask adds it to the conversation history and sends the whole thing to groq so the model has context. reply comes back and shows up in the chat. sessions are stored in memory so they reset when the server restarts, which is fine for now.

## stuff i want to add later
```
- save chat history to a file so it doesnt reset
- let the user pick which model they want to use
- maybe add a character limit on messages
```
