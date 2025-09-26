# Chatbot com LangChain e GPT-4o-mini

Este projeto é um chatbot simples construído em Python utilizando a biblioteca LangChain e o modelo GPT-4o-mini da OpenAI. O chatbot permite conversas via terminal e exporta o histórico de perguntas e respostas em arquivos JSON organizados por data.

---

## Estrutura do Projeto

LANGCHAIN/  
│  
├── app/  
│   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── history_chats/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Histórico das conversas exportadas  
│   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── secrets/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Arquivos com chaves secretas  
│   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── main.py &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Script principal para rodar o chatbot  
│   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── utils.py &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Funções auxiliares e classe do chatbot  
├── venv/ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Ambiente virtual (não incluído no Git)  
├── .gitignore  
└── requirements.txt  


---

## Funcionalidades

- Interação em tempo real com um modelo de linguagem GPT-4o-mini.
- Histórico da conversa armazenado em formato JSON.
- Configuração do modelo e temperatura (criatividade) personalizáveis.
- Facilidade para extensão e integração com outras interfaces.

---

## Tecnologias Utilizadas

- Python 3.13.5
- [LangChain](https://python.langchain.com/)
- [LangChain Groq](https://console.groq.com/docs/model/openai/gpt-oss-120b)
- openai/gpt-oss-120b (via API)

---

## Como usar

### Pré-requisitos

- Ter uma chave de API da OpenAI.
- Python 3.13.5 instalado.
- Requirements.txt

### Instalação

1. Clone este repositório:  
git clone https://github.com/JOHGNATAN/langchain-lab  
cd seu-repositorio  

2. Crie e ative um ambiente virtual:  
  
```cmd 
python -m venv venv  
```
3. Ativação:
 
### No macOS/Linux:
```bash
source venv/bin/activate 
```


### No Windows: 
```bash
venv\Scripts\activate  
```
4. Instale as dependências:  
```bash
pip install -r requirements.txt  
```

5. Configure sua chave API da OpenAI:  
Crie o arquivo `app/secrets/secrets.json` com o conteúdo:  
```json
{
  "open_ai_key": "sua-chave-aqui"
}