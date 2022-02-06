from concurrent.futures import Executor
import telebot
from telebot import types

TOKEN = '5270877307:AAHht1HAlNpKWao_TF4lKy3ZNxKom53r3Ms'
BOT_URL = 'git@github.com:timyrapple/tmpervsbot.git'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton("Вход в приват чат")
    item2 = types.KeyboardButton("Реклама")
    item3 = types.KeyboardButton("Отзывы")

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}!'. format(message.from_user), reply_markup = markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type =='private':
        if message.text == "Вход в приват чат":
            bot.send_message(message.chat.id, 'https://qiwi.com/n/SSTAILE' )
            bot.send_message(message.chat.id, 'Вход в приват чат = 39р (навсегда)' )
        elif message.text == "Отзывы":
           markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
           back = types.KeyboardButton ("Назад")
           markup.add(back)

           bot.send_message(message.chat.id, 'https://t.me/+yAaD73XdeFkzNWEy', reply_markup =  markup)

        elif message.text == "Реклама":
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            back = types.KeyboardButton ("Назад")
            markup.add(back)

            bot.send_message(message.chat.id, 'https://qiwi.com/n/SSTAILE', reply_markup =  markup)
            bot.send_message(message.chat.id, 'Реклама:  1 час - 49 рублей, 3 часа - 69 рублей, 5 часов - 80 рублей, 10 часов - 100 рублей, 12 часов - 159 рублей, ∞ часов - 359 рублей' , reply_markup = markup)
            bot.send_message(message.chat.id, 'После оплаты рекламы, обратитесь к админу, прайс лист на реклманое время указан в группе.', reply_markup = markup)

        elif message.text == "Назад":
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton("Вход в приват чат")
            item2 = types.KeyboardButton("Реклама")
            item3 = types.KeyboardButton("Отзывы")

            markup.add(item1, item2, item3)

            bot.send_message(message.chat.id, "Назад", reply_markup =  markup)

bot.polling(none_stop = True)
