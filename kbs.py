from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_weather = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('Khlebnikovo')
b2 = KeyboardButton('Batumi')
b3 = KeyboardButton('Cancel')

kb_weather.row(b1,b2)
kb_weather.add(b3)

kb_exchange = ReplyKeyboardMarkup(resize_keyboard=True)
b4 = KeyboardButton('dollar_rub')
b5 = KeyboardButton('lari_rub')
b6 = KeyboardButton('Cancel')

kb_exchange.row(b4,b5)
kb_exchange.add(b6)