from fastapi import FastAPI
from typing import Dict
import json
import openai

with open ('/etc/python-gpt.json') as config_file:
   config = json.load(config_file)

app = FastAPI()

# Set your OpenAI API key
openai.api_key = config['OPENAI_API_KEY']

@app.post("/chat")
def chat(data: Dict[str, str]):
    message = data.get("message")
    if message:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message}
            ]
        )
        return {"message": response.choices[0].message["content"]}
    else:
        return {"message": "Invalid request"}

