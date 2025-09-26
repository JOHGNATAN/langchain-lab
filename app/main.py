from chat_client import LlmChatClient
from utils import load_secrets, load_prompt


if __name__ == "__main__":
    load_secrets()

    client = LlmChatClient("llama-3.3-70b-versatile", 0.3)

    guardrail_prompt = load_prompt("prompts_template/guardrail_prompt.yaml")['guardrail_prompt_template']
    llm_prompt = load_prompt("prompts_template/llm_prompt.yaml")['llm_prompt_template']
    
    chat_history = client.get_chat_answer(guardrail_prompt, llm_prompt)

    client.export_chat_history(chat_history)

