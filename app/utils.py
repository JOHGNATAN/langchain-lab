from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
import json
import os


def load_secrets():
    with open('secrets/secrets.json', 'r') as file:
        secrets = json.load(file)

    os.environ["OPENAI_API_KEY"] = secrets["open_ai_key"]


class LlmChatClient:
    def __init__(self, modelo: str, criatividade: float):
        self.client = ChatOpenAI(model = modelo, temperature=criatividade)

    def get_chat_answer(self, prompt):
        messages = [
            ("system", "You are a helpful assistant."),
            ("user", prompt)
        ]
        
        for chunk in self.client.stream(messages):
            print(chunk.content, end='', flush=True)
        