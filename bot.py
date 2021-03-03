import telebot
from telebot import types
from config import fullSchedule


TOKEN = '1601968835:AAEyW0dxRYp1SI_WuMgGk50k35u7GlKmWnk'
bot = telebot.TeleBot(TOKEN)

group_number = ''
day_week = ''

@bot.message_handler(commands=['start'])
def welcom(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAALoyWA81nQQAAFyg9s_tGIaWmWGgcbjOgACAQADsX2qEuODdIY35897HgQ')

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Помощь")
    item2 = types.KeyboardButton("Начать")

    markup.add(item1, item2)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот который поможет тебе не опаздывать на пары.".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Помощь':
        bot.send_message(message.chat.id, "Просто напиши мне свою группу и день недели")

    if message.text == 'Начать':
        bot.send_message(message.from_user.id, "Введите номер группы: ")
        bot.register_next_step_handler(message, groupnumber)


def groupnumber(message):

    global  group_number
    group_number = message.text
    bot.send_message(message.from_user.id, "Введите день недели: ")
    bot.register_next_step_handler(message, data)


def data(message):

    global  day_week
    day_week = message.text
    shed = fullSchedule(group_number.lower(), day_week.lower())
    if shed !="":
        bot.send_message(message.from_user.id, shed)
    else:
        bot.send_message(message.from_user.id, "Сегодня нет пар")



bot.polling(none_stop=True)