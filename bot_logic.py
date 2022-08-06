from aiogram import Bot, types, executor
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import KeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from db_connection import try_to_add
from config import TOKEN, RESTORE_QUESTIONS

storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)

class Form(StatesGroup):
    check_login = State()
    check_password = State()
    check_restore_question = State()


def check_symbols(pass_str):
    conditions = [0, 0, 0, 1]
    for symbol in pass_str:
        if 'a'<= symbol <='z':
            conditions[0] = 1
        elif 'A'<= symbol <='Z':
            conditions[1] = 1
        elif '0' <= symbol <= '9':
            conditions[2] = 1
        elif symbol == " ":
            conditions[3] = 0
    if 0 in conditions:
        return False
    return True


def questions_payload():
    payload = ""
    for question in RESTORE_QUESTIONS:
        payload += question + '\n'
    return payload


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


@dp.message_handler(state=Form.check_login)
async def process_check_login(message: types.Message, state: FSMContext):
    login = message.text
    if len(login) > 32 or len(login) < 5:
        await message.reply("Недопустимая длина логина! Допускается от 5 до 32 символов")
        return
    async with state.proxy() as data:
        data['ref1'] = login
    await bot.send_message(message.from_user.id, text="Введите пароль: ")
    await Form.check_password.set()


@dp.message_handler(state=Form.check_password)
async def process_check_password(message: types.Message, state: FSMContext):
    password = message.text
    if len(password) > 32 or len(password) < 8:
        await message.reply("Недопустимая длина пароля! Допускается от 8 до 32 символов")
    if not check_symbols(password):
        await message.reply("В пароле должна быть хотя бы одна: \n1.Цифра, \n2.Маленькая буква, \n3.Заглавная буква")
        return
    async with state.proxy() as data:
        login = data['ref1']
        res = try_to_add(login, password)
        await message.reply(res)
    await state.finish()

"""@dp.message_handler(state=Form.check_restore_question)
async def process_check_restore_question(message: types.Message, state: FSMContext):
    await message.text("Выберите из списка: \n"+ questions_payload())
    await Form.check_restore_question().set()
    async with state.proxy() as data:
        
    answer = RESTORE_QUESTIONS[]"""



def start_bot():
    executor.start_polling(dp)


