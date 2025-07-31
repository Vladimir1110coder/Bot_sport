from aiogram import Dispatcher, Bot
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
from aiogram.fsm.strategy import FSMStrategy
from handlers.user import user_router
from Database.engine import on_create, on_drop, session_maker
from middlewares.db import DataBaseSession
import os
import asyncio



bot = Bot(token = os.getenv("TOKEN"))
bot.my_admins_list = []

ALLOWED_UPDATES = ["message", "edited_message"]

dp = Dispatcher(fsm_strategy = FSMStrategy.USER_IN_CHAT)

dp.include_router(user_router)


admins_list = []

async def create(bot):
    remove = False
    if remove:
        await on_drop()
    await on_create()

async def shutdown(bot):
    print("Бот лёг")


async def main():
    dp.startup.register(create)
    dp.shutdown.register(shutdown)
    dp.update.middleware(DataBaseSession(session_pool = session_maker))
    await bot.delete_webhook(drop_pending_updates = True)
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


asyncio.run(main())