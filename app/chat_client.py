from langchain_groq import ChatGroq
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from datetime import datetime
import json


class LlmChatClient:
    def __init__(self, modelo: str, criatividade: float):
        self.client = ChatGroq(model = modelo, temperature=criatividade)
    
    def content_guardrail(self, guardrail_prompt_template, input_text: str):
    
        system = SystemMessage(content = guardrail_prompt_template)
        
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


    def get_chat_answer(self, guardrail_prompt_template, llm_prompt_template: str):
        
        self.history_chat = []

        while True:
            user_prompt = input("\nPrompt: ")

            if user_prompt.lower() == "exit":
                break

            validator = self.content_guardrail(guardrail_prompt_template, user_prompt)
            if not validator:
                user_input = HumanMessage(content=user_prompt)

                message = [SystemMessage(content = llm_prompt_template),
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
            pergunta = chat_list[i]
            resposta = chat_list[i + 1]

            self.history.append({
                                'User': pergunta,
                                'IA': resposta
                            })
        
        self.destino = f"history_chats/chat_history_{datetime.now().strftime('%Y_%m_%d')}.json"

        with open(f"{self.destino}", "w", encoding='utf-8') as file:
            self.export_file = json.dump(self.history, file, ensure_ascii=False, indent=4)