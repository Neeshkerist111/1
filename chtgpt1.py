import openai
import aiogram.dispatcher
import aiogram.utils
import aiogram.types
import aiogram.bot

API_TOKEN = "5932924279:AAHjbT6B1cIg83zMtI5YO9A5nLR3MQeEsas"

# Setup bot and dispatcher
bot = aiogram.bot.Bot(token=API_TOKEN)
dp = aiogram.dispatcher.Dispatcher(bot)

openai.api_key = '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'

@dp.message_handler(commands='start')
async def cmd_start(message: aiogram.types.Message):
    await message.answer("Hi there! I'm an AI language model created by OpenAI. How can I help you today?")

@dp.message_handler()
async def handle_text(message: aiogram.types.Message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.0,
        max_tokens=3500,
        top_p=0.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    await bot.send_message(chat_id=message.chat.id, text=response['choices'][0]['text'])

if __name__ == '__main__':
    import logging

    logging.basicConfig(level=logging.INFO)
    aiogram.executor.start_polling(dp, skip_updates=True)
