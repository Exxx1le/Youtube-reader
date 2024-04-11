from openai import OpenAI
from keys import OPEN_AI_API_KEY

client = OpenAI(api_key=OPEN_AI_API_KEY)

print(client.models.list())

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "Summarize content you are provided with for a second-grade student."
    },
    {
      "role": "user",
      "content": "",
    }
  ],
  temperature=0.7,
  max_tokens=64,
  top_p=1
)