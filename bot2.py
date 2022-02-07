from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler

def start(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text="Hola! Soy un bot de Charlas de Software!"
    )


def main():
    updater = Updater(token='<token va acá>', use_context=True)
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    updater.start_polling()

if __name__ == '__main__':
    main()