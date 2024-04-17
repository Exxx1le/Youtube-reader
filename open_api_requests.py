from openai import OpenAI

from config import OPEN_AI_API_KEY, MAX_OUTPUT_TOKENS

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
                "content": "Create summary in russian of the text from video. Summary must be at least 2000 but no more than 2500 characters. If the content of the submitted text is less than 2000 characters, then make the character count in the response less.",
            },
            {
                "role": "user",
                "content": f"{video_text}",
            },
        ],
        temperature=0.5,
        max_tokens=MAX_OUTPUT_TOKENS,
        top_p=1,
    )

    return response.choices[0].message.content
