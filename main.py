from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram.request import HTTPXRequest

TOKEN = "8845810807:AAG38l3EstdH8jXcCtVPJJxrvdOhUaSXmIQ"

request = HTTPXRequest(
    connect_timeout=30,
    read_timeout=60,
    write_timeout=120,
    pool_timeout=60
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    mensaje = (
        "✨ 🔥*GRUPO VIP*🔥 ✨\n\n"
        "Desbloquea +1,000 videos exclusivos 🔥\n\n"
        "🇵🇪 PERÚ: S/25\n"
        "💜 Yape | 📲 Plin\n\n"
        "🌍 INTERNACIONAL: $10\n"
        "🅿️ PayPal | 💳 Visa | ❤️ Mastercard | 🟡 Binance Pay\n\n"
        "👉 Envíame un mensaje a @TioMachin y al instante te paso los datos para el pago.\n\n"
        "Únete al grupo gratuito https://t.me/+Csuc5Yv8puI0YzAx"
    )

    try:
        with open("IMG_2638.mp4", "rb") as video:
            await update.message.reply_video(
                video=video,
                caption=mensaje,
                parse_mode="Markdown"
            )
    except Exception as e:
        print(f"ERROR: {e}")
        await update.message.reply_text(
            "Hubo un problema enviando el video."
        )

app = (
    ApplicationBuilder()
    .token(TOKEN)
    .request(request)
    .build()
)

app.add_handler(CommandHandler("start", start))

print("Bot encendido ✅")
app.run_polling()