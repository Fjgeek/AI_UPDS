from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import apiai, json
updater = Updater(token='788270565:AAHH0zQVcJTjdTTlNLcbpY7OHRMCY25IrvA') # Telegram API Token
dispatcher = updater.dispatcher
# Обработка команд
def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Hola Hablemos para probar mi AI')
def textMessage(bot, update):
    request = apiai.ApiAI('6d6c4ffc13a947ddac301ea19b32ceb4').text_request() # Dialogflow API Token
    request.lang = 'es' # Request language
    request.session_id = 'SabioDominguero_bot' # ID dialog session (for bot training)
    request.query = update.message.text # Send request to AI ИИ with the user message
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech'] # Take JSON answer
    if response:    
        bot.send_message(chat_id=update.message.chat_id, text=response)
    else:
        bot.send_message(chat_id=update.message.chat_id, text='No te entiendo, Programame')
        bot.send_message(chat_id=update.message.chat_id, text='Usa DialogFLow mas facil que TensorFLOW')
# Handlers
start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)
# Add handlers to the dispatcher
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)
# Start update search
updater.start_polling(clean=True)
# Stops the bot
updater.idle()