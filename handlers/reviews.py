from aiogram import types, Dispatcher, Bot
from aiogram.dispatcher.filters import Text
from keyboards.inline import registr_back, get_back
import asyncio

async def cmd_reviews(call: types.CallbackQuery):
    with open('review1.png', 'rb') as photo1:
        await call.message.answer_photo(photo=photo1)
        reviews_list = ['review2.png', 'review3.png', 'review4.png', 'review5.png', 'review6.png', 'review7.png',
                        'review8.png']
        for review in reviews_list:
            await asyncio.sleep(1)

            await call.message.answer_photo(photo=open(f'{review}', 'rb'))

        #
        # await asyncio.sleep(1)
        #
        # await call.message.answer_photo(photo=open('review3.png', 'rb'))
        #
        # await asyncio.sleep(1)
        #
        # await call.message.answer_photo(photo=open('review4.png', 'rb'))
        #
        # await asyncio.sleep(1)
        #
        # await call.message.answer_photo(photo=open('review5.png', 'rb'))
        #
        # await asyncio.sleep(1)
        #
        # await call.message.answer_photo(photo=open('review6.png', 'rb'))
        #
        # await asyncio.sleep(1)
        #
        # await call.message.answer_photo(photo=open('review7.png', 'rb'))
        #
        # await asyncio.sleep(1)
        #
        # await call.message.answer_photo(photo=open('review8.png', 'rb'))


        await call.message.answer('<b>Якщо ти хочешь залишити свій відгук, \n'
                                  'напиши мені у особисті повідомлення.\n'
                                  'Твій відгук дуже важливий для мене!</b>', reply_markup=get_back())


def register_handler_reviews(dp: Dispatcher):
    dp.register_callback_query_handler(cmd_reviews, text='reviews')
