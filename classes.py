class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.damage = False
        self.contour = False
        self.ship = False
        self.ship_damage = False

    def get_coordinates(self):
        return self.x, self.y

    def __str__(self):
        if self.ship_damage:
            return '#'
        elif self.ship:
            return '='
        elif self.contour:
            return '-'
        elif self.damage:
            return '/'
        else:
            return '*'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def is_in_map(self):
        if self.x in range(0, 6) and self.y in range(0, 6):
            return True
        else:
            print('Not in map!')
            return False

    def can_be_damage(self):
        if self.damage == False and self.contour == False:
            return True
        else:
            return False

    def can_be_ship(self):
        if self.is_in_map() == True and self.ship == False and self.contour == False:
            return True
        else:
            return False

    def set_contur(self):
        self.damage = False
        self.contour = True

    def set_damage(self):
        self.damage = True

    def set_ship(self):
        self.ship = True


class Ship:
    def __init__(self, len, begin, orientation, hearts):
        self.len = len
        self.begin = begin
        self.orientation = orientation
        self.hearts = hearts


class Board:
    def __init__(self):
        self.ships = {'four': 1, 'three': 2, 'one': 4}
        # self.def_board = [['o', 'o', 'o', 'o', 'o', 'o'],
        #                   ['o', 'o', 'o', 'o', 'o', 'o'],
        #                   ['o', 'o', 'o', 'o', 'o', 'o'],
        #                   ['o', 'o', 'o', 'o', 'o', 'o'],
        #                   ['o', 'o', 'o', 'o', 'o', 'o'],
        #                   ['o', 'o', 'o', 'o', 'o', 'o']]
        self.board = [['o', 'o', 'o', 'o', 'o', 'o'],
                      ['o', 'o', 'o', 'o', 'o', 'o'],
                      ['o', 'o', 'o', 'o', 'o', 'o'],
                      ['o', 'o', 'o', 'o', 'o', 'o'],
                      ['o', 'o', 'o', 'o', 'o', 'o'],
                      ['o', 'o', 'o', 'o', 'o', 'o']]
        self.hiden = False

    def show_map(self):
        return f'  1 2 3 4 5 6\n' \
               f'1 {self.board[0][0]} {self.board[0][1]} {self.board[0][2]} {self.board[0][3]} {self.board[0][4]} {self.board[0][5]}\n' \
               f'2 {self.board[1][0]} {self.board[1][1]} {self.board[1][2]} {self.board[1][3]} {self.board[1][4]} {self.board[1][5]}\n' \
               f'3 {self.board[2][0]} {self.board[2][1]} {self.board[2][2]} {self.board[2][3]} {self.board[2][4]} {self.board[2][5]}\n' \
               f'4 {self.board[3][0]} {self.board[3][1]} {self.board[3][2]} {self.board[3][3]} {self.board[3][4]} {self.board[3][5]}\n' \
               f'5 {self.board[4][0]} {self.board[4][1]} {self.board[4][2]} {self.board[4][3]} {self.board[4][4]} {self.board[4][5]}\n' \
               f'6 {self.board[5][0]} {self.board[5][1]} {self.board[5][2]} {self.board[5][3]} {self.board[5][4]} {self.board[5][5]}'

    def initialisation(self):
        for i in range(6):
            for j in range(6):
                self.board[i][j] = Dot(i, j)

    def add_ship(self, ship):
        try:
            x, y = ship.begin
            if self.board[x][y].can_be_ship():
                if ship.orientation == 'hor':
                    ship.begin[1] += ship.len - 1
                    last_x, last_y = ship.begin
                    if self.board[last_x][last_y].can_be_ship:
                        for i in range(y, last_y + 1):
                            self.board[x][i].set_ship()
                    else:
                        print('You can not install this ship!')
                elif ship.orientation == 'ver':
                    ship.begin[0] += ship.len - 1
                    last_x, last_y = ship.begin
                    if self.board[last_x][last_y].can_be_ship:
                        for i in range(x, last_x + 1):
                            self.board[i][y].set_ship()
                    else:
                        print('You can not install this ship!')
                else:
                    print("We can't do this orientation!")

            self.show_map()
        except Exception as exc:
            print(exc)


a = Board()
a.initialisation()
b = Ship(2, [1, 2], 'hor', 3)
c = Ship(4, [2, 5], 'ver', 3)
a.add_ship(b)
a.add_ship(c)
print(a.show_map())
