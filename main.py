from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import math
TOKEN = '5814467709:AAHSc6qzjNHoHC01CCq9Nqbg8LEQaC2gD0w'


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("/start - очевидно\n/help - очевидно\n"
                        "/prop - все ваше будующее\n/past - тоже самое но с прошлым"
                        "\n/meth5 - его я еще не придумал\n/resmeth - " 
                       "\n/sin2x - выводит  x от вашего х")

@dp.message_handler(commands=['prop'])
async def process_start_command(message: types.Message):
    await message.reply("у вас будет быстрый сон")

@dp.message_handler(commands=['past'])
async def process_start_command(message: types.Message):
    await message.reply("у вас был тяжелый день")
@dp.message_handler(commands=['sin2x'])
async def process_start_command(message: types.Message):
    await message.reply("введите х")
@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)



if __name__ == '__main__':
    executor.start_polling(dp)