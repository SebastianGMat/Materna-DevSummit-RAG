import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

ai_client = OpenAI(
    base_url=os.environ["OPEN_AI_BASE_URL"],
    api_key=os.environ["OPEN_AI_API_KEY"],
)


def get_embedding(text, model=os.environ["OPEN_AI_DEFAULT_EMBED_MODEL"]):
    text = text.replace("\n", " ")
    return (
        ai_client.embeddings.create(input=[text], model=model)
        .data[0]
        .embedding
    )


def create_chat_completion(
    messages, model=os.environ["OPEN_AI_DEFAULT_CMPLT_MODEL"]
):
    return (
        ai_client.chat.completions.create(
            model=model, messages=messages, temperature=0.7
        )
        .choices[0]
        .message.content
    )


def user(content: str):
    return {
        "role": "user",
        "content": content,
    }


def system(content: str):
    return {
        "role": "system",
        "content": content,
    }
