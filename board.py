from enums import Squares
from pieces import Pawn, Rook, Knight, Queen, King, Bishop
import queue

LEGAL = True
ILLEGAL = False
WHITE_TURN = 0
BLACK_TURN = 1
WHITE = 0
BLACK = 1
NONE = 0


class Board:
    def __init__(self) -> None:
        self.pieceSet = {}
        self.moveQueue = queue.Queue()
        self.activePieces = []

        self.turn = WHITE_TURN
        self.whiteCastlineRights = LEGAL
        self.blackCastlingRights = LEGAL
        self.movesWithoutCapture = NONE
        self.whiteKinginCheck = False
        self.blackKinginCheck = False

        self.wR1 = Rook(Squares.A1, WHITE)
        self.wKn1 = Knight(Squares.B1, WHITE)
        self.wB1 = Bishop(Squares.C1, WHITE)
        self.wQ = Queen(Squares.D1, WHITE)
        self.wKg = King(Squares.E1, WHITE)
        self.wB2 = Bishop(Squares.F1, WHITE)
        self.wKn2 = Knight(Squares.G1, WHITE)
        self.wR2 = Rook(Squares.H1, WHITE)
        self.wP1 = Pawn(Squares.A2, WHITE)
        self.wP2 = Pawn(Squares.B2, WHITE)
        self.wP3 = Pawn(Squares.C2, WHITE)
        self.wP4 = Pawn(Squares.D2, WHITE)
        self.wP5 = Pawn(Squares.E2, WHITE)
        self.wP6 = Pawn(Squares.F2, WHITE)
        self.wP7 = Pawn(Squares.G2, WHITE)
        self.wP8 = Pawn(Squares.H2, WHITE)

        self.bR1 = Rook(Squares.A8, BLACK)
        self.bKn1 = Knight(Squares.B8, BLACK)
        self.bB1 = Bishop(Squares.C8, BLACK)
        self.bQ = Queen(Squares.D8, BLACK)
        self.bKg = King(Squares.E8, BLACK)
        self.bB2 = Bishop(Squares.F8, BLACK)
        self.bKn2 = Knight(Squares.G8, BLACK)
        self.bR2 = Rook(Squares.H8, BLACK)
        self.bP1 = Pawn(Squares.A7, BLACK)
        self.bP2 = Pawn(Squares.B7, BLACK)
        self.bP3 = Pawn(Squares.C7, BLACK)
        self.bP4 = Pawn(Squares.D7, BLACK)
        self.bP5 = Pawn(Squares.E7, BLACK)
        self.bP6 = Pawn(Squares.F7, BLACK)
        self.bP7 = Pawn(Squares.G7, BLACK)
        self.bP8 = Pawn(Squares.H7, BLACK)

        self.activePieces = [self.wR1, self.wKn1, self.wB1, self.wQ, self.wKg, self.wB2, self.wKn2, self.wR2, self.wP1, self.wP2, self.wP3, self.wP4, self.wP5, self.wP6, self.wP7,
                             self.wP8, self.bR1, self.bKn1, self.bB1, self.bQ, self.bKg,  self.bB2, self.bKn2, self.bR2, self.bP1, self.bP2, self.bP3, self.bP4, self.bP5, self.bP6, self.bP7, self.bP8]

        for p in self.activePieces:
            self.pieceSet[p.getSquare()] = p

    def move(self):
        self.turn = ~self.turn
        return

    def pop(self):
        self.moveQueue.pop()

    def getLegalMoves(self):
        arr = []
        # Iterate through squares
        # Generate moves for each piece by calling getMoves() for each piece
        return

    def setBoard(self, fen: str):
        return

    def getTurn(self) -> int:
        return self.turn

    def printBoard(self):
        flag = WHITE
        temp = ""
        i = 1
        for square in Squares:
            if square in self.pieceSet:
                temp += self.pieceSet[square].getType()[0]
            else:
                if flag == WHITE:
                    temp += "--"
                else:
                    temp += "++"
                flag = ~flag
            temp += " "
            if (i % 8 == 0):
                print(temp)
                temp = ""
                i = 1
                flag = ~flag
            else:
                i += 1


class Main:
    def main():
        board = Board()
        board.printBoard()
        return

    if __name__ == "__main__":
        main()
