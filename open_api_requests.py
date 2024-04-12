from openai import OpenAI

from keys import OPEN_AI_API_KEY

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
        max_tokens=100,
        top_p=1,
    )

    return response
