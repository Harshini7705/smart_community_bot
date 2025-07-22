from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Store important messages in a dictionary
stored_messages = {
    "MEETING": [],
    "EVENT": [],
    "MAINTENANCE": [],
    "GENERAL": []
}

# Function to classify and store messages
def classify_and_store(message_text):
    text_lower = message_text.lower()
    if "meeting" in text_lower:
        category = "MEETING"
    elif "event" in text_lower or "festival" in text_lower or "celebration" in text_lower:
        category = "EVENT"
    elif "maintenance" in text_lower:
        category = "MAINTENANCE"
    else:
        category = "GENERAL"

    stored_messages[category].append(message_text)
    return category

# Message handler for new messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text.endswith("?"):
        await answer_query(update, text)
    else:
        category = classify_and_store(text)
        if category == "GENERAL":
            await update.message.reply_text(f"✅ Message stored under category: {category}.")
        else:
            await update.message.reply_text(
                f"✅ Message stored under category: {category}.\n📌 Highlighted as important!"
            )

# Function to answer questions
async def answer_query(update: Update, question):
    question_lower = question.lower()

    if "meeting" in question_lower:
        if stored_messages["MEETING"]:
            last_message = stored_messages["MEETING"][-1]
            await update.message.reply_text(f"🗓 Latest meeting info: {last_message}")
        else:
            await update.message.reply_text("No meeting information available.")
    elif "event" in question_lower or "festival" in question_lower or "celebration" in question_lower:
        if stored_messages["EVENT"]:
            last_message = stored_messages["EVENT"][-1]
            await update.message.reply_text(f"🎉 Latest event info: {last_message}")
        else:
            await update.message.reply_text("No event information available.")
    elif "maintenance" in question_lower:
        if stored_messages["MAINTENANCE"]:
            last_message = stored_messages["MAINTENANCE"][-1]
            await update.message.reply_text(f"🛠 Latest maintenance info: {last_message}")
        else:
            await update.message.reply_text("No maintenance information available.")
    else:
        if stored_messages["GENERAL"]:
            last_message = stored_messages["GENERAL"][-1]
            await update.message.reply_text(f"ℹ Latest general info: {last_message}")
        else:
            await update.message.reply_text("I don't have information on that topic yet.")

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello! I am your smart community bot.\n\n"
        "✅ Send any important announcements, and I will automatically highlight & store them.\n"
        "❓ Ask me questions like 'When is the meeting?' or 'When is the festival?' and I'll reply with the latest info."
    )

# Main function to run the bot
def main():
    bot_token = "REPLACE_WITH_YOUR_BOT_TOKEN"

    app = ApplicationBuilder().token(bot_token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()