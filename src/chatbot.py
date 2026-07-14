import os

from openai import OpenAI
from dotenv import load_dotenv

from src.chat_prompt import SYSTEM_PROMPT
from src.chat_memory import (
    add_message,
    get_history
)

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


def ask_bot(question):

    messages = [
        {
            "role":"system",
            "content":SYSTEM_PROMPT
        }
    ]

    messages.extend(
        get_history()
    )

    messages.append(
        {
            "role":"user",
            "content":question
        }
    )

    response = client.chat.completions.create(

        model="openrouter/free",

        messages=messages

    )

    answer = response.choices[0].message.content

    add_message("user", question)
    add_message("assistant", answer)

    return answer