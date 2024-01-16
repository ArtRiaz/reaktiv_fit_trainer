from aiogram import types, Dispatcher, Bot
from aiogram.dispatcher.filters import Text
from keyboards.inline import kb_menu, get_kb_menu
from data.db import create_db, DBCommands


db = DBCommands()

async def cmd_start(message: types.Message):
    with open('photo_start.jpg', 'rb') as photo:
        await create_db()
        await message.answer_photo(
            photo=photo,
            caption=f'<b>Привіт, {message.from_user.full_name}!\n</b>'
                    f'<b>Мене звати , Микита 💪\n'
                    f'Я фітнес тренер з міжнародною акредитацією !\n'
                    f'Я створив цей бот для більш зручної комунікації з вами.\n'
                    f'В моєму телеграм боті ви зможете знайти всю інформацію : Про мене , мої послуги , '
                    f'мої контакти, зможете особисто написати мені і зареєструватися на тренування</b>',
            reply_markup=kb_menu()
        )
        await db.add_new_user()


async def menu(callback: types.CallbackQuery):
    await callback.message.answer('Управління меню:', reply_markup=get_kb_menu())
    # await callback.message.delete()


def register_handlers_start(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=['start'])
    dp.register_callback_query_handler(menu, text='menu')
