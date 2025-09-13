from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
import json
import os


def load_secrets():
    with open('secrets/secrets.json', 'r') as file:
        secrets = json.load(file)

    os.environ["OPENAI_API_KEY"] = secrets["open_ai_key"]


class LlmCompletionClient:
    def __init__(self, modelo: str, criatividade: float):
        self.client = OpenAI(model = modelo, temperature=criatividade)

    def get_completion_answer(self, prompt):
        
        for chunk in self.client.stream(prompt):
            print(chunk, end='', flush=True)



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
        