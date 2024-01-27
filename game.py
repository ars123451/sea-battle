from player import *


class Game():
    _ships = [3, 2, 2, 1, 1, 1]
    _user = None
    _user_board = Board()
    _ai: Ai = None
    _ai_board = Board()

    @classmethod
    def _random_board(cls, board):  # Метод для рандомного размещения кораблей
        tr_limit = 2500
        tr = 0  # Количество попыток размещения кораблей
        attempt = 0
        for len in cls._ships:
            while tr < tr_limit:
                try:
                    x = random.randint(0, Board.SCALE() - 1)
                    y = random.randint(0, Board.SCALE() - 1)
                    dir = ["Горизонтально", "Вертикально"]
                    dir = random.choice(dir)
                    ship = Ship(x, y, len, dir)
                    board.add_ship(ship)
                except:
                    tr += 1
                else:
                    tr = 0
                    break

    @classmethod
    def _manual_board(cls,
                      board):  # Метод для создания доски вручную. Если честно, немного устаешь по одной координате писать. Поэтому не используется
        for len in cls._ships:
            while True:
                try:
                    print(f"Размещение {len}-палубного корабля")
                    print("Ориентация (0 - Вертикально/1 - Горизонтально)")
                    direction = int(input())
                    direction = "Горизонтально" if direction else "Вертикально"
                    print("Введите координату x: ")
                    x = int(input())
                    print("Введите координату y: ")
                    y = int(input())
                    ship = Ship(x, y, len, direction)
                    board.add_ship(ship)
                    board.board_view(True)
                except Exception as e:
                    print(e)
                    print("Начать размещение сначала или продолжить размещение? (закончить - 0/продолжить - 1)")
                    if int(input()):
                        continue
                    else:
                        raise BoardCreatingError()
                else:
                    break

    @classmethod
    def greet(cls):
        print("Морской бой 6x6. Противник - бот")
        cls._random_board(cls._ai_board)
        cls._random_board(cls._user_board)
        cls._user = User(cls._user_board, cls._ai_board)
        cls._ai = Ai(cls._ai_board, cls._user_board)

    @classmethod
    def loop(cls):  # Проверяем, кто победил
        while True:
            cls._user.move()
            cls._ai.move()
            if cls._user_board.get_ships_left == 0:
                print("Робот победил")
                break
            elif cls._ai_board.get_ships_left == 0:
                print("Вы победили")
                break
            else:
                continue

    @classmethod
    def start(cls):
        cls.greet()
        cls.loop()