from aiogram import Bot, Dispatcher

ADMINS = [908379438, 5517017632]
COINGECKO_API_URL = 'https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd'
TOKEN = "6974809575:AAH6rbh5Y8vmcqXiPpAx5LTT1d9PNogNk4w"
bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot=bot)
