import sqlite3
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

API_TOKEN = "6608318606:AAENjISuyYo4jOn-cd7bfe4ORQbFH5O-85s"
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
storage = MemoryStorage()
dp.middleware.setup(LoggingMiddleware())

conn = sqlite3.connect('tg.db')
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS tg_user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tg_id INTEGER NOT NULL,
        username TEXT NOT NULL
    )
""")
conn.commit()

class RegistrationStates(StatesGroup):
    waiting_username = State()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Assalomu alaykum! {} Botga xush kelibsiz.\nIltimos, foydalanuvchi nomingizni kiriting.")

@dp.message_handler(state=RegistrationStates.waiting_username)
async def process_username(message: types.Message, state: FSMContext):
    username = message.text
    tg_id = message.from_user.id

    cursor.execute("INSERT INTO tg_user (tg_id, username) VALUES (?, ?)", (tg_id, username))
    conn.commit()

    await message.reply(f"Tabriklayman, {username}! Siz bazaga muvaffaqiyatli qo'shildingiz.")

    await state.finish()

@dp.message_handler(commands=['register'])
async def register(message: types.Message):
    await message.reply("Iltimos, foydalanuvchi nomingizni kiriting.")
    await RegistrationStates.waiting_username.set()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)