from aiogram import types, Dispatcher, Bot
from aiogram.dispatcher.filters import Text
from keyboards.inline import registr_back
import asyncio


async def cmd_service(call: types.CallbackQuery):
    photos = ['services.jpg', 'serv2.jpg', 'services3.png']
    captions = [f'<b>МОЇ ПОСЛУГИ:</b>\n'
                f'📍<b>Release and Activation\n</b>'
                'Сеанс тренувальної сесії повʼязаний з міофасціальним релізом та вправами пов’язаних з активацією '
                ', направлених на пошук та ліквідацію дисфункцій м’язового і опорно-рухового апарату.\n'
                '\n'
                '📍<b>Pattern’s Training\n</b>'
                'Тренування присвячене  корекційній системі тренування з використанням рухових патернів тіла , '
                'центром маси , гравітацією та силою опори\n'
                '\n'
                '📍<b>Strength and Correction</b>\n'
                'Тренування базується на навчальній методиці ,  програму присвячену корекційному тренінгу з '
                'використанням силових вправ , як в тренажерному залі так і з вільною вагою . Нові алгоритми '
                'побудови тренувальних процесів на основі скрінінгів , впроваджених інститутом корекційної '
                'постави.\n'
                '\n'
                '📍<b>HIIT Training</b>\n'
                'Тренування (HIIT, “High-Intensity Interval Training”) – це високоінтенсивний інтервальний '
                'тренінг, який являє собою силове або кардіо тренування з послідовним чергуванням максимальних, '
                'середніх і помірних рівнів навантажень.',
                '<b>ВИДИ ГРУПОВИХ ЗАНЯТЬ:</b>\n'
                '⁃ MICT ( низько-інтенсивне навантаження)\n'
                '⁃ HIIT ( високо-інтенсивне навантаження)\n'
                '⁃ SIT ( Швидкі спринти )\n'
                '⁃ Power Functional\n'
                '⁃ TAE-BO\n'
                '⁃ CrossFit : EMOM , AMRAP\n'
                '⁃ Hips&Bums\n'
                '⁃ ABS ( core )\n'
                '⁃ Stretching\n'
                '⁃ TRX\n'
                '⁃ PUMP\n'
                '⁃ Body Sculpt\n'
                '⁃ Station Change',
                f'<b>💪Занурюй у світ фітнесу разом зі '
                f'мною!</b>\n'
                f'Натисни на посилання нижче 👇\n'
                '\n'
                'Групові тренування 👇\n'
                'https://youtube.com/shorts/igO-WGvHoAw?feature=share\n'
                'Онлайн тренування 👇\n'
                'https://youtube.com/shorts/J4p6yKRlucc\n'

                ]

    for photos1, caption1 in zip(photos, captions):
        with open(f'{photos1}', 'rb') as photo:
            await call.message.answer_photo(
                photo=photo,
                caption=caption1,
            )
            await asyncio.sleep(0.5)
    await call.message.answer('<b>Приєднуйтесь до нас!</b>', reply_markup=registr_back())
    await call.message.edit_reply_markup()


def register_handler_service(dp: Dispatcher):
    dp.register_callback_query_handler(cmd_service, text='service')
