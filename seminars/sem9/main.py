from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from random import randint

token1 = '5839031956:AAFEyovdrzM_46yGJfFh8w62_Y1u2SQPwl0'

A = 0
B = 1

bot = Bot(token='5839031956:AAFEyovdrzM_46yGJfFh8w62_Y1u2SQPwl0')
updater = Updater(token=token1)
dispatcher = updater.dispatcher # brain

def start(update, contex):
    contex.bot.send_message(update.effective_chat.id, 'Привет! \nКак дела?')
    return A

def howareyou(update, contex):
    text = update.message.text
    if 'хор' in text.lower():
        contex.bot.send_message(update.effective_chat.id, 'Я рад! ;)')
    else:
        contex.bot.send_message(update.effective_chat.id, 'Не грусти.')
    contex.bot.send_message(update.effective_chat.id, 'Как у тебя погода?')
    return B

def weather(update, contex):
    text = update.message.text
    contex.bot.send_message(update.effective_chat.id, 'У меня такая же погода.')
    contex.bot.send_message(update.effective_chat.id, 'Мне пора бежать.')
    return ConversationHandler.END


def cancel(update, contex):
    contex.bot.send_message(update.effective_chat.id, 'Что-то пошло не так.')
# def rand(update, contex):
#     contex.bot.send_message(update.effective_chat.id, f'{randint(1,100)}')

# def default(update, contex):
#     contex.bot.send_message(update.effective_chat.id, 'Я не знаю таких команд')

# def privet(update, contex):
#     text = update.message.text
#     if 'прив' in text.lower():
#         contex.bot.send_message(update.effective_chat.id, 'И тебе привет')
#     else:
#         contex.bot.send_message(update.effective_chat.id, 'Я не понимаю')
 
start_handler = CommandHandler('start', start)
howareyou_handler = MessageHandler(Filters.text, howareyou)
weather_handler = MessageHandler(Filters.text, weather)
cancel_handler = CommandHandler('cancel', cancel)
# random_handler = CommandHandler('random', rand)
# default_handler = MessageHandler(Filters.voice, default)
# privet_handler = MessageHandler(Filters.text, privet)
conv_handler = ConversationHandler(entry_points=[start_handler],
                                        states={A: [howareyou_handler],
                                        B:[weather_handler]},
                                        fallbacks=[cancel_handler])

dispatcher.add_handler(conv_handler)
# dispatcher.add_handler(random_handler)
# dispatcher.add_handler(default_handler)
# dispatcher.add_handler(privet_handler)

updater.start_polling() # start
updater.idle() # end

# python anywhere - бесплатный сервер для тг-бота
