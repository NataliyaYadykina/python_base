from datetime import datetime
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters, CallbackContext

TOKEN = 'token'

bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

def start(update:Update, context:CallbackContext):
    context.bot.send_message(update.effective_chat.id, f'''Привет, {update.effective_user.first_name}! ✌️

👨‍🎓 Я бот-математик и могу решать примеры с рациональными числами.

Выбери действие:

🧮 Решить пример - /do
📝 Смотреть журнал - /history
📚 Читать справку - /faq''')

def history(update:Update, context:CallbackContext):
    history = view_history(update.effective_user.id, 'hw10_tg_bot_math_log.csv')
    context.bot.send_message(update.effective_chat.id, history)
    context.bot.send_message(update.effective_chat.id, 'Решать примеры - /do\nВ главное меню - /start')

def faq(update:Update, context:CallbackContext):
    context.bot.send_message(update.effective_chat.id, '''СПРАВКА

- бот работает только с рациональными числами
- бот не умеет обрабатывать скобки
- для корректной работы в примере необходимо ставить пробелы между числами и знаками-операторами
- если, например, число отрицательное, то между числом и его знаком "минус" пробел ставить не нужно. Иначе бот обработает пример неверно.

Решать примеры - /do
В главное меню - /start''')

def do_start(update:Update, context:CallbackContext):
    context.bot.send_message(update.effective_chat.id, '''Пришли в чат пример, разделяя числа и знаки пробелами.\nНЕ используй скобки.
Если число отрицательное, не ставь пробел между числом и его знаком "минус".''')

def do(update:Update, context:CallbackContext):
    example = update.message.text
    example_lst = example.split()
    result = procces(example_lst)
    context.bot.send_message(update.effective_chat.id, f'{example} = {round(float(result[0]), 2)}')
    log(update.effective_user.id, example, round(result[0], 2), 'hw10_tg_bot_math_log.csv')

def cancel(update:Update, context:CallbackContext):
    context.bot.send_message(update.effective_chat.id, '❗️ Что-то пошло не так.')

def procces(lst):
    while '/' in lst:
        ind = lst.index('/')
        res = float(lst[ind - 1]) / float(lst[ind + 1])
        del lst[(ind - 1) : (ind + 2)]
        lst.insert(ind - 1, res)

    while '*' in lst:
        ind = lst.index('*')
        res = float(lst[ind - 1]) * float(lst[ind + 1])
        del lst[(ind - 1) : (ind + 2)]
        lst.insert(ind - 1, res)

    while '-' in lst:
        ind = lst.index('-')
        res = float(lst[ind - 1]) - float(lst[ind + 1])
        del lst[(ind - 1) : (ind + 2)]
        lst.insert(ind - 1, res)

    while '+' in lst:
        ind = lst.index('+')
        res = float(lst[ind - 1]) + float(lst[ind + 1])
        del lst[(ind - 1) : (ind + 2)]
        lst.insert(ind - 1, res)
    
    return lst

def log(user, example, result, file_path):
    time = datetime.now()
    with open(file_path, 'a', encoding = 'utf-8') as f:
        f.write(f'{time}; {user}; {example}; {result}\n')
    return

def view_history(user, file_path):
    user_history = []
    str_history = ''
    with open (file_path, 'r', encoding = 'utf-8') as f:
        for line in f:
            if str(user) in line:
                user_history.append(line)
    if user_history:
        for i in range(len(user_history)):
            user_history[i] = user_history[i].split(';')
            str_history += user_history[i][2][1:] + ' =' + user_history[i][3]
        str_history += '\n'
    return str_history

start_handler = CommandHandler('start', start)
history_handler = CommandHandler('history', history)
faq_handler = CommandHandler('faq', faq)
do_start_handler = CommandHandler('do', do_start)
do_handler = MessageHandler(Filters.text, do)

cancel_handler = CommandHandler('cancel', cancel)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(history_handler)
dispatcher.add_handler(faq_handler)
dispatcher.add_handler(do_start_handler)
dispatcher.add_handler(do_handler)

updater.start_polling() # start
updater.idle() # end
