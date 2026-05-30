from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8845810807:AAGaIFGBRC2RBS6-Rnb-Fkuws0mK2zGJdKM"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    mensaje = (
       "✨ 🔥*GRUPO VIP*🔥 ✨\n\n"
        "Desbloquea +1,000 videos exclusivos 🔥\n\n"
        "🇵🇪 PERÚ: S/25\n"
        " 💜 Yape | 📲 Plin\n\n"
        "🌍 INTERNACIONAL: $ 10\n"
        "🅿️ PayPal | 💳 Visa | ❤️ Mastercard | 🟡 Binance Pay\n\n"
        "👉 Envíame un mensaje a @TioMachin y al instante te paso los datos para el pago.\n\n"
        "Unete al grupo gratuito https://t.me/+Csuc5Yv8puI0YzAx"
    )

    video = open("IMG_2638.mp4", "rb")

    await update.message.reply_video(
        video=video,
        caption=mensaje,
        parse_mode="Markdown"
    )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Bot encendido...")
app.run_polling()