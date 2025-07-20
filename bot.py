import os
from aiogram import Bot, Dispatcher, types, executor
from dotenv import load_dotenv

# Читаем токен из .env
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer("Обновленный бот")

if __name__ == "__main__":
    executor.start_polling(dp)