from move import Move
from enums import Squares


def test():
    assert (1 == 1)


def generateMoves():
    board = board()  # start position
    move = Move(Squares.A1, Squares.A2,)
    assert (board.generateMoves())
