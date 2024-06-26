import youtube_transcript_api
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

from config import MAX_INPUT_TOKENS, MIN_WORDS, TELEGRAM_BOT_KEY
from open_api_requests import chat_gpt_response
from youtube_transcripter import *

bot = Bot(token=TELEGRAM_BOT_KEY)
dp = Dispatcher()


@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer(
        "Привет!\nЯ бот, который поможет сократить для тебя время просмотра видео с YouTube\nЯ умею делать краткую выжимку из содержания видео."
    )


@dp.message(Command(commands=["help"]))
async def process_help_command(message: Message):
    await message.answer("Пришли мне ссылку на видео в YouTube,\nа в ответ я пришлю тебе краткое содержание видео 🤓")


@dp.message(F.text.startswith("http") | F.text.startswith("yout"))
async def send_transctipt(message: Message):
    video_id = extract_video_id(message.text)
    if video_id is None:
        await message.answer("По-моему, это не ссылка на YouTube или вообще не ссылка 🤨")
    else:
        try:
            transcription = transcript_video(video_id, MIN_WORDS)
            if transcription:
                short_transcription = reduce_transcript_to_max_tokens(transcription, MAX_INPUT_TOKENS)
                await message.answer("⏳Подождите немного.\nГенерируется короткое содержание видео. ")
                response = chat_gpt_response(short_transcription)
                if response:
                    await message.reply(text=response)
                else:
                    await message.answer("Не удалось получить ответ от Chat GPT 😞")
            else:
                await message.answer("Не удалось найти субтитры к видео, либо видео слишком короткое 🤖")
        except youtube_transcript_api._errors.TranscriptsDisabled:
            await message.answer("Субтитры для этого видео отключены или недоступны.🤖")
        except Exception as e:
            print(e)


@dp.message(F.content_type != "text")
async def send_other(message: Message):
    await message.answer("К сожалению, я могу распознавать только ссылки с YouTube 😢")


if __name__ == "__main__":
    dp.run_polling(bot)
