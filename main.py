from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


TOKEN =("8944541596:AAFzXDwacuLaIbdpfzWJTr5FoF7vixnU2I0")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    # Texto
    mensaje =  (
        "✨ 🔥*GRUPO VIP*🔥 ✨\n\n"
    "Desbloquea +1,000 videos exclusivos 🔥\n\n"
    "Tenemos grupo de respaldo para que nunca pierdas tu acceso 🔑\n\n"
    "🇵🇪 PERÚ: \n\n"
    "S/25 YAPE 💜 \n\n"
    "🌍 INTERNACIONAL: \n\n"
    "$10 PAYPAL 🤍\n\n"
    "👉 Envíame un mensaje a @TioMachin y te paso los datos para el pago al instante."
    )


    # Ruta del video
    video = open("IMG_2638.mp4", "rb")

    # Enviar video con texto
    await update.message.reply_video(
        video=video,
        caption=mensaje
    )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Bot encendido...")
app.run_polling()