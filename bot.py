from conf import token_bot
from weather import get_weather
from aiogram import Bot, executor, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from week import week,date_now, what_day_of_week
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from kbs import kb_weather, kb_exchange
from exchange import get_exchange


abc = """
<b>/help</b> - <em>список комманд</em>
<b>/start</b> - <em>начать работу с ботом</em>
<b>/creator</b> - <em>показать создателя</em>
<b>/weather</b> - <em>узнать погоду</em>
<b>/exchange</b> - <em>курс валют</em>
"""

storage = MemoryStorage()
bot = Bot(token_bot)
dp = Dispatcher(bot=bot, storage=storage)

creator = InlineKeyboardButton(text='StButcher',
                               url='https://www.instagram.com/stbutcher/')

class ClientStatesGroup(StatesGroup):
    city = State()
    exchange = State()

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer_photo(photo=open('pictures/what do you want.jpg', 'rb'))
    await message.delete()

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=abc,  parse_mode='HTML')
    await message.delete()

@dp.message_handler(commands=['creator'])
async def creator_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Вот инста хозяина',
                           reply_markup=InlineKeyboardMarkup(row_width=1).add(creator))
    await message.delete()

@dp.message_handler(commands=['weather'])
async def weather_command(message: types.Message):
    await message.delete()
    await ClientStatesGroup.city.set()
    await message.answer('В каком городе ходите узнать?', reply_markup=kb_weather)

@dp.message_handler(state=ClientStatesGroup.city)
async def load_city(message: types.Message, state: FSMContext):
    if message.text.lower() != 'cancel':
        await message.answer(get_weather(message.text))
    await message.answer('Пожалуйста', reply_markup = types.ReplyKeyboardRemove())
    await state.finish()

@dp.message_handler(commands=['exchange'])
async def exchange_command(message: types.Message):
    await message.delete()
    await ClientStatesGroup.exchange.set()
    await message.answer('Какая валюта интересует?', reply_markup=kb_exchange)

@dp.message_handler(state=ClientStatesGroup.exchange)
async def load_exchange(message: types.Message, state: FSMContext):
    if message.text.lower() != 'cancel':
        await message.answer(get_exchange(message.text))
    await message.answer_sticker(sticker='CAACAgIAAxkBAAEJBUZkZgI3yR6jr9JTFfIPrKZv6spBhQAC7QYAAkb7rASusnq3cIRG2y8E'
                                 , reply_markup = types.ReplyKeyboardRemove())
    await state.finish()

@dp.message_handler(content_types=['text'])
async def get_user_text(message: types.Message):
    if message.text.lower() == 'кто твой хозяин?':
        await bot.send_message(chat_id=message.chat.id,
                               text='Вот инста хозяина',
                               reply_markup=InlineKeyboardMarkup(row_width=1).add(creator))
    elif 'что у нас сегодня' in message.text.lower():
        await message.answer(f'Вроде {week[date_now.weekday()]}')
    elif 'какой день недели' in message.text.lower():
        answer = what_day_of_week(message.text.lower())
        await message.answer(answer)
        if answer == 'мне так не понятно...':
            await message.answer_sticker(
                             sticker="CAACAgIAAxkBAAEHg9Bj18gcFfcazFLufRv_T1cFnFcHRgACIAMAAs-71A4jijg8wgu1oC0E")
    elif message.text.lower() == 'погода':
        await weather_command(message)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

