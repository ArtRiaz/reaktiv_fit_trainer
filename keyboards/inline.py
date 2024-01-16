from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


def kb_menu():
    kb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton('👇Меню', callback_data='menu')
    ]])

    return kb


def get_kb_menu():
    kb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton('🦾Послуги', callback_data="service"),
        InlineKeyboardButton('🏃‍Про мене', callback_data="about"),
        InlineKeyboardButton('📲Питання', url='t.me/reaktiv_fit_trainer')
    ],

        [
            InlineKeyboardButton('👨🏼‍💻Реєстрація на тренування', callback_data="consultasion")
        ], [
            InlineKeyboardButton('💪Комплексні сети', callback_data="exercises")
        ], [
            InlineKeyboardButton('📩Відгуки', callback_data="reviews")
        ], [
            InlineKeyboardButton('☎️Контакти', callback_data="contact")
        ]

    ])

    return kb


def ikb_contact():
    ikb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton('👨🏼‍💻Instagram', url='https://www.instagram.com/reaktiv_fit_trainer_?igsh'
                                                  '=MXJ2YmE4Mmh3bzI3aw%3D%3D&utm_source=qr')
    ], [
        InlineKeyboardButton('📞 +38(097)-048-53-37', callback_data='calling')
    ], [
        InlineKeyboardButton('↩️ Назад у головне  меню', callback_data="back_general_menu")
    ]])

    return ikb


def get_back():
    ikb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton('↩️ Назад у головне  меню', callback_data="back_general_menu")
    ]])

    return ikb


def registr_back():
    ikb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton('👨🏼‍💻Реєстрація на тренування', callback_data="consultasion")
    ], [
        InlineKeyboardButton('↩️ Назад у головне  меню', callback_data="back_general_menu")
    ]])
    return ikb


def sert_back():
    ikb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton('🎫 Мої сертіфікати', callback_data='sertificate')
    ], [InlineKeyboardButton('↩️ Назад у головне  меню', callback_data="back_general_menu")]])

    return ikb
