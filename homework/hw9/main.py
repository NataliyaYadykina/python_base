from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

token1 = '6161250705:AAGuSIvSddYd0MJ9Dp-A2yNPJo1YgPE_iOE'

bot = Bot(token=token1)
updater = Updater(token=token1)
dispatcher = updater.dispatcher # brain

def start(update, context):
    context.bot.send_message(update.effective_chat.id, f'''Привет, {update.effective_user.first_name}! ✌️
Введи слова через пробел.''')

def delwords(update, context):
    new_text = ''
    text = update.message.text.split()
    if text:
        for i in text:
            if 'абв' not in i:
                new_text += i + ' '
        if new_text:
            context.bot.send_message(update.effective_chat.id, f'{new_text}')
            context.bot.send_message(update.effective_chat.id, '''Ух! Интересная задачка! 🔥
Славно я потрудился. Приходи сюда еще! 😉''')
        else:
            context.bot.send_message(update.effective_chat.id, 'Нет слов для вывода. 🤷‍♂️')

def cancel(update, contex):
    contex.bot.send_message(update.effective_chat.id, 'Что-то пошло не так.')

start_handler = CommandHandler('start', start)
delwords_handler = MessageHandler(Filters.text, delwords)

cancel_handler = CommandHandler('cancel', cancel)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(delwords_handler)

updater.start_polling() # start
updater.idle() # end
