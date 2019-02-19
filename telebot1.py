import telebot
bot = telebot.TeleBot("788270565:AAHH0zQVcJTjdTTlNLcbpY7OHRMCY25IrvA")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "¿Eres el elegido a hacerme mas inteligente?")
	bot.reply_to(message,"Solo repito todo lo que tu dices")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()