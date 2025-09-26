from utils import LlmChatClient, load_secrets


if __name__ == "__main__":
    load_secrets()

    client = LlmChatClient("llama-3.3-70b-versatile", 0.3)

    chat_history = client.get_chat_answer()

    client.export_chat_history(chat_history)

