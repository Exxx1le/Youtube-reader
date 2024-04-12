from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from keys import TELEGRAM_BOT_KEY
from open_api_requests import chat_gpt_response
from youtube_transcripter import *

# Создаем объекты бота и диспетчера
bot = Bot(token=TELEGRAM_BOT_KEY)
dp = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer(
        "Привет!\nЯ бот, который поможет сократить для тебя время просмотра видео с YouTube\nЯ умею делать краткую выжимку из содержания видео."
    )


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=["help"]))
async def process_help_command(message: Message):
    await message.answer("Пришли мне ссылку на видео в YouTube, а в ответ я пришлю тебе краткое содержание видео")


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
@dp.message()
async def send_echo(message: Message):
    video_id = extract_video_id(message.text)
    if video_id != None:
        transcription = transcript_video(video_id)
        if transcription != None:
            responce = chat_gpt_response(transcript_video)
            if responce:
                await message.reply(text=responce)
        else:
            await message.answer("Не удалось найти субтитры к видео")
    else:
        await message.answer("Это не ссылка на YouTube или вообще не ссылка")


if __name__ == "__main__":
    dp.run_polling(bot)
