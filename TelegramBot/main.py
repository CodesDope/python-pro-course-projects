import os
from bs_news import get_news
from telegram.ext import Updater
from telegram.ext import CommandHandler

updater = Updater(token=os.environ.get("TELEGRAM_TOKEN"))


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hi There! Here is a list of commands you should try:\n/hi - Say Hi\n/news - Get NEWS",
    )


def hi(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello!")


def news(update, context):
    news = get_news()
    news_string = "\n".join(news)
    context.bot.send_message(chat_id=update.effective_chat.id, text=news_string)


dispatcher = updater.dispatcher

start_handler = CommandHandler("start", start)
hi_handler = CommandHandler("hi", hi)
news_handler = CommandHandler("news", news)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(hi_handler)
dispatcher.add_handler(news_handler)
updater.start_polling()
