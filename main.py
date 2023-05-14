from Bard import Chatbot
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from environs import Env

env = Env()
env.read_env()

telegram_token = env.str('TELEGRAM_TOKEN')
bard_token = env.str('BARD_SESSION')

bot = Bot(token=telegram_token)
dp = Dispatcher(bot)
chatbot = Chatbot(session_id=bard_token)

# For the bot to work, you need a US proxy or VPN
proxy = env.str('PROXY', None)
chatbot.session.proxies.update({"http": proxy, "https": proxy})


@dp.message_handler()
async def send(message: types.Message):
    try:
        await message.answer('Google Bard writes...')
        await message.answer_chat_action('typing')
        response = chatbot.ask(message.text)
        await message.answer(response.get('content'), parse_mode="markdown")
    except Exception as ex:
        await message.answer(str(ex))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
