import os
import telebot

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "🎉 Welcome!\n\n"
        "এটি আপনার Referral & Task Bot.\n\n"
        "🎯 Tasks\n"
        "👥 Referral\n"
        "💰 Balance\n"
        "💸 Withdraw"
    )

@bot.message_handler(commands=["help"])
def help_command(message):
    bot.send_message(
        message.chat.id,
        "Help Center\n\n"
        "যেকোনো সমস্যায় Admin-এর সাথে যোগাযোগ করুন।"
    )

bot.infinity_polling()
