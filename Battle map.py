



first = Dot(3, 4)
try:

    x, y = first.get_coordinates()
    print(map[x][y])
except IndexError:
    print('Index is out of map')
