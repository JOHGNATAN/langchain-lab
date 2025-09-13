from utils import LlmChatClient, load_secrets


if __name__ == "__main__":
    load_secrets()
    user_input = input("Enter your prompt: ")

    client = LlmChatClient("gpt-4o-mini", 0.3)
    client.get_chat_answer(user_input)
