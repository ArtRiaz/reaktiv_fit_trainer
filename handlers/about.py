from aiogram import types, Dispatcher, Bot
from aiogram.dispatcher.filters import Text
from keyboards.inline import sert_back


async def cmd_about(call: types.CallbackQuery):
    with open('about.jpg', 'rb') as photo:
        await call.message.answer_photo(photo=photo, caption='Микита Занемонський ( reaktiv_fit_trainer )\n'
                                                             '🥇Personal Trainer\n'
                                                             '🥈Group Coach \n'
                                                             '🥉 Online Trainer\n'
                                                             'Ambassador  «Mood_Stores_» \n'
                                                             'Презентор : «For Fit Day 2023 Odesa »\n'
                                                             '1 вищі освіта\n'
                                                             '\n'
                                                             'Сертифікований тренер міжнародної навчальної академії EREPS в Україні «ForFitAcademy», за темами :\n'
                                                             '📍 Release and Activation\n'
                                                             '📍 Patterns Training \n'
                                                             '📍 HIIT  Training \n'
                                                             '📍 Bands Training\n'
                                                             '📍Strength and Correction ( Upper Body , Low Body )\n'
                                                             '📍Body Weight Training \n'
                                                             '📍Functional  Step \n'
                                                             '📍Women’s Training \n'
                                                             '📍 Strength with free weight \n'
                                                             '\n'
                                                             'Учасник 4-х всеукраїнських  фітнес конвенції ForFitDay та майстер-класів за напрямками «Dynamic Postural»,\n'
                                                             '«Bodyweight training» , «Functional Step » , «Brand Name » \n'
                                                             'Учасник 3-х Fitness Camp ( Bukovel , Ukraine 🇺🇦)',
                                        reply_markup=sert_back())
        await call.message.edit_reply_markup()
        await call.message.delete()


def register_handler_about(dp: Dispatcher):
    dp.register_callback_query_handler(cmd_about, text='about')
