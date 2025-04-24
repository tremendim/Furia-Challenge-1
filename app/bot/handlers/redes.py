from telegram import Update
from telegram.ext import ContextTypes

async def redes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensagem = (
        "🔥 Redes sociais oficiais da FURIA:\n\n"
        "🐦 Twitter: https://twitter.com/FURIA\n"
        "📸 Instagram: https://instagram.com/furiagg\n"
        "📘 Facebook: https://facebook.com/furiagg\n"
        "🎥 YouTube: https://youtube.com/FURIA\n"
        "🟣 Twitch: https://www.twitch.tv/furiatv\n"
        "🌐 Site: https://www.furia.gg/\n"
    )
    await update.message.reply_text(mensagem)
