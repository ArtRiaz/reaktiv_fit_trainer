from aiogram import types, Dispatcher, Bot
from aiogram.dispatcher.filters import Text
from keyboards.inline import registr_back, get_back
import asyncio

async def cmd_service(call: types.CallbackQuery):
    with open('sert1.jpg', 'rb') as photo1:
        await call.message.answer_photo(photo=photo1)
        sertifacates_list = ['sert2.jpg', 'sert3.jpg', 'sert4.jpg']
        for sert in sertifacates_list:
            await asyncio.sleep(1)
            await call.message.answer_photo(photo=open(f'{sert}', 'rb'))

        # await asyncio.sleep(1)
        #
        # await call.message.answer_photo(photo=open('sert3.jpg', 'rb'))
        #
        # await asyncio.sleep(1)
        #
        # await call.message.answer_photo(photo=open('sert4.jpg', 'rb'))

        await call.message.answer('Всі сертітфікати дійсні у 2024 році', reply_markup=get_back())


def register_handler_sertificate(dp: Dispatcher):
    dp.register_callback_query_handler(cmd_service, text='sertificate')

