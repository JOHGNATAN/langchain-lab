from langchain_groq import ChatGroq
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from datetime import datetime
import json
import os

def load_secrets():
    with open('secrets/secrets.json', 'r') as file:
        secrets = json.load(file)

    os.environ["GROQ_API_KEY"] = secrets["GROQ_API_KEY"]


class LlmChatClient:
    def __init__(self, modelo: str, criatividade: float, reasoning_effort: str):
        self.client = ChatGroq(model = modelo, temperature=criatividade)
    
    def content_guardrail(self, input_text: str):
    
        system = SystemMessage(content="""Analise e determine se ele envolve, mesmo de forma implícita, alguma das categorias de conteúdo sensível listadas abaixo.

                                            Importante:
                                            - O conteúdo pode ser hipotético, conceitual, especulativo, criativo ou apresentado em perguntas, diálogos, narrativas ou contextos ficcionais.
                                            - A simples menção, intenção de discutir, explorar ou referenciar o tema já é suficiente para considerar a categoria como "presente".
                                            - O texto **não precisa** descrever os atos de forma gráfica ou explícita para ser considerado sensível.
        
                                            Categorias:
                                            1. Violência
                                            2. Conteúdo sexual
                                            3. Discurso de ódio
                                            4. Automutilação ou suicídio
                                            5. Abuso ou exploração infantil
                                            6. Drogas ou substâncias ilícitas
                                            7. Atividades ilegais ou criminosas
                                            8. Terrorismo ou extremismo violento
                                            9. Informações pessoais sensíveis
        
                                            
                                            Instruções de Resposta:
                                            Retorne:
                                            - True → Se qualquer uma das categorias estiver presente ou for discutida, mesmo indiretamente.
                                            - False → Se nenhuma categoria estiver presente ou referida de forma alguma.
                                    """)
        
        few_shot_examples = [
                                HumanMessage(content="Era uma vez um garoto que pensava em tirar a própria vida."),
                                AIMessage(content="True"),

                                HumanMessage(content="Como posso melhorar minha produtividade no trabalho?"),
                                AIMessage(content="False"),

                                HumanMessage(content="Quais são os efeitos de se cortar para aliviar a dor emocional?"),
                                AIMessage(content="True"),
                            ]

        human = HumanMessage(content=input_text)

        message = [system] + few_shot_examples + [human]

        guardrail_response = self.client.invoke(message)
        
        return guardrail_response.content.strip().lower() == "true"


    def get_chat_answer(self):
        
        self.history_chat = []

        while True:
            user_prompt = input("\nPrompt: ")

            if user_prompt.lower() == "exit":
                break

            validator = self.content_guardrail(user_prompt)
            if not validator:
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
            else:
                print("Conteúdo não permitido. Tente novamente.")
                continue

        return self.history_chat
    

    def export_chat_history(self, chat_list: list):
        
        self.history = []

        for i in range(0, len(chat_list), 2):
            self.pergunta = chat_list[i]
            self.resposta = chat_list[i + 1]

            self.history.append({
                                'User': self.pergunta,
                                'IA': self.resposta
                            })
        
        self.destino = f"history_chats/chat_history_{datetime.now().strftime('%Y_%m_%d')}.json"

        with open(f"{self.destino}", "w", encoding='utf-8') as file:
            self.export_file = json.dump(self.history, file, ensure_ascii=False, indent=4)

<<<<<<< HEAD
=======
    
>>>>>>> langchain_feature
            
        
