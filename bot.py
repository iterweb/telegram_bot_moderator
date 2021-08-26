import logging
import filters
from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN, ACCESS_DENIED_MESSAGE, BAN_MESSAGE, MUTE_TIME
from db_writer import DataWriter


db_write = DataWriter()

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['mute', 'info'], commands_prefix='!')
async def admin_command(message: types.Message):
    user_status = ['creator', 'administrator']
    member = await bot.get_chat_member(message.chat.id, message.from_user.id)

    if member['status'] in user_status:
        if message.text.startswith('!mute'):
            await message.delete()
            user_id = message.text.replace('!mute', '').strip()
            await bot.restrict_chat_member(message.chat.id, user_id, until_date=int(message.date.timestamp() + MUTE_TIME * 3600))
            await message.answer(f'{db_write.get_user_name(user_id)} - {BAN_MESSAGE}!')
        elif message.text.startswith('!info'):
            full_name = message.text.replace('!info', '').strip()
            await bot.send_message(message.from_user.id, db_write.get_user_info(full_name))
    else:
        await message.reply(ACCESS_DENIED_MESSAGE)


@dp.message_handler()
async def filter_message(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    full_name = message.from_user.full_name
    msg_date = message.date
    msg = message.text.lower()
    timestamp = message.date.timestamp()

    check_msg = await filters.filter_text(msg, user_id, int(timestamp))
    if check_msg:
        await message.delete()

    if str(message.from_user.id) not in db_write.get_all_users_id():
        db_write.save_user_data(user_id, user_name, full_name, msg_date, msg, timestamp)
    else:
        db_write.update_user_data(user_id, user_name, full_name, msg_date, msg, timestamp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
