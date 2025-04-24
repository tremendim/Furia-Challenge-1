from telegram import Update
from telegram.ext import ContextTypes
from app.services.twitch import get_twitch_token, get_live_streamers

STREAMERS_FURIA = ['gaules', 'yuurih', 'dropfps']  # coloca aqui os reais

async def streamers(update: Update, context: ContextTypes.DEFAULT_TYPE):
    token = get_twitch_token()
    lives = get_live_streamers(STREAMERS_FURIA, token)

    if not lives:
        await update.message.reply_text("😔 Nenhum streamer da FURIA está ao vivo agora.")
        return

    mensagem = "🎮 Streamers da FURIA ao vivo agora:\n\n"
    for live in lives:
        mensagem += (
            f"🔴 [{live['user_name']}](https://twitch.tv/{live['user_login']})\n"
            f"🕹️ {live['game_name']} — {live['title']}\n\n"
        )

    await update.message.reply_text(mensagem, parse_mode="Markdown")
