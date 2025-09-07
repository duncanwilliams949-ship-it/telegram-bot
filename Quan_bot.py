from telegram.ext import Application, CommandHandler

async def start(update, context):
    await update.message.reply_text("Hello! Your bot is running 🚀")

def main():
    app = Application.builder().token("8467580968:AAFkdqRyAdB3iC9Py2u91PubO03bwaPi6uQ").build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
