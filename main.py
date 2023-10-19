from aiogram.utils import executor
import logging
from config import bot, dispatcher, COINGECKO_API_URL, ADMINS
import requests
from aiogram import types

curs = 0
comsa = 0


@dispatcher.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.from_user.id in ADMINS:
        await message.answer("чтобы поменять курс и комсу надо ввести\n"
                             "/set курс комса (пробел обязательно)")
    else:
        await message.reply(
            "Привет! Я бот для отслеживания цены Litecoin. Используйте команду "
            "/price, чтобы получить текущую цену Litecoin, или отправьте мне количество Litecoin для конвертации в USD.")


@dispatcher.message_handler(commands=['set'])
async def set_comsa_and_curs(message: types.Message):
    try:
        if message.from_user.id in ADMINS:
            mess = message.text.split()
            global curs, comsa
            curs = int(mess[1])
            comsa = int(mess[2])
            await message.answer("курс и комса поменялись")

    except IndexError:
        await message.answer("Проверьте правильность написания курса и комсы")


@dispatcher.message_handler(commands=['price'])
async def get_litecoin_price(message: types.Message):
    response = requests.get(COINGECKO_API_URL)
    if response.status_code == 200:
        data = response.json()
        litecoin_price = data.get('litecoin', {}).get('usd', 'N/A')
        await message.reply(f"Текущая цена Litecoin.: ${litecoin_price}")
    else:
        await message.reply("Не удалось получить цену Litecoin. Пожалуйста, попробуйте позже.")


@dispatcher.message_handler()
async def convert_to_usd(message: types.Message):
    try:
        litecoin_amount = float(message.text)
        response = requests.get(COINGECKO_API_URL)
        if response.status_code == 200:
            data = response.json()
            litecoin_price = data.get('litecoin', {}).get('usd', 'N/A')
            usd_value = int(litecoin_amount * litecoin_price * curs) + comsa
            await message.reply(f"{usd_value:,}")
        else:
            await message.reply("Не удалось получить цену Litecoin. Пожалуйста, попробуйте снова позже.")
    except ValueError:
        await message.reply("Неверный ввод. Пожалуйста, введите правильное количество Litecoin.")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dispatcher, skip_updates=True)