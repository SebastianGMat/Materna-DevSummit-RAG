from openai import OpenAI

ai_client = OpenAI(
    base_url="http://192.168.178.60:2500/v1", api_key="lm-studio"
)


def get_embedding(text, model="nomic-ai/nomic-embed-text-v1.5-GGUF"):
    text = text.replace("\n", " ")
    return (
        ai_client.embeddings.create(input=[text], model=model)
        .data[0]
        .embedding
    )


def create_chat_completion(
    messages, model="lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF"
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
