import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.getenv("7799612638:AAHcflKUbrzpwRPUcg1RMVradG8EeRfX5cE")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hi! I am your chatbot 🤖. Type anything!")

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text.lower()

    if "hello" in user_message:
        await update.message.reply_text("Hey there!")
    elif "bye" in user_message:
        await update.message.reply_text("Goodbye! Take care.")
    else:
        await update.message.reply_text("I didn't understand that.")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), reply))

    app.run_polling()

if __name__ == "__main__":
    main()
