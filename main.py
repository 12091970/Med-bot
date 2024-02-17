import telebot

from random import *
import json
import requests
spisok = []
API_URL = 'https://7012.deeppavlov.ai/model'


API_TOKEN = 
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):

    spisok.append('Сердечно-сосудистые заболеввания')
    spisok.append('Диабет')
    spisok.append('Бронхиальная астма')
    bot.send_message(message.chat.id,'Привет,список хроническиx заболеваний -жми /all,\
                                     более подробная информация -жми /wiki плюс вопрос, просто \
                                     пообщаться -жми /text плюс вопрос')

@bot.message_handler(commands=['all'])
def show_all(message):
    try:
        bot.send_message(message.chat.id,'Вот список:')
        bot.send_message(message.chat.id,", ".join(spisok))
    except:
        bot.send_message(message.chat.id,'Что-то пошло не так!')

@bot.message_handler(commands=['save'])
def save_all(message):
    with open("spisok.json","w",encoding="utf-8") as fh:
        fh.write(json.dumps(spisok,ensure_ascii=False))
    bot.send_message(message.chat.id,'Информация была сохранена в файле spisok.json')


@bot.message_handler(commands=['wiki'])
def wiki(message):
    quest = message.text.split()[1:]
    qq = " ".join(quest)
    data = {'question_raw': [qq]}
    try:
        res = requests.post(API_URL,json=data,verify=False).json()
        bot.send_message(message.chat.id,res)
    except:
        bot.send_message(message.chat.id,'Что-то я ничего не нашла...')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if"дела"in message.text.lower():
      bot.send_message(message.chat.id,'Дела хороши, а как у тебя?')
    elif "отлично" or "хорошо" in message.text.lower():
      bot.send_message(message.chat.id, 'Нам везёт!')




bot.polling()

