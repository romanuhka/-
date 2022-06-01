import random
from random import choice
import telebot
from telebot import types
from config import bot
import bs4
import requests
import math

value = ''
old_value = ''

#------------------------------------------------------------------------------------------------------------------------
keyboard1 = telebot.types.InlineKeyboardMarkup()
keyboard1.row(telebot.types.InlineKeyboardButton(' ', callback_data='no'),
            telebot.types.InlineKeyboardButton('C', callback_data='C'),
            telebot.types.InlineKeyboardButton('<=', callback_data='<='),
            telebot.types.InlineKeyboardButton('/', callback_data='/'),
            telebot.types.InlineKeyboardButton('^2', callback_data='**'))

keyboard1.row(telebot.types.InlineKeyboardButton('7', callback_data='7'),
            telebot.types.InlineKeyboardButton('8', callback_data='8'),
            telebot.types.InlineKeyboardButton('9', callback_data='9'),
            telebot.types.InlineKeyboardButton('*', callback_data='*'),
            telebot.types.InlineKeyboardButton('(', callback_data='('))

keyboard1.row(telebot.types.InlineKeyboardButton('4', callback_data='4'),
            telebot.types.InlineKeyboardButton('5', callback_data='5'),
            telebot.types.InlineKeyboardButton('6', callback_data='6'),
            telebot.types.InlineKeyboardButton('-', callback_data='-'),
            telebot.types.InlineKeyboardButton(')', callback_data=')'))

keyboard1.row(telebot.types.InlineKeyboardButton('1', callback_data='1'),
            telebot.types.InlineKeyboardButton('2', callback_data='2'),
            telebot.types.InlineKeyboardButton('3', callback_data='3'),
            telebot.types.InlineKeyboardButton('+', callback_data='+'),
            telebot.types.InlineKeyboardButton('%', callback_data='/100'))

keyboard1.row(telebot.types.InlineKeyboardButton('00', callback_data='00'),
            telebot.types.InlineKeyboardButton('0', callback_data='0'),
            telebot.types.InlineKeyboardButton(',', callback_data='.'),
            telebot.types.InlineKeyboardButton('=', callback_data='='),
            telebot.types.InlineKeyboardButton('π', callback_data='*3,14'))


#------------------------------------------------------------------------------------------------------------------------
@bot.message_handler(commands=["start"])

def start(message):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Главное меню")
    markup.add(btn1)

    bot.send_message(chat_id,
                     text="Привет, {0.first_name}! Я бот Марины Романюк".format(
                         message.from_user), reply_markup=markup)


#------------------------------------------------------------------------------------------------------------------------
@bot.message_handler(content_types=['text'])
def play_message(message):
    chat_id = message.chat.id
    ms_text = message.text

    if ms_text == "Главное меню" or ms_text == "👋 Главное меню" or ms_text == "Вернуться в главное меню":  # ..........
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Развлечения")
        btn3 = types.KeyboardButton("Приложения")
        back = types.KeyboardButton("Помощь")
        markup.add(btn1, btn3, back)
        bot.send_message(chat_id, text="Вы в главном меню", reply_markup=markup)


    elif ms_text == "Развлечения" or ms_text == "Вернуться в Развлечения":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Котяха')
        btn2 = types.KeyboardButton("Прислать анекдот")
        btn3 = types.KeyboardButton("Игра")
        btn4 = types.KeyboardButton("Создать ник")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, btn4, back)
        bot.send_message(chat_id, text="Развлечения", reply_markup=markup)


    elif ms_text == "Игра" or ms_text == "Вернуться в игры":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Камень, ножницы, бумага")
        btn3 = types.KeyboardButton("Вернуться в Развлечения")
        markup.add(btn1, btn3)
        bot.send_message(chat_id, text="Игра", reply_markup=markup)

    elif ms_text == "Камень, ножницы, бумага":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Камень")
        btn2 = types.KeyboardButton("Ножницы")
        btn3 = types.KeyboardButton("Бумага")
        btn4 = types.KeyboardButton("Старт")
        back = types.KeyboardButton("Вернуться в игры")
        markup.add(btn1, btn2, btn3, btn4, back)
        bot.send_message(chat_id, text="Камень, ножницы, бумага", reply_markup=markup)



    elif message.text == "Создать ник":
        bot.send_message(message.chat.id, text=get_nickname())


    elif ms_text == 'Приложения':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Калькулятор")
        btn2 = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2)
        bot.send_message(chat_id, text="Приложения", reply_markup=markup)


    elif ms_text == "Калькулятор":
        global value
        if value == '':
            bot.send_message(message.from_user.id, '0', reply_markup=keyboard1)
        else:
            bot.send_message(message.from_user.id, value, reply_markup=keyboard1)


    elif ms_text == "Помощь" or ms_text == "/help":
        bot.send_message(chat_id, "Автор: Marina Romanuk")
        key1 = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="Страница автора", url="https://t.me/romanuhka")
        key1.add(btn1)
        img = open('cemarina.jpg', 'rb')
        bot.send_photo(message.chat.id, img, reply_markup=key1)


    elif ms_text == "Старт":
        bot.register_next_step_handler(message, reggame)
    elif message.text == "Прислать анекдот":
        bot.send_message(message.chat.id, text=get_anekdot())
    elif ms_text == "Котяха":

        IGM = ['100', '101', '102', '200', '201', '202', '203', '204', '206', '207', '300', '301', '302', '303', '304', '305', '307', '308', '400', '401', '402', '403', '404', '405', '406', '407', '408', '409', '410', '411', '412', '413', '414', '415', '416', '417', '418', '420', '421', '422', '423', '424', '425', '426', '429', '431', '444', '450', '451', '498', '499', '500', '501', '502', '503', '504', '506', '507', '508', '509', '510', '511', '521', '522', '523', '525', '599']
        IGM5 = choice(IGM)
        IGM2 = 'images-original/'+IGM5+'.jpg'
        IGM1 = open(IGM2, 'rb')
        bot.send_photo(chat_id, IGM1)

    #elif ms_text == "Лисичка":
    #elif message.text == "Показать лисичку":
          #contents = requests.get('https://randomfox.ca/floof').json()
          #urlCAT = contents['image']
          #bot.send_photo(message.chat.id, photo=urlCAT)
#------------------------------------------------------------------------------------------------------------------------
@bot.callback_query_handler(func=lambda call: True)
def calllback_fun(query):
    global value, old_value
    data = query.data

    if data == 'no':
        pass
    elif data == 'C':
        value = ''
    elif data == '<=':
        value = value[:-1]
    elif data == '=':
        try:
            value = str(eval(value))
        except:
            value ='Ошибка!'
    else:
        value += data

    if (value != old_value and value != '') or ('0' != old_value and value != ''):
        if value == '':
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text='0', reply_markup=keyboard1)
            old_value = '0'
        else:
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text=value, reply_markup=keyboard1)

        old_value = value
        if value == 'Ошибка!': value = ''
#------------------------------------------------------------------------------------------------------------------------
@bot.callback_query_handler(func=lambda call: True)
def get_anekdot():
    array_anekdots = []
    req_anek = requests.get('http://anekdotme.ru/random')
    soup = bs4.BeautifulSoup(req_anek.text, "html.parser")
    result_find = soup.select('.anekdot_text')
    for result in result_find:
        array_anekdots.append(result.getText().strip())
    return array_anekdots[0]
#------------------------------------------------------------------------------------------------------------------------
@bot.callback_query_handler(func=lambda call: True)
def reggame(message):
    option = ['Камень', 'Ножницы', 'Бумага']
    global game
    global value
    value = random.choice(option)
    game = message.text
    if game == 'Камень':
        if value == 'Камень':
            bot.send_message(message.chat.id, 'Ничья')
        if value == 'Ножницы':
            bot.send_message(message.chat.id, 'Вы победили, я поставил ножницы')
        if value == 'Бумага':
            bot.send_message(message.chat.id, 'Вы проиграли , я поставил бумагу')
    if game == 'Ножницы':
        if value == 'Камень':
            bot.send_message(message.chat.id, 'Вы проиграли , я поставил камень')
        if value == 'Ножницы':
            bot.send_message(message.chat.id, 'Ничья')
        if value == 'Бумага':
            bot.send_message(message.chat.id, 'Вы выиграли , я поставил бумагу')
    if game == 'Бумага':
        if value == 'Камень':
            bot.send_message(message.chat.id, 'Вы выиграли , я поставил камень')
        if value == 'Ножницы':
            bot.send_message(message.chat.id, 'Вы проиграли , я поставил ножницы')
        if value == 'Бумага':
            bot.send_message(message.chat.id, 'Ничья')

def get_nickname():
    array_names = []
    req_names = requests.get("https://ru.nickfinder.com")
    soup = bs4.BeautifulSoup(req_names.text, "html.parser")
    result_find = soup.findAll(class_='one_generated_variant vt_df_bg')
    for result in result_find:
        array_names.append(result.getText())
    return array_names[0]


#------------------------------------------------------------------------------------------------------------------------
bot.polling(none_stop=True, interval=0)

print()
