from telegram import update
from telegram.ext import Updater, CommandHandler
from telegram.ext.dispatcher import run_async
import requests
import re


def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    image_url = contents['url']
    return image_url

@run_async
def bop(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def main():
    updater = Updater('<token va acá>', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop', bop))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
