import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from app.bot.handlers.redes import redes  # Importa o handler de redes
from app.bot.handlers.streamers import streamers  # Importa o handler de redes
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bem-vindo ao Bot da FURIA! 🔥")

async def start_bot():
    print("Bot do Telegram iniciado...")

    app = ApplicationBuilder().token(TOKEN).build()

    # Adiciona os handlers para os comandos
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("redes", redes))  
    app.add_handler(CommandHandler("streamers", streamers))  


    await app.initialize()
    await app.start()
    await app.updater.start_polling()
