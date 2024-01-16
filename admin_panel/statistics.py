from aiogram import types
from data.db import DBCommands
from aiogram.dispatcher.filters import Text
db = DBCommands()


async def count(callback: types.CallbackQuery):
    data = await db.show_users()
    await callback.message.answer(f'Кількість користувачів {data}')


def register_handler_statistics(dp):
    dp.register_callback_query_handler(count, text='statistics')
