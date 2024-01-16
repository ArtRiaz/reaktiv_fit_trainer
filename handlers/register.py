import asyncio
import pytz

from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types.message import ContentType
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from keyboards.inline import kb_menu, get_kb_menu, get_back
from aiogram.types import CallbackQuery
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, \
    ReplyKeyboardRemove
from config import load_config
from data.db import RegisterUser
import datetime

config = load_config()


class TraningOrder(StatesGroup):
    name = State()
    phone = State()
    training = State()


async def cancel(message: types.Message, state: FSMContext):
    await message.answer("Ви відмінили pеєстрація", reply_markup=ReplyKeyboardRemove())
    await state.reset_state()


async def order_start(call: types.CallbackQuery):
    await TraningOrder.name.set()
    await call.message.answer(
        "<b>Залиште свої контактні дані і я звʼяжуся з вами найближчим часом.</b>")
    await call.message.answer(f"Введіть своє ім'я або нажміть /cancel",
                              reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                               keyboard=[[KeyboardButton(
                                                                   f'{call.message.chat.first_name}')]]))


async def get_name(message: types.Message, state: FSMContext):
    name = message.text
    register = RegisterUser()
    register.name = name
    await TraningOrder.next()
    await state.update_data(register=register)
    await message.reply("Введіть свій контактний номер телефону або нажміть /cancel",
                        reply_markup=ReplyKeyboardRemove())


async def get_phone(message: types.Message, state: FSMContext):
    if all(c.isdigit() or c == "+" for c in message.text):  # проверка на цифры и символ +
        phone = message.text
        data = await state.get_data()
        register: RegisterUser = data.get("register")
        register.phone = phone
        await state.update_data(register=register)
        await TraningOrder.next()
        await message.answer("Введить яке тренування Ви обираєте: або нажміть /cancel",
                             reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                              keyboard=[[KeyboardButton(f'Онлайн')],
                                                                        [KeyboardButton(
                                                                            'Індівідуальне заняття у залі')]]))

    else:
        await message.answer("Введить вірний номер")


async def get_type(message: types.Message, state: FSMContext):
    train = message.text
    data = await state.get_data()
    register: RegisterUser = data.get("register")
    register.train = train
    await state.update_data(register=register)
    await register.create()

    await message.bot.send_sticker(chat_id=message.chat.id,
                                   sticker='CAACAgEAAxkBAAELGAtll9tFnhzmRvdBG5FCr3EVXtti9AACNAIAAgeG6Ueaxv72mQt9RDQE',
                                   reply_markup=ReplyKeyboardRemove())
    await message.answer("Дякую за Вашу регістрацію, я з Вами зв'яжусь, як можно скоріше!\n"
                         "Якщо ви бажаєте оплатити карткою, натисніть сюди 👇\n "
                         "<tg-spoiler><b>PrivatBank:</b> 5457082507230493</tg-spoiler>")

    await message.answer_photo(photo=open('qr.png', 'rb'), caption='<b>Або скористайтесь QR кодом</b>',
                               reply_markup=get_back())

    for admin in config.tg_bot.admin_ids:
        await message.bot.send_message(chat_id=admin,
                                       text=f'<b>Прийшов запит на тренування:\n'
                                            f'Імя: {register.name}\n'
                                            f'Номер телефона: {register.phone}\n'
                                            f'Тренування: {register.train}</b>'

                                       )

    await state.finish()


def handlers_form(dp: Dispatcher):
    dp.register_message_handler(cancel, commands=["cancel"], state=TraningOrder)
    dp.register_callback_query_handler(order_start, text='consultasion', state=None)
    dp.register_message_handler(get_name, state=TraningOrder.name)
    dp.register_message_handler(get_phone, state=TraningOrder.phone)
    dp.register_message_handler(get_type, state=TraningOrder.training)
