import json
import telebot
import datetime
from test2 import parse
from telebot import types

bot = telebot.TeleBot(token = '')

@bot.message_handler(content_types=['text']) 
def get_text_messages(message):
    if message.text == "/start": 
        keyboard = types.InlineKeyboardMarkup()
        key_onekanal = types.InlineKeyboardButton(text='Первый канал', callback_data='ONEKANAL_eng')
        keyboard.add(key_onekanal)
        key_rusone = types.InlineKeyboardButton(text='Россия 1', callback_data='RUSONE_eng')
        keyboard.add(key_rusone)
        key_match = types.InlineKeyboardButton(text='Матч!', callback_data='Match_eng')
        keyboard.add(key_match)
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
        ONE_msg = parse()[0]['link']
        bot.send_message(call.message.chat.id, ONE_msg)
    elif call.data == "RUSONE_eng": 
        RUS1_msg = parse()[1]['link']
        bot.send_message(call.message.chat.id, RUS1_msg)
    elif call.data == "Match_eng": 
        Match_msg = parse()[17]['link']
        bot.send_message(call.message.chat.id, Match_msg)
    elif call.data == "NTV_eng": 
        NTV_msg = parse()[2]['link']
        bot.send_message(call.message.chat.id, NTV_msg)
    elif call.data == "REN_eng": 
        REN_msg = parse()[6]['link']
        bot.send_message(call.message.chat.id, REN_msg)
    elif call.data == "CTC_eng": 
        CTC_msg = parse()[3]['link']
        bot.send_message(call.message.chat.id, CTC_msg)
    elif call.data == "TV3_eng": 
        TV3_msg = parse()[13]['link']
        bot.send_message(call.message.chat.id, TV3_msg)
    elif call.data == "FRIDAY_eng": 
        FRIDAY_msg = parse()[20]['link']
        bot.send_message(call.message.chat.id, FRIDAY_msg)
    elif call.data == "TNT_eng":
        TNT_msg = parse()[4]['link']
        bot.send_message(call.message.chat.id, TNT_msg)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши для запуска /start")


if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)