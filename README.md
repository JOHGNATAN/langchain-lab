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
- [LangChain OpenAI](https://python.langchain.com/en/latest/modules/llms/integrations/openai.html)
- OpenAI GPT-4o-mini (via API)

---

## Como usar

### Pré-requisitos

- Ter uma chave de API da OpenAI.
- Python 3.13.5 instalado.
- Requirements.txt

### Instalação

1. Clone este repositório:  
git clone https://github.com/seu-usuario/seu-repositorio.git  
cd seu-repositorio  

2. Crie e ative um ambiente virtual:  
python -m venv venv  
No macOS/Linux: source venv/bin/activate  
No Windows: venv\Scripts\activate  

3. Instale as dependências:  
pip install -r requirements.txt  

4. Configure sua chave API da OpenAI:  
Crie o arquivo `app/secrets/secrets.json` com o conteúdo:  
```json
{
  "open_ai_key": "sua-chave-aqui"
}