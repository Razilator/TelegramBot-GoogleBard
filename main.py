from Bard import AsyncChatbot
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from environs import Env

env = Env()
env.read_env()

secure_1PSID = env('SECURE_1PSID')
secure_1PSIDTS = env('SECURE_1PSIDTS')
telegram_token = env('TELEGRAM_TOKEN')

bot = Bot(token=telegram_token)
dp = Dispatcher(bot)


@dp.message_handler()
async def send(message: types.Message):
    try:
        chatbot = await AsyncChatbot.create(secure_1PSID, secure_1PSIDTS)  # it's sad that initialization happens every time a message is sent, I'll probably fix it sometime.
        await message.answer('Google Bard начинает думать...')
        await message.answer_chat_action('typing')
        answer = await chatbot.ask(message.text)
        await message.answer(answer.get('content'), parse_mode="markdown")
    except Exception as ex:
        await message.answer(str(ex))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
