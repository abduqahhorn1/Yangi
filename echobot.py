from telegram.ext import Updater, MessageHandler, Filters

def echo(update, context):
    # Foydalanuvchidan kelgan xabarni olish
    message = update.message
    text = message.text

    # Foydalanuvchiga xabarni tiklash
    message.reply_text(text)

def main():
    # Telegram bot tokeningizni quyidagi o'zgaruvchiga saqlang
    token = '6608318606:AAENjISuyYo4jOn-cd7bfe4ORQbFH5O-85s'

    # Updater yaratish
    updater = Updater(token, use_context=True)

    # MessageHandler qo'shish
    dispatcher = updater.dispatcher
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)

    # Botni ishga tushirish
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
