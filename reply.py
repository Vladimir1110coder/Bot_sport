from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

keyboard_start = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text = "Messi"),
            KeyboardButton(text = "Ronaldo"),
            KeyboardButton(text = "Neymar JR")
            ]
    ],
    resize_keyboard = True,
    input_field_placeholder = "Что ты выберешь?"

)
