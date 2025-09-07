# %%
# from langchain_openai import openAI
import json

# %%
with open('secrets/secrets.json', 'r') as file:
    secrets = json.load(file)


# %%
llm_model = openAI(api_key = secrets['open_ai_key'])
llm_model.invoke("Olá")

