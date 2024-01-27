from exceptions import *


class Dot():
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f'Dot: {self.x, self.y}'


class Ship():
    def __init__(self, x: int, y: int, len: int, direction: str):
        if direction not in ["Горизонтально", "Вертикально"]:  # Проверка входного параметра direction
            raise IncorrectShipDirection("Некорректное направление корабля")
        self._x = x
        self._y = y
        self._len = self._lifes = len
        self._direction = direction

    @property
    def lifes(self):
        return self._lifes

    @property
    def dots(self) -> list:  # Получаем точки корабля
        dots = []
        if self._direction == "Горизонтально":  #
            for i in range(self._len):
                dots.append(Dot(self._x - i, self._y))
            dots.reverse()
        elif self._direction == "Вертикально":  #
            for i in range(self._len):
                dots.append(Dot(self._x, self._y - i))
            dots.reverse()
        return dots

    @property
    def contour(self):
        contour = []
        for dot in self.dots:
            for x in range(dot.x - 1, dot.x + 2):
                for y in range(dot.y - 1, dot.y + 2):
                    if (Dot(x, y) in self.dots or Dot(x, y) in contour):
                        continue
                    else:
                        contour.append(Dot(x, y))
        return contour

    def hit(self):  # Метод, отбавляющий 1 жизнь у корабля
        self._lifes -= 1


class Board():
    _scale = 6

    def __init__(self):
        self._ships = []  # Список кораблей
        self._ships_left = 0  # Количество живых кораблей
        self._board = ["| О |"] * self._scale
        for i in range(self._scale):
            self._board[i] = ["| О |"] * self._scale

    @classmethod
    def SCALE(cls):  # Получаем масштаб доски
        return cls._scale

    def out(self, dot: Dot) -> bool:
        return dot.x < 0 or dot.y < 0 or dot.x > self._scale - 1 or dot.y > self._scale - 1

    def add_ship(self, ship: Ship):
        for dot in ship.dots:
            if self.out(dot):  # Проверка на выход координат за границы
                raise IncorrectShipPlacement("Корабль выходит за границы")
            for other_ship in self._ships:  # Проверка на пересечение с другим кораблем
                if dot in other_ship.dots or dot in other_ship.contour:
                    raise IncorrectShipPlacement(f"Корабль пересекается с другим кораблем. Точка ({dot.x}, {dot.y})")
            self._board[dot.x][dot.y] = "| ■ |"
        self._ships.append(ship)
        self._ships_left += 1

    @property
    def get_ships(self):  # Получаем все корабли экземпляры Ship
        return self._ships

    @property
    def get_ships_left(self):  # Получаем оставшееся количество кораблей
        return self._ships_left

    def board_view(self, hid: bool):  # Вывод доски
        print("  | 1 |  | 2 |  | 3 |  | 4 |  | 5 |  | 6 |\n\n")
        if hid is False:
            for col in range(self._scale):
                print(col + 1, end=" ")
                for row in range(self._scale):
                    if self._board[row][col] == "| ■ |":
                        print("| О |", end="  ")
                    else:
                        print(self._board[row][col], end="  ")
                print("\n")
        elif hid is True:
            for col in range(self._scale):
                print(col + 1, end=" ")
                for row in range(self._scale):
                    print(self._board[row][col], end="  ")
                print("\n")

    def shot(self, dot: Dot) -> bool:
        if self.out(dot) or self._board[dot.x][dot.y] == "T" or self._board[dot.x][
            dot.y] == "X":  # Проверка на попадание в пределах границы и отсуствие повторения
            raise IncorrectShotPoint()
        else:
            self._board[dot.x][dot.y] = "| T |"
            for ship in self._ships:
                if dot in ship.dots:
                    ship.hit()
                    if ship.lifes == 0:
                        self._ships_left -= 1  # Уменьшаем количество живых кораблей на 1, если корабль убит
                        for contour in ship.contour:
                            if (contour.x >= 0 and contour.y >= 0 and contour.x < self._scale and
                                    contour.y < self._scale):
                                self._board[contour.x][contour.y] = "| T |"
                    self._board[dot.x][dot.y] = "| X |"  # отметка попадания в корабль
                    return True  # Возвращаем true если попали в корабль и false если не попали
        return False