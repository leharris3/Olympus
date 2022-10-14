from squares import Squares
from pieces import Pawn, Rook, Knight, Queen, King, Bishop


WHITE_TURN = 0
BLACK_TURN = 1
WHITE = 0
BLACK = 1


class Board:

    def __init__(self) -> None:
        self.pieceSet = {}
        self.turn = WHITE_TURN

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

        self.pieceSet[self.wR1.getSquare()] = self.wR1
        self.pieceSet[self.wKn1.getSquare()] = self.wKn1
        self.pieceSet[self.wB1.getSquare()] = self.wB1
        self.pieceSet[self.wQ.getSquare()] = self.wQ
        self.pieceSet[self.wKg.getSquare()] = self.wKg
        self.pieceSet[self.wB2.getSquare()] = self.wB2
        self.pieceSet[self.wKn2.getSquare()] = self.wKn2
        self.pieceSet[self.wR2.getSquare()] = self.wR2
        self.pieceSet[self.wP1.getSquare()] = self.wP1
        self.pieceSet[self.wP2.getSquare()] = self.wP2
        self.pieceSet[self.wP3.getSquare()] = self.wP3
        self.pieceSet[self.wP4.getSquare()] = self.wP4
        self.pieceSet[self.wP5.getSquare()] = self.wP5
        self.pieceSet[self.wP6.getSquare()] = self.wP6
        self.pieceSet[self.wP7.getSquare()] = self.wP7
        self.pieceSet[self.wP8.getSquare()] = self.wP8

        self.pieceSet[self.bR1.getSquare()] = self.bR1
        self.pieceSet[self.bKn1.getSquare()] = self.bKn1
        self.pieceSet[self.bB1.getSquare()] = self.bB1
        self.pieceSet[self.bQ.getSquare()] = self.bQ
        self.pieceSet[self.bKg.getSquare()] = self.bKg
        self.pieceSet[self.bB2.getSquare()] = self.bB2
        self.pieceSet[self.bKn2.getSquare()] = self.bKn2
        self.pieceSet[self.bR2.getSquare()] = self.bR2
        self.pieceSet[self.bP1.getSquare()] = self.bP1
        self.pieceSet[self.bP2.getSquare()] = self.bP2
        self.pieceSet[self.bP3.getSquare()] = self.bP3
        self.pieceSet[self.bP4.getSquare()] = self.bP4
        self.pieceSet[self.bP5.getSquare()] = self.bP5
        self.pieceSet[self.bP6.getSquare()] = self.bP6
        self.pieceSet[self.bP7.getSquare()] = self.bP7
        self.pieceSet[self.bP8.getSquare()] = self.bP8

    def move(self):
        self.turn = BLACK_TURN
        return

    def getTurn(self) -> int:
        return self.turn

    def printBoard(self):
        flag = WHITE
        temp = ""
        i = 1
        for square in Squares:
            if square in self.pieceSet:
                temp += self.pieceSet[square].getType()[0:1]
            else:
                if flag == WHITE:
                    temp += "--"
                    flag = BLACK
                else:
                    temp += "++"
                    flag = WHITE
            temp += " "
            if (i % 8 == 0):
                print(temp)
                temp = ""
                i = 1
                if flag == WHITE:
                    flag = BLACK
                else:
                    flag = WHITE
            else:
                i += 1


class Main:
    def main():
        board = Board()
        board.printBoard()
        return

    if __name__ == "__main__":
        main()
