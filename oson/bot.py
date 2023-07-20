import logging

from aiogram import Bot, Dispatcher, executor, types
from keyboards import *

BOT_TOKEN = 'YOUR TOKEN'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

location = 'Ташкент'
find_check = False
location_check = False


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    global location
    global find_check
    btn = await start_keyboard(location)
    await message.answer('💊 Введите название лекарства', reply_markup=btn)


@dp.message_handler(text='🔍 Начать поиск')
async def find(message: types.Message):
    global find_check
    await message.answer('💊 Отправьте название лекарства (не менее 3 букв)')
    find_check = True
@dp.message_handler(text='🏠️ Главное меню')
async def main(message: types.Message):
    global find_check
    find_check = False
    btn = await start_keyboard(location)
    await message.answer('💊 Введите название лекарства', reply_markup=btn)


@dp.message_handler(text='✍️ Оставить отзыв')
async def main(message: types.Message):
    await message.answer('Уважаемый пользователь, через этот бот Вы можете направить свои мнения и предложения. @osonaptekamurojatbot.')


@dp.message_handler(text='🔄 Изменить язык')
async def main(message: types.Message):
    btn = await changeLang_keyboard()
    await message.answer('Выберите язык 👇', reply_markup=btn)
@dp.message_handler(text='⏪ Назад')
async def main(message: types.Message):
    btn = await start_keyboard(location)
    await message.answer('💊 Введите название лекарства', reply_markup=btn)


@dp.message_handler(text_contains='📍 Мое местоположение: ')
async def main(message: types.Message):
    global location_check
    btn = await selectLocation_keyboard()
    await message.answer('Выберите город', reply_markup=btn)
    location_check = True


@dp.message_handler(text='Как пользоваться❓')
async def main(message: types.Message):
    await message.answer_video(types.InputFile('use_bot.mp4'))

@dp.message_handler()
async def messages(message: types.Message):
    if find_check == True:
        btn = await find_keyboard()
        await message.answer('❗️По этому запросу ничего не найдено. 💊 Отправьте название лекарства (не менее 3 букв)', reply_markup=btn)
    elif location_check == True:
        location = message.text
        btn = await start_keyboard(location)
        await message.answer('💊 Введите название лекарства', reply_markup=btn)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
