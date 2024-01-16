from aiogram import types, Dispatcher
import asyncio
from aiogram.dispatcher.filters import Text
from keyboards.inline import get_back

async def get_exersices(call: types.CallbackQuery):
    await call.message.answer('<b>Дорогі друзі,\n'
                              'я підготував для вас  дуже цікаві та корисні вправи,\n'
                              'щоб побачити вправи натиснить на посилання під описом кожної вправи👇</b>')
    photos = ['p22.png', 'p23.png', 'p31.png', 'p4.png', 'p11.png']
    captions = [
                'Давайте все-таки вирішимо , який тип мʼязових волокон у вас переважає .\n'
                'Підготував для вас легкий тест , який дасть вам відповідь.\n'
                '\n'
                'На сьогодні наука нам дає :\n'
                '- 1 тип МВ\n'
                '- 2А тип МВ\n'
                '- 2В тип МВ\n'
                '\n'
                'Відповіді :\n'
                'Якщо у вас 1 тип МВ , то ви здатні виконувати повільну роботу, але на довгий термін.\n'
                '\n'
                'Якщо у вас 2А ,то ви здатні виконувати середній темп роботи та середній час роботи .\n'
                '\n'
                'Якщо у вас 2В , то ви здатні до швидкої , вибухової роботи, але на короткий період часу.\n'
                'Натисніть на посилання нижче 👇\n'
                'https://youtu.be/qQ9A-AoqyW0',
                'Мій три-сет  на ноги с власною вагою\n'
                'Темп : 4х4 повільно \n'
                '4-6 Повторів\n'
                'Натисніть на посилання нижче 👇\n'
                'https://youtube.com/shorts/VsJ9Ua8opOw',
                'Мій три-сет  на сідниці с власною вагою\n'
                'Натисніть на посилання нижче 👇\n'
                'https://youtube.com/shorts/AQAA8LsfWd0',
                'Три-сет на прес\n'
                'Натисніть на посилання нижче 👇\n'
                'https://youtube.com/shorts/eOlkTsXUgW0',
                'Три-Сет на спину в домашніх умовах\n'
                'Натисніть на посилання нижче 👇\n'
                'https://youtube.com/shorts/dAGs-aKuUCg'

                ]

    for photo, caption in zip(photos, captions):
        with open(f'{photo}', 'rb') as photos:

            await call.message.answer_photo(photo=photos, caption=caption)
            await asyncio.sleep(0.5)
    await call.message.answer('<b>Приєднуйтесь до нас!</b>', reply_markup=get_back())


def register_handler_exercises(dp: Dispatcher):
    dp.register_callback_query_handler(get_exersices, text='exercises')
