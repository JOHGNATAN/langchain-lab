from app.utils import LlmClient


if __name__ == "__main__":
    user_input = input("Enter your prompt: ")

    client = LlmClient("gpt-4o-mini", 0.3)
    client.get_answer(user_input)