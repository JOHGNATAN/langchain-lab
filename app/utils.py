import json
import os
import yaml

def load_secrets():
    with open('secrets/secrets.json', 'r') as file:
        secrets = json.load(file)

    os.environ["GROQ_API_KEY"] = secrets["GROQ_API_KEY"]


def load_prompt(yaml_path: str):
    yaml_path = yaml_path
    with open(yaml_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)