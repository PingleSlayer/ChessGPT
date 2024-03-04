import os
from openai import OpenAI
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)


def ask_gpt(prompt, model="gpt-3.5-turbo"):
    chat_completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )
    return chat_completion.choices[0].message.content
