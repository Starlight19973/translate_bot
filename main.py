from aiogram import Bot, Dispatcher, types, executor
from googletrans import Translator, LANGUAGES
from dotenv import load_dotenv
import os

load_dotenv()


TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

translator = Translator()


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я бот-переводчик. Отправь мне текст, и я переведу его на английский.")


@dp.message_handler()
async def translate_text(message: types.Message):
    translated = translator.translate(message.text, dest='en')
    await message.reply(translated.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
