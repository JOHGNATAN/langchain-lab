from chat_client import LlmChatClient
from utils import load_secrets, load_prompt


if __name__ == "__main__":
    load_secrets()

    client = LlmChatClient("llama-3.3-70b-versatile", 0.3)

    chat_history = client.get_chat_answer()

    client.export_chat_history(chat_history)

