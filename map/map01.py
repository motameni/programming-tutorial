mylist = [1, 2, 3, 4]

def double(num):
    return num * 2

map_result = map(double, mylist)

print(map_result)

list_result = list(map_result)

print(list_result)
