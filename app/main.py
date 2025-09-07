from langchain_openai import OpenAI
import json
import os

with open('app/secrets/secrets.json', 'r') as file:
    secrets = json.load(file)

os.environ["OPENAI_API_KEY"] = secrets["open_ai_key"]

class LlmClient:
    def __init__(self, modelo: str, criatividade: float):
        self.client = OpenAI(model = modelo, temperature=criatividade)

    def get_answer(self, prompt):
        
        for chunk in self.client.stream(prompt):
            print(chunk, end='', flush=True)


if __name__ == "__main__":
    user_input = input("Enter your prompt: ")

    client = LlmClient("gpt-4o-mini", 0.3)
    client.get_answer(user_input)