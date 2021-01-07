import json
import telebot

from test2 import OUT_FILENAME
from telebot import types

bot = telebot.TeleBot('token')

with open(OUT_FILENAME, 'r', encoding="utf-8") as f:
    s = json.load(f)
    link_ONEKANAL = s[38]['link']
    link_STS = s[41]['link']
    link_TNT = s[42]['link']

@bot.message_handler(content_types=['text']) 
def get_text_messages(message): 
    if message.text == "/start": 
        keyboard = types.InlineKeyboardMarkup()
        key_onekanal = types.InlineKeyboardButton(text='Первый_канал', callback_data='ONEKANAL_eng')
        keyboard.add(key_onekanal)
        key_sts = types.InlineKeyboardButton(text='СТС', callback_data='CTC_eng')
        keyboard.add(key_sts)
        key_tnt = types.InlineKeyboardButton(text='ТНТ', callback_data='TNT_eng') 
        keyboard.add(key_tnt)
        bot.send_message(message.from_user.id, text='Выберете канал', reply_markup=keyboard) 
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши /start") 
    else: 
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши для запуска /start")

@bot.callback_query_handler(func=lambda call: True) 
def callback_worker(call): 
    if call.data == "ONEKANAL_eng":
        ONE_msg = link_ONEKANAL
        bot.send_message(call.message.chat.id, ONE_msg)
    elif call.data == "CTC_eng": 
        CTC_msg = link_STS
        bot.send_message(call.message.chat.id, CTC_msg)
    elif call.data == "TNT_eng":
        TNT_msg = link_TNT
        bot.send_message(call.message.chat.id, TNT_msg)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши для запуска /start")


bot.polling(none_stop=True, interval=0)