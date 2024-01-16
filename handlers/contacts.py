from keyboards.inline import ikb_contact, get_back
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text


async def cmd_contact(call: types.CallbackQuery):
    await call.message.answer("Як зі мною зв'язатись:", reply_markup=ikb_contact())
    await call.message.edit_reply_markup()
    await call.message.delete()


async def send_phone(callback: types.CallbackQuery):
    await callback.message.bot.send_contact(chat_id=callback.from_user.id,
                                            phone_number='+38097-048-53-37',
                                            first_name='Твій Тренер',
                                            reply_markup=get_back())


def register_handler_contact(dp: Dispatcher):
    dp.register_callback_query_handler(cmd_contact, text="contact")
    dp.register_callback_query_handler(send_phone, text='calling')
