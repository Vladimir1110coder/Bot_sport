from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

def get_keyboard(
        *,
        btns = dict[str, str],
        sizes = (2,)
):

    keyboard = InlineKeyboardBuilder()

    for text, data in btns.items():
        if "https://" in data:
            keyboard.add(InlineKeyboardButton(text = text, url = data))
        else:
            keyboard.add(InlineKeyboardButton(text = text, callback_data = data))

    return keyboard.adjust(*sizes).as_markup()
