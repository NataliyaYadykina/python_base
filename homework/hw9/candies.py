from random import randint
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters, CallbackContext

token1 = '6161250705:AAGuSIvSddYd0MJ9Dp-A2yNPJo1YgPE_iOE'

# ид чата; имя игрока; всего конфет; уровень; статус игры; чей ход; конфет у игрока; конфет у бота; число игр; число выигрышей; сумма баллов;
#       0;          1;            2;       3;           4;       5;               6;             7;         8;               9;           10;

bot = Bot(token=token1)
updater = Updater(token=token1)
dispatcher = updater.dispatcher # brain

count_candies = 150
max_take_candies = 28
file_path = 'hw9_statistic.csv'
A = 0
B = 1

# Стартуем игру с конфетами
def start(update:Update, context:CallbackContext):
    context.bot.send_message(update.effective_chat.id, f'''Привет, сладкоежка! 🍭🍭🍭
Я бот 🤖 для игры с конфетами.
Отлично, {update.effective_user.first_name}! 🔥🔥🔥
Я очень рад, что ты сыграешь со мной! 😎

Выбери уровень сложности игры или почитай правила (/rules):

1. ⭐️ Простой 
2. ⭐️⭐️ Средний
3. ⭐️⭐️⭐️ Сложный

Отправь в чат номер уровня сложности игры.''')

# Правила игры
def rules(update:Update, context:CallbackContext):
    context.bot.send_message(update.effective_chat.id, f'''ПРАВИЛА ИГРЫ:
На столе лежит {count_candies} конфет. \
Играют два игрока, делая ход друг после друга. \
Жеребьевка определяет, кто начинает игру. \
За один ход можно забрать от 1 до {max_take_candies} конфет. \
Победитель - тот, кто оставил на столе 0 конфет. \
В качестве приза он забирает все {count_candies} конфет.''')

# Определяем уровень сложности, обновляем статистику игрока, стартуем игру
def level(update:Update, context:CallbackContext):
    level = update.message.text
    state = A
    if level.isdigit():
        level = int(level)
        if level == 1:
            context.bot.send_message(update.effective_chat.id, f'''Ты выбрал уровень {level}. ⭐️
Хороший выбор, чтобы потренироваться! 🙂
Я сделаю вид, что плохо умею играть в эту игру. 🤷‍♂️''')
        elif level == 2:
            context.bot.send_message(update.effective_chat.id, f'''Ты выбрал уровень {level}. ⭐️⭐️
Супер! 👍 На этом уровне я буду тебе поддаваться. 😉 \
Но ты не расслабляйся! Иногда я буду рассчитывать свои ходы 🙃''')
        elif level == 3:
            context.bot.send_message(update.effective_chat.id, f'''Ты выбрал уровень {level}. ⭐️⭐️⭐️
WOW!!! 🔥🔥🔥 Сильное заявление! \
Имей в виду, здесь я не играю ни в какие поддавки. 🦾 \
Тебе нужно проявить смекалку и быть удачливым, чтобы победить меня 😜''')
        else:
            context.bot.send_message(update.effective_chat.id, '❌ Ошибка! Нет такого уровня.')
            state = B
    else:
        context.bot.send_message(update.effective_chat.id, '❌ Ошибка! Введены некорректные данные.')
        state = B
    if level == 1 or level == 2 or level == 3:
        data_player = []
        file_statistic = get_data(file_path)
        player_info = str(update.effective_chat.id)
        check_stat_player = check_data_player(player_info, file_statistic)
        active_player = random_start_player()
        if active_player == 1:
            context.bot.send_message(update.effective_chat.id, f'Жеребьевка: первый ход - твой. 😎\nБери конфеты! Ты можешь взять не более чем {max_take_candies} конфет(ы). Отправь в чат количество конфет.')
        if check_stat_player:
            data_player = get_data_player(player_info, file_statistic)
            data_player[3] = level
            data_player[5] = active_player
        else:
            data_player = [update.effective_chat.id, update.effective_user.first_name, count_candies, level, 1, active_player, 0, 0, 0, 0, 0]
        if active_player == 0:
            take_candies = bot_plays(level, data_player)
            data_player[2] = count_candies - take_candies
            data_player[5] = 1
            data_player[7] = int(data_player[7]) + take_candies
            context.bot.send_message(update.effective_chat.id, 'Жеребьевка: первый ход - мой. 🤖\nПоехали!!!')
            context.bot.send_message(update.effective_chat.id, f'''🤖 Я забрал {take_candies} конфет.
На столе осталось {data_player[2]} конфет(ы).
Твой ход! Ты можешь взять не более чем {max_take_candies} конфет(ы). Отправь в чат количество конфет.''')
        update_data(check_stat_player, player_info, data_player, file_path)
    return state

# Читаем файл с данными
def get_data(file_path):
    with open(file_path, 'r', encoding = 'utf-8') as f:
        text_file = f.read()
    return text_file

# Проверяем, есть ли статистика игрока в файле
def check_data_player(player_info, text_file):
    check = 0
    if player_info in text_file:
        check = 1
    return check

# Обновляем файл с данными (если игрока еще нет или если статистика уже есть и надо обновить)
def update_data(check, player_info, data, file_path):
    string_player = ''
    old_str = ''
    for i in data:
        string_player += str(i) + ';'
    string_player += '\n'
    if not check:
        with open (file_path, 'a', encoding = 'utf-8') as f:
            f.write(string_player)
    else:
        old_text_file = get_data(file_path)
        with open (file_path, 'r', encoding = 'utf-8') as f:
            for line in f:
                if player_info in line:
                    old_str = line
                    break
        new_text_file = old_text_file.replace(old_str, string_player)
        with open (file_path, 'w', encoding = 'utf-8') as f:
            f.write(new_text_file)

# Забираем данные игрока из файла для работы с ними
def get_data_player(player_info, text_file):
    data_player = []
    text_file = text_file.split(';\n')
    text_file = text_file[:-1]
    for i in text_file:
        if player_info in i:
            i = i.split(';')
            for j in i:
                data_player.append(j)
    return data_player

# Жеребьевка - кто начинает.
def random_start_player():
    active_player = randint(0, 1)
    return active_player # 0 - бот, 1 - игрок

# Ход бота
def bot_plays(level, data_player):
    # бот тупой
    if int(level) == 1:
        if int(data_player[2]) <= max_take_candies:
            take_candies = int(data_player[2])
        else:
            take_candies = randint(1, max_take_candies)
    # бот иногда умный, иногда тупой
    elif int(level) == 2:
        if int(data_player[2]) <= max_take_candies:
            take_candies = int(data_player[2])
        else:
            bot_is_smart = randint(0, 1)
            if bot_is_smart == 0:
                take_candies = randint(1, max_take_candies)
            else:
                if int(data_player[2]) % (1 + max_take_candies) != 0:
                    take_candies = int(data_player[2]) % (1 + max_take_candies)
                else:
                    take_candies = randint(1, max_take_candies)
    # бот умный
    else:
        if int(data_player[2]) <= max_take_candies:
            take_candies = int(data_player[2])
        else:
            if int(data_player[2]) % (1 + max_take_candies) != 0:
                take_candies = int(data_player[2]) % (1 + max_take_candies)
            else:
                take_candies = randint(1, max_take_candies)
    return take_candies
        

# Game
# ид чата; имя игрока; всего конфет; уровень; статус игры; чей ход; конфет у игрока; конфет у бота; число игр; число выигрышей; сумма баллов;
#       0;          1;            2;       3;           4;       5;               6;             7;         8;               9;           10;
def game(update:Update, context:CallbackContext):
    state = A
    win = 0
    error = 0
    max_take_candies1 = max_take_candies
    file_statistic = get_data('hw9_statistic.csv')
    player_info = str(update.effective_chat.id)
    check_stat_player = check_data_player(player_info, file_statistic)
    data_player = get_data_player(player_info, file_statistic)
    print(data_player)
    # играем, еще нет победителя, есть конфеты на столе
    if int(data_player[2]) > 0:
        if max_take_candies1 > int(data_player[2]):
            max_take_candies1 = int(data_player[2])
        # ход делает игрок
        take_candies = update.message.text
        if take_candies.isdigit():
            take_candies = int(take_candies)
            if 0 < take_candies < max_take_candies1 + 1:
                data_player[2] = int(data_player[2]) - take_candies
                data_player[5] = 0
                data_player[6] = int(data_player[6]) + take_candies
                context.bot.send_message(update.effective_chat.id, f'😎 Ты забрал(а) {take_candies} конфет.\nНа столе осталось {data_player[2]} конфет(ы).')
                update_data(check_stat_player, player_info, data_player, file_path)
                if data_player[2] == 0:
                    win = f'😎 {update.effective_user.first_name}'
                    context.bot.send_message(update.effective_chat.id, f'{win} - победитель! Супер!!! Поздравляю!\nВсе {count_candies} конфет твои!\nСпасибо за игру!\n\nИграть еще раз - /start')
                    data_player[2] = count_candies
                    data_player[4] = 0
                    data_player[6] = 0
                    data_player[7] = 0
                    data_player[8] = int(data_player[8]) + 1
                    data_player[9] = int(data_player[9]) + 1
                    data_player[10] = int(data_player[10]) + 1
                    update_data(check_stat_player, player_info, data_player, file_path)
                    state = ConversationHandler.END
            else:
                context.bot.send_message(update.effective_chat.id, f'❌ Ошибка! Ты можешь взять от 1 до {max_take_candies1} конфет.')
                error = 1
        else:
            context.bot.send_message(update.effective_chat.id, '❌ Ошибка! Введены некорректные данные.')
            error = 1
        
        # Ход делает бот
        file_statistic = get_data('hw9_statistic.csv')
        data_player = get_data_player(player_info, file_statistic)
        if int(data_player[4]) == 1 and error == 0:
            take_candies = bot_plays(data_player[3], data_player)
            data_player[2] = int(data_player[2]) - take_candies
            if max_take_candies1 > int(data_player[2]):
                max_take_candies1 = int(data_player[2])
            context.bot.send_message(update.effective_chat.id, f'''🤖 Я забрал {take_candies} конфет.
На столе осталось {data_player[2]} конфет(ы).
Твой ход! Ты можешь взять не более чем {max_take_candies1} конфет(ы). Отправь в чат количество конфет.''')
            if data_player[2] == 0:
                win = '🤖 BOT'
                context.bot.send_message(update.effective_chat.id, f'{win} - победитель!\nВсе {count_candies} конфет мои!\nСпасибо за игру!\n\nИграть еще раз - /start')
                data_player[2] = count_candies
                data_player[6] = 0
                data_player[7] = 0
                take_candies = 0
                data_player[8] = int(data_player[8]) + 1
                update_data(check_stat_player, player_info, data_player, file_path)
                state = ConversationHandler.END
            data_player[5] = 1
            data_player[7] = int(data_player[7]) + take_candies
            update_data(check_stat_player, player_info, data_player, file_path)
        else:
            data_player[4] = 1
            update_data(check_stat_player, player_info, data_player, file_path)
    return state

def cancel(update, context):
    context.bot.send_message(update.effective_chat.id, 'Что-то пошло не так.')

start_handler = CommandHandler('start', start)
rules_handler = CommandHandler('rules', rules)
level_handler = MessageHandler(Filters.text, level)
game_handler = MessageHandler(Filters.text, game)

cancel_handler = CommandHandler('cancel', cancel)

conv_handler = ConversationHandler(entry_points=[level_handler],
                                        states={A: [game_handler],
                                                B: [level_handler]},
                                        fallbacks=[cancel_handler])

dispatcher.add_handler(start_handler)
dispatcher.add_handler(rules_handler)
dispatcher.add_handler(conv_handler)

updater.start_polling() # start
updater.idle() # end
