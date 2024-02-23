def get_player_input(turn_counter, table):
    is_valid_input = False
    while not is_valid_input:
        if turn_counter % 2 == 1:
            x_num = int(input("X turn (enter a number between 1 to 9): "))
            row = (x_num - 1) // 3
            col = x_num - (row * 3) - 1
            if table[row][col] == str(x_num):
                table[row][col] = 'X'
                is_valid_input = True
        else:
            o_num = int(input("O turn (enter a number between 1 to 9): "))
            row = (o_num - 1) // 3
            col = o_num - (row * 3) - 1
            if table[row][col] == str(o_num):
                table[row][col] = 'O'
                is_valid_input = True
    return table