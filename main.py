import asyncio
import logging

from config import load_config
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from handlers.start import register_handlers_start
from handlers.contacts import register_handler_contact
from handlers.back_menu import register_handler_back
from handlers.services import register_handler_service
from handlers.tests import register_handler_tests
from handlers.about import register_handler_about
from handlers.register import handlers_form
from handlers.sertificate import register_handler_sertificate
from handlers.reviews import register_handler_reviews
from handlers.exercises import register_handler_exercises


from utils.set_command_default import set_commands
from middlewares.anti_time import Anti_time

from admin_panel.admin_keyboards import register_handler_admin
from admin_panel.mailing import register_handler_mailing
from admin_panel.statistics import register_handler_statistics

logger = logging.getLogger(__name__)


def register_all_middleware(dp):
    dp.setup_middleware(Anti_time())


def register_all_handlers(dp):
    register_handlers_start(dp)
    register_handler_contact(dp)
    register_handler_back(dp)
    register_handler_service(dp)
    register_handler_tests(dp)
    register_handler_about(dp)
    handlers_form(dp)
    register_handler_sertificate(dp)
    register_handler_reviews(dp)
    register_handler_admin(dp)
    register_handler_mailing(dp)
    register_handler_exercises(dp)
    register_handler_statistics(dp)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s'
    )

    config = load_config(".env")

    bot = Bot(token=config.tg_bot.token, parse_mode="HTML")
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)
    bot['config'] = config  # доставать config из переменной bot, если в handler я хочу достать что то из Config
    # я делаю => bot.get("config")

    register_all_middleware(dp)
    # register_all_fillters(dp)
    register_all_handlers(dp)
    try:
        await dp.start_polling()
        await set_commands(bot=bot)
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await dp.bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stop")
