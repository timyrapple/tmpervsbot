import telebot
from telebot import types
TOKEN = "5168479325:AAGQnmPwTDl-33ZLO0JOEOHMWYjivVoPTJw"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def strat(message):
    markup = types.ReplyKeyboardMarkup
    item1 = types.KeyboardButton("Отзывы 📑")
    item2 = types.KeyboardButton("Реклама 🎞")
    item3 = types.KeyboardButton("Вход в приват чат 👨🏽‍💻")

    markup.add(item1, item2, item3)

    bot.send_messege(messege.chat.id, "Привет, {0.first_name}". format(message.from_user), reply_markup - markup)

bot.polling(none_stop = True)   