import json
import telebot

from test2 import OUT_FILENAME
from telebot import types
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

with open(OUT_FILENAME, 'r', encoding="utf-8") as f:
    s = json.load(f)
    link_ONEKANAL = s[38]['link']
    link_RUSONE = s[39]['link']
    link_NTV = s[40]['link']
    link_RENTV = s[43]['link']
    link_STS = s[41]['link']
    link_TV3 = s[46]['link']
    link_FRIDAY = s[47]['link']
    link_TNT = s[42]['link']

@bot.message_handler(content_types=['text']) 
def get_text_messages(message): 
    if message.text == "/start": 
        keyboard = types.InlineKeyboardMarkup()
        key_onekanal = types.InlineKeyboardButton(text='Первый канал', callback_data='ONEKANAL_eng')
        keyboard.add(key_onekanal)
        key_rusone = types.InlineKeyboardButton(text='Россия 1', callback_data='RUSONE_eng')
        keyboard.add(key_rusone)
        key_ntv = types.InlineKeyboardButton(text='НТВ', callback_data='NTV_eng')
        keyboard.add(key_ntv)
        key_rentv = types.InlineKeyboardButton(text='РЕН ТВ', callback_data='REN_eng')
        keyboard.add(key_rentv)
        key_sts = types.InlineKeyboardButton(text='СТС', callback_data='CTC_eng')
        keyboard.add(key_sts)
        key_tv3 = types.InlineKeyboardButton(text='ТВ 3', callback_data='TV3_eng')
        keyboard.add(key_tv3)
        key_friday = types.InlineKeyboardButton(text='Пятница', callback_data='FRIDAY_eng')
        keyboard.add(key_friday)
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
    elif call.data == "RUSONE_eng": 
        RUS1_msg = link_RUSONE
        bot.send_message(call.message.chat.id, RUS1_msg)
    elif call.data == "NTV_eng": 
        NTV_msg = link_NTV
        bot.send_message(call.message.chat.id, NTV_msg)
    elif call.data == "REN_eng": 
        REN_msg = link_RENTV
        bot.send_message(call.message.chat.id, REN_msg)
    elif call.data == "CTC_eng": 
        CTC_msg = link_STS
        bot.send_message(call.message.chat.id, CTC_msg)
    elif call.data == "TV3_eng": 
        TV3_msg = link_TV3
        bot.send_message(call.message.chat.id, TV3_msg)
    elif call.data == "FRIDAY_eng": 
        FRIDAY_msg = link_FRIDAY
        bot.send_message(call.message.chat.id, FRIDAY_msg)
    elif call.data == "TNT_eng":
        TNT_msg = link_TNT
        bot.send_message(call.message.chat.id, TNT_msg)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши для запуска /start")


bot.polling(none_stop=True, interval=0)