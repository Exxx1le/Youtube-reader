from openai import OpenAI

from config import OPEN_AI_API_KEY, MAX_TOKENS

client = OpenAI(api_key=OPEN_AI_API_KEY)


def chat_gpt_response(video_text: str) -> str:
    """
    Gets string of text and sends it to ChatGPT

    Args:
        video_text (str): Text

    Returns:
        str: Responce of ChatGPT with a short summary of the text
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {
                "role": "system",
                "content": "сделай короткую выжимку содержания текста из видео",
            },
            {
                "role": "user",
                "content": f"{video_text}",
            },
        ],
        temperature=0.5,
        max_tokens=MAX_TOKENS,
        top_p=1,
    )

    return response.choices[0].message.content
