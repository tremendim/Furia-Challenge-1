import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bem-vindo ao Bot da FURIA! 🔥")

async def start_bot():
    print("Bot do Telegram iniciado...")

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("redes", redes))

    await app.initialize()
    await app.start()
    await app.updater.start_polling()

async def redes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensagem = (
        "🔥 Redes sociais oficiais da FURIA:\n\n"
        "🐦 Twitter: https://twitter.com/FURIA\n"
        "📸 Instagram: https://instagram.com/furiagg\n"
        "📘 Facebook: https://facebook.com/furiagg\n"
        "🎥 YouTube: https://youtube.com/FURIA\n"
        "🟣 Twitch: https://twitch.tv/furiagg\n"
        "🌐 Site: https://www.furia.gg/\n"
    )
    await update.message.reply_text(mensagem)