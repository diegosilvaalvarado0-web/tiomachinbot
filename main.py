from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# TOKEN desde variables de entorno
TOKEN = os.getenv("TOKEN")

# Servidor web para Render
app_web = Flask(__name__)

@app_web.route("/")
def home():
    return "Bot activo ✅"

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    mensaje = (
        "✨ 🔥*GRUPO VIP*🔥 ✨\n\n"
        "Desbloquea +1,000 videos exclusivos 🔥\n\n"
        "Tenemos grupo de respaldo para que nunca pierdas tu acceso 🔑\n\n"
        "🇵🇪 PERÚ:\n\n"
        "S/25 YAPE 💜\n\n"
        "🌍 INTERNACIONAL:\n\n"
        "$10 PAYPAL 🤍\n\n"
        "👉 Envíame un mensaje a @TioMachin y te paso los datos para el pago al instante."
    )

    video = open("IMG_2638.mp4", "rb")

    await update.message.reply_video(
        video=video,
        caption=mensaje
    )

# Ejecutar servidor web
def run_web():
    port = int(os.environ.get("PORT", 10000))
    app_web.run(host="0.0.0.0", port=port)

# Ejecutar bot
def run_bot():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot encendido ✅")

    app.run_polling()

# Ejecutar ambos al mismo tiempo
Thread(target=run_bot).start()

run_web()