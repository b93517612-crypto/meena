import os
from flask import Flask, request, abort
from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler

BOT_TOKEN = os.environ.get("BOT_TOKEN")
WEBHOOK_PATH = "/webhook"   # endpoint path
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN environment variable required")

app = Flask(__name__)
bot = Bot(token=BOT_TOKEN)

# Create dispatcher for handling updates (no persistence)
dispatcher = Dispatcher(bot=bot, update_queue=None, workers=0, use_context=False)

# Example command handler
def start(update: Update, context):
    chat_id = update.effective_chat.id
    bot.send_message(chat_id=chat_id, text="Namaste! Main Render se chalne wala bot hoon 😊")

dispatcher.add_handler(CommandHandler("start", start))

@app.route("/")
def index():
    return "Telegram Render Bot is running."

@app.route(WEBHOOK_PATH, methods=["POST"])
def webhook():
    if request.method == "POST":
        try:
            json_data = request.get_json(force=True)
            update = Update.de_json(json_data, bot)
            dispatcher.process_update(update)
        except Exception as e:
            # log error in real app
            print("Webhook error:", e)
            abort(400)
        return "OK"
    else:
        abort(405)

# Optional: helper to set webhook on startup if you prefer
if __name__ == "__main__":
    app.run()
