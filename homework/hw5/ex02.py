# 2) Создайте программу для игры в ""Крестики-нолики"" человек vs человек.
# 1 | 2 | X
# 4 | X | O
# X | 8 | O

from random import randint

# New field
def new_field(row):
    field = [i + 1 for i in range(row ** 2)]
    return field

# Print game field
def print_field(row, fill_field):
    div = ' '
    for i in range(row):
        for j in range(row):
            if j: div = ' | '
            print(f'{div}{fill_field[j + row * i]}', end = '')
            div = ' '
        print()

# Get free cells
def free_cells(fill_field):
    free_cells = []
    for i in range(len(fill_field)):
        if fill_field[i] != 'x' and fill_field[i] != '0':
            free_cells.append(i + 1)
    return free_cells

# Update game field
def update_field(cell_number, row, fill_field):
    next_player = False
    if cell_number.isdigit() and int(cell_number) > 0 and int(cell_number) <= row ** 2:
        cell = int(cell_number)
        if fill_field[cell - 1] != 'x' and fill_field[cell - 1] != '0':
            fill_field[cell - 1] = symbol
            next_player = True
        else:
            print('This sell not empty! Choose other cell from list:')
    else:
        print('Error! The wrong cell number. Try again.')
    return next_player

# win?
def check_win(row, fill_field):
    win = False
    if fill_field.count('x') > 2 or fill_field.count('0') > 2:
        string1 = '0' * row
        string2 = 'x' * row
        temp_string_gorizontal = ''
        temp_string_vertical = ''
        temp_string_diagonal1 = ''
        temp_string_diagonal2 = ''
        add_ind = 0
        # print(string1, string2)
        for i in range(0, len(fill_field), row):
            for j in range(0, row):
                # print(f'1. i = {i}; j = {j}; add_ind = {add_ind}')

                # print('Check gorizontal:')
                temp_string_gorizontal += str(fill_field[i + j])
                # print(temp_string_gorizontal)
                if temp_string_gorizontal == string1 or temp_string_gorizontal == string2:
                    win = True

                # print('Check vertical:')
                temp_string_vertical += str(fill_field[j * row + add_ind])
                # print(temp_string_vertical)
                if temp_string_vertical == string1 or temp_string_vertical == string2:
                    win = True

                # print('Check diagonal1:')
                temp_string_diagonal1 += str(fill_field[j * row + j])
                # print(temp_string_diagonal1)
                if temp_string_diagonal1 == string1 or temp_string_diagonal1 == string2:
                    win = True

                # print('Check diagonal2:')
                temp_string_diagonal2 += str(fill_field[j * 2 + 2])
                # print(temp_string_diagonal2)
                if temp_string_diagonal2 == string1 or temp_string_diagonal2 == string2:
                    win = True
                
            temp_string_gorizontal = ''
            temp_string_vertical = ''
            temp_string_diagonal1 = ''
            temp_string_diagonal2 = ''
            add_ind += 1
            if win:
                break
    return win
        

# What is your name?
player1 = input('Enter your name, player 1 (x): ')
player2 = input('Enter your name, player 2 (0): ')
row = 3
count_steps = 0
win = False

# Random - who starts the game (player 1 or player 2):
active_player = randint(1, 2)
if active_player == 1:
    active_player = player1
    symbol = 'x'
else:
    active_player = player2
    symbol = '0'

# Play
print(f'Start game: {player1} vs {player2}!')
fill_field = new_field(row)
print(f'{active_player} ({symbol}) starts the game!')

while count_steps < row ** 2 and win == False:
    print_field (row, fill_field)
    if win == False:
        empty_cells = free_cells(fill_field)
        cell = input(f'{active_player} ({symbol}), choose one free cell {empty_cells}:')
        if update_field(cell, row, fill_field):
            win = check_win(row, fill_field)
            if not win:
                empty_cells = free_cells(fill_field)
                if active_player == player1:
                    active_player = player2
                    symbol = '0'
                else:
                    active_player = player1
                    symbol = 'x'
                count_steps += 1
else:
    print_field (row, fill_field)
    if win:
        print(f'{active_player} ({symbol}) win!!!')
    else:
        print('Nobody wins.')