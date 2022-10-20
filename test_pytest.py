from move import Move
from enums import Squares
from board import Board

def test():
    assert (1 == 1)

def generateMoves():
    board = Board()  # start position
    move = Move(Squares.A1, Squares.A2,)
    assert (board.generateMoves())
