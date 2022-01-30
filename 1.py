"""
 This is a echo bot.
 It echoes any incoming text messages.
 """
 
import logging
from transliterate import to_cyrillic, to_latin
from aiogram import Bot, Dispatcher, executor, types
 
API_TOKEN = 'BOT TOKEN ni qoying'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
   """
    await message.reply("salom!\nI'm transliterateBot!\nPowered by @kow.")



@dp.message_handler()
async def send(message: types.Message):
        matn=message.text
        if matn.isascii():
                javob=to_cyrillic(message.text)
                await message.answer(javob)
        else:
                javob=to_latin(message.text)
                await message.answer(javob)
'''
    try:
        respond = wikipedia.summary(massage.text)
        await message.answer(respond)
    except:
        await message.answer("bu mavzuga oid maqola topilmadi")
  '''      
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)




'''


from transliterate import to_cyrillic, to_latin
import telebot
#---bot bn ulanish url ----#
url ='5104481022:AAE5wSkIfRUHjUOVZ6Ead9s-nKN-yE4rfuw'
bot = telebot.TeleBot(url, parse_mode=None)

#---start va help ni ulash---#

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Assalom alaykum, Xush kelibsiz!")

bot.infinity_polling()






matn = input ('matinni kiriting:')
if matn.isascii():
    print(to_cyrillic(matn))
else:
    print(to_latin(matn))
'''
