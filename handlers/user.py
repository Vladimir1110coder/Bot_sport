from aiogram import types, Router, F
from aiogram.types import CallbackQuery
from aiogram.filters import Command, CommandStart, StateFilter, or_f
from sqlalchemy.ext.asyncio import AsyncSession

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from filters.Chat_types import ChatTypeFilter
from reply import keyboard_start
from aiogram.types import Message
from Database.orm_query import orm_add_player, orm_get_players
from Inline import get_keyboard
from Statistic import static_Messi, static_Ronaldo, static_NeymarJR
import os


user_router = Router()
user_router.message.filter(ChatTypeFilter(["private"]))


class Add_GAME(StatesGroup):
    name = State()
    word = State()





@user_router.message(StateFilter(None), CommandStart())
async def start(message: types.Message, state: FSMContext, session: AsyncSession):
    await message.answer("Введи своё имя")
    await state.set_state(Add_GAME.name)


@user_router.message(Add_GAME.name, F.text)
async def start(message: types.Message, state: FSMContext, session: AsyncSession):
    await state.update_data(name = message.text)
    await message.answer("Выбери вариант ответа", reply_markup = keyboard_start)
    await state.set_state(Add_GAME.word)

@user_router.message(or_f(F.text == "Messi", F.text == "Ronaldo", F.text == "Neymar JR"), Add_GAME.word)
async def game_level1(message: types.Message, state: FSMContext, session: AsyncSession):
    if message.text == "Messi":
        await message.answer_photo(os.getenv("photo1"),
            caption = f"{message.text} Хороший выбор 👍",
                       reply_markup = get_keyboard(btns = {message.text : os.getenv("url1"),
                                                           "Достижения игрока": "Статистика_Messi"}))
    elif message.text == "Ronaldo":
        await message.answer_photo(os.getenv("photo2"),
            caption = f" {message.text} Хороший выбор 👍",
                       reply_markup = get_keyboard(btns = {message.text : os.getenv("url2"),
                                                           "Достижения игрока": "Статистика_Ronaldo"}))
    else:
        await message.answer_photo(os.getenv("photo3"),
            caption = f"{message.text} Хороший выбор 👍",
                       reply_markup = get_keyboard(btns = {message.text: os.getenv("url3"),
                                                           "Достижения игрока": "Статистика_NeymarJR"}))

    await state.update_data(word=message.text)
    data = await state.get_data()
    await orm_add_player(session, data)
    await state.clear()

@user_router.message(Command("admin"))
async def spisok_player(message: types.Message, session: AsyncSession):
    spisok = await orm_get_players(session)
    count_football = [player.word for player in spisok]
    await message.answer(f"----Статистика----\n"
                   f"Месси: {count_football.count("Messi")}\n"
                   f"Ronaldo: {count_football.count("Ronaldo")}\n"
                   f"Neymar JR: {count_football.count("Neymar JR")}")


@user_router.callback_query(F.data.startswith() == "Статистика_")
async def Messi_static(callback: types.CallbackQuery):
    name = await callback.data.split("_")[-1]
    if name == "Messi":
        result = await static_Messi()
    elif name == "Ronaldo":
        result = await static_Ronaldo()
    else:
        result = await static_NeymarJR()
    await callback.answer()
    await callback.message.answer(result)

@user_router.message(F.text == "Привет")
async def hello(message: types.Message):
    await message.answer()
