from asyncio import sleep
from aiogram.dispatcher.filters import Text
from aiogram import types, Dispatcher
from config import load_config
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

config = load_config()


# Keyboards

def menu_admin_panel():
    ikb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton('📥 Розсилання', callback_data='sending')
    ], [
        InlineKeyboardButton('📊 Статистика', callback_data='statistics')
    ]])
    return ikb


def back_admin_panel():
    ikb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton('↩️ Назад у меню адміна', callback_data='back_admin_panel')
    ]])
    return ikb


# Админ панель
async def admin_panel(message: types.Message):
    await message.answer_sticker(sticker="CAACAgEAAxkBAAEJ78Bkz6Cp-U71pthpElEDBxjIfT8VdAACMQIAAoKgIEQHCzBVrLHGhy8E")
    await sleep(3)
    await message.answer_sticker(sticker="CAACAgIAAxkBAAEJ76Rkz5pVqYHtFcLn9EwC2gpAqT-R8wACxgEAAhZCawpKI9T0ydt5Ry8E")
    await message.answer("Привіт Адмін!!!!", reply_markup=menu_admin_panel())


# Назад в админ панель
async def back_admin(call: types.CallbackQuery):
    await call.message.answer("Ви повернулись у меню адміна", reply_markup=menu_admin_panel())


def register_handler_admin(dp: Dispatcher):
    dp.register_message_handler(admin_panel, Text(equals="reaktiv"), user_id=config.tg_bot.admin_ids)
    dp.register_callback_query_handler(back_admin, text="back_admin_panel")
