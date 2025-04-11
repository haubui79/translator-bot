import logging
from deep_translator import GoogleTranslator
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# Thay bằng token bot của bạn
BOT_TOKEN = "8153189108:AAG7uq1uacGZRdFwELcybBj6lfdKaFbhzfo"

# Cấu hình logging (tùy chọn)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Hàm xử lý tin nhắn
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    original_text = update.message.text
    try:
        # Dịch tự động: nếu là tiếng Việt → dịch sang Anh, ngược lại thì dịch sang Việt
        translated = GoogleTranslator(source='auto', target='en').translate(original_text)
        if translated.lower() == original_text.lower():
            translated = GoogleTranslator(source='auto', target='vi').translate(original_text)

        await update.message.reply_text(f"🌐 Dịch:\n{translated}")
    except Exception as e:
        await update.message.reply_text("❌ Đã có lỗi xảy ra khi dịch.")

# Hàm chạy bot
def run_bot():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
