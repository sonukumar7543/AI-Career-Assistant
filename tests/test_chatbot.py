from src.chatbot import ask_bot

while True:

    question = input("You: ")

    if question.lower() == "exit":
        break

    answer = ask_bot(question)

    print("\nCareerGPT:", answer)
    print()