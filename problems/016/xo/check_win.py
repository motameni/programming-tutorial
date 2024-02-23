def check_win(table):
    for i in range(3):
        row = table[i]
        if row[0] == row[1] and row[0] == row[2]:
            return True
    
    for i in range(3):
        cell1 = table[0][i]
        cell2 = table[1][i]
        cell3 = table[2][i]
        if cell1 == cell2 and cell1 == cell3:
            return True
        
    if table[0][0] == table[1][1] and table[0][0] == table[2][2]:
            return True
    
    if table[0][2] == table[1][1] and table[0][2] == table[2][0]:
            return True
    
    return False