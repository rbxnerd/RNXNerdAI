import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Get token from Render environment variables
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

print("BOT STARTING...")

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! I'm your Telegram bot 🤖")

# Echo message (simple test)
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(f"You said: {text}")

def main():
    if not TOKEN:
        print("ERROR: TELEGRAM_BOT_TOKEN is missing")
        return

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("RUNNING BOT...")
    app.run_polling()

if __name__ == "__main__":
    main()
