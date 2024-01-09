def print_grid(grid_list):
    row = "\n %s | %s | %s "
    divider = "\n---+---+--- "
    print((row + divider + row + divider + row) % tuple(grid_list))


mylist = ['1', '2', '3', '4', 'x', '6', '7', '8', '9']
print_grid(mylist)
