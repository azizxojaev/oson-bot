from aiogram import types


async def start_keyboard(location):
    btn = types.ReplyKeyboardRemove()
    btn = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn.row('🔍 Начать поиск')
    btn.row('✍️ Оставить отзыв', '🔄 Изменить язык')
    btn.row(f'📍 Мое местоположение: {location}')
    btn.row('Как пользоваться❓')
    return btn


async def find_keyboard():
    btn = types.ReplyKeyboardRemove()
    btn = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn.row('🏠️ Главное меню')
    return btn


async def changeLang_keyboard():
    btn = types.ReplyKeyboardRemove()
    btn = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn.row('🇺🇿 UZ', '🇷🇺 RU', '🇺🇸 EN')
    btn.row('⏪ Назад')
    return btn


async def selectLocation_keyboard():
    btn = types.ReplyKeyboardRemove()
    btn = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn.row('По всему узбекистану')
    btn.row('Республика Каракалпакстан')
    btn.row('Ташкент') 
    btn.row('Ташкентская область') 
    btn.row('Андижан') 
    btn.row('Бухара') 
    btn.row('Самарканд') 
    btn.row('Джизак') 
    btn.row('Кашкадарья') 
    btn.row('Навои') 
    btn.row('Наманган') 
    btn.row('Сурхандарья') 
    btn.row('Сырдарья') 
    btn.row('Фергана') 
    btn.row('Хорезм') 
    return btn