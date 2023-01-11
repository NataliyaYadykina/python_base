# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint

count_candies = 23
max_take_candies = 3
candies_player1 = 0
candies_player2 = 0
win = 0

# What is your name?
player1 = input('Enter your name, player 1: ')
player2 = ''

# Choose: bot or human:
is_bot = int(input('Enter - bot(1) or human(0): '))

if is_bot == 1:
    player2 = 'Bot'
else:
    player2 = input('Enter your name, player 2: ')

# Random - who starts the game (player 1 or player 2):
active_player = randint(1, 2)
if active_player == 1:
    active_player = player1
else:
    active_player = player2

# Play
print(f'{player1} vs {player2}')
print(f'{active_player} starts the game!')

while count_candies > 0:
    if is_bot == 1 and active_player == player2:
        if count_candies % (1 + max_take_candies) != 0:
            take_candies = count_candies % (1 + max_take_candies)
        else:
            take_candies = randint(1, max_take_candies)
    else:
        if max_take_candies > count_candies:
            max_take_candies = count_candies
        take_candies = abs(int(input(f'{active_player}, take no more than {max_take_candies} candies: ')))
    print(f'{active_player} took {take_candies} candies')
    if take_candies != 0 and take_candies <= max_take_candies and take_candies <= count_candies:
        count_candies -= take_candies
        if count_candies == 0:
            win = active_player
        if active_player == player1:
            candies_player1 += take_candies
            print(f'{active_player} has {candies_player1} candies')
            active_player = player2
        else:
            candies_player2 += take_candies
            print(f'{active_player} has {candies_player2} candies')
            active_player = player1
        print(f'There are {count_candies} candies left')
    else:
        print('Error! Incorrect number of candies! Try again.')

print(f'Win - {win}!!! {win} takes all candies!')

# Win
if win == player1:
    candies_player1 += candies_player2
    candies_player2 = 0
else:
    candies_player2 += candies_player1
    candies_player1 = 0

print(f'Result: {player1} has {candies_player1} candies, {player2} has {candies_player2} candies.')