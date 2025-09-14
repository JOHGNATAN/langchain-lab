from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from datetime import datetime
import json
import os

def load_secrets():
    with open('secrets/secrets.json', 'r') as file:
        secrets = json.load(file)

    os.environ["OPENAI_API_KEY"] = secrets["open_ai_key"]


class LlmChatClient:
    def __init__(self, modelo: str, criatividade: float):
        self.client = ChatOpenAI(model = modelo, temperature=criatividade)

    def get_chat_answer(self):
        self.system_message = SystemMessage(content="You are a helpful AI assistant")
        
        self.history_chat = []

        while True:
            self.user_prompt = input("\nPrompt: ")
            if self.user_prompt.lower() == "exit":
                break

            user_input = HumanMessage(content=self.user_prompt)

            self.history_chat.append(user_input.content)

            self.resposta = ""

            for chunk in self.client.stream(self.user_prompt):
                print(chunk.content, end='', flush=True)
                self.resposta  += chunk.content 
            
            self.history_chat.append(self.resposta)

        return self.history_chat

    def export_chat_history(self, history_chat: list):
        self.history = []
        for i in range(0, len(history_chat), 2):
            self.pergunta = history_chat[i]
            self.resposta = history_chat[i+1]

            self.history.append({
                                'User': self.pergunta,
                                'IA': self.resposta
                            })
        
        self.destino = f"history_chats/chat_history_{datetime.now().strftime("%Y_%m_%d")}.json"

        with open(f"{self.destino}", "w", encoding='utf-8') as file:
            self.export_file = json.dump(self.history, file, ensure_ascii=False, indent=4)

        
            
        
