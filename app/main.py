from utils import LlmChatClient, load_secrets


if __name__ == "__main__":
    load_secrets()

    client = LlmChatClient("gpt-4o-mini", 0.3)

    chat_history = client.get_chat_answer()

    client.export_chat_history(chat_history)
