def print_table(table):
    divider = "---+---+---"
    rows = []
    for i in range(3):
        rows.append(" %s | %s | %s " % (table[i][0], table[i][1], table[i][2]))
    print(rows[0] + "\n" + divider + "\n" + rows[1] + "\n" + divider + "\n" + rows[2] + "\n")
