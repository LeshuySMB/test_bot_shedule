import telebot
from server import print_shedule as print_shedule

bot = telebot.TeleBot("5696685310:AAGJ7lvgINmkRW0qyB5IgOBMdxChDkt2ZKY")

@bot.message_handler(commands='start')
def shedule(message):
    text_mess = message.text.split()
    text_mess.pop(0)
    print(text_mess)

    mess = print_shedule(text_mess[0], text_mess[1], text_mess[2])
    bot.send_message(message.chat.id, mess)

bot.polling(non_stop=True)