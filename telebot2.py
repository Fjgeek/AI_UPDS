import telebot
bot = telebot.TeleBot('78788270565:AAHH0zQVcJTjdTTlNLcbpY7OHRMCY25IrvA')

@bot.message_handler(commands=['encender','start'])
def send_welcome(message):
	bot.reply_to(message,"""\
¿Eres el elegido para hacerme mas inteligente?
DI TU NOMBRE O NO PASARAS
""")
@bot.message_handler(func=lambda message: True)
def fucn(message):
    if(message.text=='erick'):
        bot.reply_to(message,"Bienvenido erick")
        bot.reply_to(message,"Crea en mi un arbol de decision")
    elif(message.text=='ismael'):
        bot.reply_to(message,"Bienvenido ismael")
        bot.reply_to(message,"Crea en mi un arbol de decision")
    elif(message.text=='kennet'):
        bot.reply_to(message,"Bienvenido kennet")
        bot.reply_to(message,"Crea en mi un arbol de decision")
    elif(message.text=='enrique'):
        bot.reply_to(message,"Bienvenido enrique")
        bot.reply_to(message,"Crea en mi un arbol de decision")
    elif(message.text=='fjgeek'):
        bot.reply_to(message,"AMO HAGAME MAS INTELIGENTE")
        bot.reply_to(message,"Nadie lo ha hecho")
    else:
        bot.send_message(message,"¿QUIEN ERES Y QUE HACES AQUI?")
    pass


bot.polling()