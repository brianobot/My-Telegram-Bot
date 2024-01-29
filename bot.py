import environ
import telebot

env = environ.Env()
environ.Env.read_env()

API_TOKEN = env("API_TOKEN")

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=["start", "hello"])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
