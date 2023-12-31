from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default import home

from loader import dp,db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    chatId = message.chat.id
    username=message.chat.username
    first_name=message.chat.first_name
    last_name=message.chat.last_name

    if not db.user_exists(chatId):
        db.add_user(tg_id=chatId,
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    )

    await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=home)
