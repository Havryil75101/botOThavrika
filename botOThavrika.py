import telebot
import random
from telebot.types import ReactionTypeEmoji
import os
    
# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("7362622496:AAFPLnpflxXrq1AGhk1RQlieGAnDJDVGvRQ")

@bot.message_handler(commands=['photo'])
def send_img(message):
    with open('images/pis.jpg,', 'rb') as f:
        bot.send_photo(message.chat.id, f, 'piu piu')

@bot.message_handler(commands=['help'])
def send_hello(message):
    bot.reply_to(message, "Тут есть куча команд(/help, /start, /hello, /bye, /game, /photo, /mem)")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь, ты можеш написать /help если нужна помощь!")
    bot.send_message(message.chat.id, 'Привет! Я твой Telegram бот. Напиши что-нибудь!')
    

@bot.message_handler(commands=['mem'])
def send_mem(message):
    img = random.choice(os.listdir('images'))
    with open(f'images/{img}', 'rb') as f:
        bot.send_photo(message.chat.id, f)


@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")
    
@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['game'])
def send_game(message):
    msg = bot.send_dice(message.chat.id, '🎯')
    if msg.dice.value > 4:
        bot.send_message(message.chat.id, 'Ты выиграл!')
    else:
        bot.send_message(message.chat.id, 'Ты проиграл!')
    
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if 'привет' in message.text:
        emo = ["❤", "👍"]
        bot.set_message_reaction(message.chat.id, message.id, [ReactionTypeEmoji(random.choice(emo))], is_big=False)
    bot.reply_to(message, message.text)
    
bot.polling()
