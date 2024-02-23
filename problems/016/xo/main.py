# step 1: show table
# step 2: get player input
# step 3: check win condition

from print import print_table
from input import get_player_input
from check_win import check_win

table = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
]

turn_counter = 0

while True:
    print_table(table)
    turn_counter += 1
    table = get_player_input(turn_counter, table)
    if check_win(table):
        if turn_counter % 2 == 1:
            print("X win!")
        else:
            print("O win!")
        break

    if turn_counter == 9:
        print("Draw!")
        break
