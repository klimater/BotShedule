import asyncio
from Token import TOKEN
from datetime import date
from parse_shedule import sсheduleParse
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram.utils.keyboard import ReplyKeyboardBuilder


dp = Dispatcher()
today = "2024-04-03"
new_today = date.today()
schedule_today = """
03.04.2024📅
1 пара: Современные программные средства Лекции Е.Б. Абарникова 204/5
2 пара: Алгоритмизация и программирование Лекции Е.В. Абрамсон 204/5
3 пара: ИЯ Практические занятия (УГ-1_ПР) О.И. Лопатина 312/1
4 пара: 
5 пара: 
6 пара: 
"""

if today != new_today:
    schedule_today = sсheduleParse()
    today = new_today

#список кнопок
def keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text = "Расписание")
    return builder.as_markup(resize_keyboard = True)

#обработчик команды старт
@dp.message(CommandStart())
async def get_start(message: Message,  bot: Bot):
    await bot.send_message(message.from_user.id, 
                           f"Привет {message.from_user.first_name}.\nЯ бот с расписанием.\nНажми на /keyboard и получишь актуальное расписание на сегодня.")

#вывод кнопок на экран пользователя
@dp.message(Command("keyboard"))
async def command_keyboard(message: Message) -> None:
    await message.answer("Нажми на кнопку.", reply_markup = keyboard())

#проверка текста сообщения от пользователя
@dp.message()
async def handle_message(message: types.Message, bot: Bot):
    text = message.text
    if (text == "Расписание"):
        await bot.send_message(message.from_user.id, f"Дата {schedule_today}")

async def main():
    bot = Bot(TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())