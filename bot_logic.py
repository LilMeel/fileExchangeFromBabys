from aiogram import Bot, types, executor
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import KeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from db_connection import try_to_add
from config import TOKEN

storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

class Form(StatesGroup):
    check_login = State()
    check_password = State()


def check_symbols(pass_str):
    res_sum = 0
    for symbol in pass_str:
        if 'a'<= symbol <='z':
            res_sum += 1
        elif 'A'<= symbol <='Z':
            res_sum += 1
        elif '0' <= symbol <= '9':
            res_sum += 1
    if(res_sum == 3):
        return True
    return False


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Это регистрация на ресурсе stole a stone")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = KeyboardButton('Регистрация - /register')
    button_2 = KeyboardButton('Сменить пароль - /restore')
    await message.reply("Выберите действие: ", reply_markup=keyboard.add(button_1, button_2))


@dp.message_handler(lambda message: message.text.split()[-1] == "/register")
async def process_register(message: types.Message):
    await bot.send_message(message.from_user.id, text="Введите логин: ")
    await Form.check_login.set()


@dp.message_handler(lambda message: message.text.split()[-1] == "/restore")
async def reg_new_user(message: types.Message):
    await message.reply("Это регистрация на ресурсе stole")


@dp.message_handler(state=Form.check_password)
async def process_check_password(message: types.Message, state: FSMContext):
    password = message.text
    if len(login) > 32 or len(login) < 8:
        await message.reply("Недопустимая длина пароля! Допускается от 8 до 32 символов")
    if not check_symbols(password):
        await message.reply("В пароле должна быть хотя бы одна: \n цифра, \n маленькая буква, \n заглавная буква")
    async with state.proxy() as data:
        data['ref1'] = password


@dp.message_handler(state=Form.check_login)
async def process_check_login(message: types.Message, state: FSMContext):
    login = message.text
    if(len(login) > 32 or len(login) < 8):
        await message.reply("Недопустимая длина логина! Допускается от 8 до 32 символов")
        return
    await Form.check_password.set()
    async with state.proxy() as data:
        password = data['ref1']
        try_to_add(login, password)



def login():
    executor.start_polling(dp)


