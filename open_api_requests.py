from openai import OpenAI

from config import MAX_OUTPUT_TOKENS, MIN_WORDS, MODEL, OPEN_AI_API_KEY

client = OpenAI(api_key=OPEN_AI_API_KEY)


def chat_gpt_response(video_text: str) -> str:
    """
    Gets string of text and sends it to ChatGPT

    Args:
        video_text (str): Text

    Returns:
        str: Responce of ChatGPT in russian with a short summary of the text
    """
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": f"Create a summary in russian of the text from video. Summary should have minimum {MIN_WORDS} words.",
            },
            {
                "role": "user",
                "content": f"{video_text}",
            },
        ],
        temperature=1.0,
        max_tokens=MAX_OUTPUT_TOKENS,
    )

    return response.choices[0].message.content
