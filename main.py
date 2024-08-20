import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram_dialog import setup_dialogs
from tortoise import Tortoise

from config_data import config
from handlers import setup_message_routers
from dialog import setup_aiogram_dialogs


async def on_startup() -> None:
    await Tortoise.init(db_url=config.DB_URL.get_secret_value(), modules={'models': ['module.database']})
    await Tortoise.generate_schemas()


async def on_shutdown() -> None:
    await Tortoise.close_connections()


async def main() -> None:
    bot = Bot(
        config.BOT_TOKEN.get_secret_value(),
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    dp = Dispatcher()

    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    message_routers = setup_message_routers()
    dialog_routers = setup_aiogram_dialogs()
    dp.include_router(message_routers)
    dp.include_router(dialog_routers)
    setup_dialogs(dp)

    await bot.delete_webhook(True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())