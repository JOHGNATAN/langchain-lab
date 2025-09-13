from utils import LlmCompletionClient, LlmChatClient, load_secrets


if __name__ == "__main__":
    load_secrets()
    user_input = input("Enter your prompt: ")

    while True:
        model_type = input("Enter model type (completion/chat): ").strip().lower()
        if model_type == "completion":
            client = LlmCompletionClient("gpt-4o-mini", 0.3)
            client.get_completion_answer(user_input)
            break

        elif model_type == "chat":
            client = LlmChatClient("gpt-4o-mini", 0.3)
            client.get_chat_answer(user_input)
            break
        else:
            print("Invalid input. Please enter 'completion' or 'chat'.")