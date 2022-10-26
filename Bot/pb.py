import telebot
from methods import print_shedule as print_shedule

bot = telebot.TeleBot("5696685310:AAGJ7lvgINmkRW0qyB5IgOBMdxChDkt2ZKY")

#Хендлер для вывода расписания
@bot.message_handler(commands='расписание')
def shedule(message):
    text_mess=message.text.split()
    text_mess.pop(0)

    mess = print_shedule(text_mess[0], text_mess[1])
    bot.send_message(message.chat.id, mess)

    

#@bot.message_handler(commands='сравнение')
#def compare(message):


bot.polling(non_stop=True)

