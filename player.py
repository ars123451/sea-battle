from backlogic import *
import random


class Player():
    def __init__(self, board: Board, enemy_board: Board):
        self._board: Board = board
        self._enemy_board: Board = enemy_board

    def _ask(self):
        pass

    def move(self):
        pass

    def boards_view(self):
        print("Твоя доска. Живых кораблей: " + str(self._board._ships_left))
        self._board.board_view(True)
        print("Доска противника. Живых кораблей: " + str(self._enemy_board._ships_left))
        self._enemy_board.board_view(False)


class User(Player):
    def _ask(self):
        print("x: ", end=" ")
        x = int(input()) - 1
        print("\ny: ", end=" ")
        y = int(input()) - 1
        return Dot(x, y)

    def move(self):
        while True:
            self.boards_view()
            dot = self._ask()
            try:
                if self._enemy_board.shot(dot):
                    continue
                else:
                    break
            except:
                print("Попробуй снова")
                continue


class Ai(Player):
    def _ask(self):
        x = random.randint(0, Board.SCALE() - 1)
        y = random.randint(0, Board.SCALE() - 1)
        return Dot(x, y)

    def move(self):
        while True:
            dot = self._ask()
            try:
                if self._enemy_board.shot(dot):
                    continue
                else:
                    break
            except:
                continue