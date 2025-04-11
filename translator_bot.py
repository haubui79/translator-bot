from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from deep_translator import GoogleTranslator

# Hàm xử lý tin nhắn
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    # Tự động xác định ngôn ngữ
    if any(char in text for char in "ăâđêôơưáàảãạấầẩẫậéèẻẽẹíìỉĩịóòỏõọúùủũụýỳỷỹỵ"):
        # Văn bản là tiếng Việt → dịch sang tiếng Anh
        translated = GoogleTranslator(source='vi', target='en').translate(text)
    else:
        # Văn bản là tiếng Anh → dịch sang tiếng Việt
        translated = GoogleTranslator(source='en', target='vi').translate(text)

    await update.message.reply_text(translated)

# Khởi tạo bot
if __name__ == '__main__':
    app = ApplicationBuilder().token("8153189108:AAG7uq1uacGZRdFwELcybBj6lfdKaFbhzfo").build()

    # Lắng nghe tất cả tin nhắn dạng văn bản
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot đang chạy...")
    app.run_polling()
