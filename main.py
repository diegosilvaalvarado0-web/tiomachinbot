from flask import Flask
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes
)
import threading
import asyncio
import os

TOKEN = ("8845810807:AAGaIFGBRC2RBS6-Rnb-Fkuws0mK2zGJdKM")

# Flask
app_web = Flask(__name__)

@app_web.route("/")
def home():
    return "Bot activo ✅"

# Telegram
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    mensaje = (
        "✨ 🔥*GRUPO VIP*🔥 ✨\n\n"
        "Desbloquea +1,000 videos exclusivos 🔥\n\n"
        "Tenemos grupo de respaldo para que nunca pierdas tu acceso 🔑\n\n"
        "🇵🇪 PERÚ: S/25 YAPE\n"
        " 💜 Yape | 📲 Plin\n\n"
        "🌍 INTERNACIONAL: $ 10\n"
        "🅿️ PayPal | 💳 Visa | ❤️ Mastercard | 🟡 Binance Pay\n\n"
        "👉 Envíame un mensaje a @TioMachin y te paso los datos para el pago al instante.\n"
        "Unete al grupo gratuito https://t.me/+Csuc5Yv8puI0YzAx"
    )

    video = open("IMG_2638.mp4", "rb")

    await update.message.reply_video(
        video=video,
        caption=mensaje
    )

async def run_bot():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot encendido ✅")

    await app.initialize()
    await app.start()
    await app.updater.start_polling()

# Ejecutar bot
def start_bot():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(run_bot())
    loop.run_forever()

# Hilo del bot
threading.Thread(target=start_bot).start()

# Flask
port = int(os.environ.get("PORT", 10000))
app_web.run(host="0.0.0.0", port=port)