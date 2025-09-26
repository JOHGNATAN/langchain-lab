from langchain_groq import ChatGroq
from langchain.schema import HumanMessage, SystemMessage
from datetime import datetime
import json
import os

def load_secrets():
    with open('secrets/secrets.json', 'r') as file:
        secrets = json.load(file)

    os.environ["GROQ_API_KEY"] = secrets["GROQ_API_KEY"]


class LlmChatClient:
    def __init__(self, modelo: str, criatividade: float):
        self.client = ChatGroq(model = modelo, temperature=criatividade)
    
    def content_guardrail(self, input_text: str):
    
        message = [
            SystemMessage(content="""Analise o seguinte texto e indique se ele contém algum dos seguintes tipos de conteúdo sensível.

                                      Categorias:
                                      1. Violência
                                      2. Conteúdo sexual
                                      3. Discurso de ódio
                                      4. Automutilação ou suicídio
                                      5. Abuso infantil ou exploração
                                      6. Drogas ou substâncias ilícitas

                                      Retorne True caso qualquer uma das categorias esteja presente no texto, caso contrário retorne False.
                                    """),

            HumanMessage(content=input_text)
        ]

        guardrail_response = self.client.invoke(message)
        print(guardrail_response.content)

        return guardrail_response.content

    def get_chat_answer(self):
        
        self.history_chat = []

        while True:
            user_prompt = input("\nPrompt: ")

            if user_prompt.lower() == "exit":
                break

            user_input = HumanMessage(content=user_prompt)

            message = [SystemMessage(content="You are a helpful AI assistant"),
                       user_input
                       ]

            self.history_chat.append(user_input.content)

            resposta = ""

            for chunk in self.client.stream(message):
                print(chunk.content, end='', flush=True)
                resposta  += chunk.content 
            
            self.history_chat.append(resposta)

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
            

    
            
        
