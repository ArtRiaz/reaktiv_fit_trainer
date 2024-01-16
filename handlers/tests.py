from aiogram import types, Dispatcher, Bot
from aiogram.dispatcher.filters import Text
from keyboards.inline import get_back
from aiogram.types.input_media import InputMediaVideo, InputFile


async def cmd_tests(call: types.CallbackQuery):
    with open('test.png', 'rb') as photo:
        await call.message.answer_photo(photo=photo, caption='💪Test №1\n'
                                                                             '<b>Humeral Glenoid Adduction Test</b>\n'
                                                                             '\n'
                                                                             '<b>Goal:</b> 30 degrees\n'
                                                                             '<b>Testing for:</b> Anterior & '
                                                                             'Posterior Upper Expansion(T2-4)\n'
                                                                             '\n'
                                                                             '<b>Test is over when:</b>\n'
                                                                             '📍Posterior shoulder comes off ground\n'
                                                                             '📍Singnificant restriction is felt\n'
                                                                             '\n'
                                                                             'Побачити тест, натиснить сюди👇\n'
                                                                             'https://youtube.com/shorts/nldFae01I-c'
                                  )
        await call.message.edit_reply_markup()
        await call.message.delete()


def register_handler_tests(dp: Dispatcher):
    dp.register_callback_query_handler(cmd_tests, text='tests')