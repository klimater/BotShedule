import asyncio
from Token import TOKEN
from parse_shedule import result_shedule
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram.utils.keyboard import ReplyKeyboardBuilder

dp = Dispatcher()

def keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text = "Расписание")
    return builder.as_markup(resize_keyboard = True)


@dp.message(CommandStart())
async def get_start(message: Message,  bot: Bot):
    await bot.send_message(message.from_user.id, 
                           f"Привет {message.from_user.first_name}.\nЯ бот с расписанием.\nНажми на /keyboard и получишь актуальное расписание на сегодня.")

@dp.message(Command("keyboard"))
async def command_keyboard(message: Message) -> None:
    await message.answer("Нажми на кнопку.", reply_markup = keyboard())

@dp.message()
async def handle_message(message: types.Message, bot: Bot):
    text = message.text
    if (text == "Расписание"):
        await bot.send_message(message.from_user.id, f"Дата {result_shedule}")

async def main():
    bot = Bot(TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())