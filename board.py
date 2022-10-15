from tarfile import LENGTH_LINK
from enums import Squares, PieceTypes
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
        self.whiteCastleKing = LEGAL
        self.whiteCastleQueen = LEGAL
        self.blackCastleKing = LEGAL
        self.blackCastleQueen = LEGAL

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

        self.activeWhitePieces = [self.wR1, self.wKn1, self.wB1, self.wQ, self.wKg, self.wB2, self.wKn2,
                                  self.wR2, self.wP1, self.wP2, self.wP3, self.wP4, self.wP5, self.wP6, self.wP7, self.wP8]
        self.activeBlackPieces = [self.bR1, self.bKn1, self.bB1, self.bQ, self.bKg,  self.bB2, self.bKn2,
                                  self.bR2, self.bP1, self.bP2, self.bP3, self.bP4, self.bP5, self.bP6, self.bP7, self.bP8]

        for p in self.activePieces:
            self.pieceSet[p.getSquare()] = p

    def move(self):
        self.turn = ~self.turn
        return

    def pop(self):
        self.moveQueue.pop()

    def getLegalMoves(self):
        legalMoves = []
        if self.turn == WHITE:
            if not self.whiteKinginCheck:
                for piece in self.activeWhitePieces:
                    legalMoves.append(self.getMovesByPiece(piece))
            else:
                legalMoves.append(self.getMovesByPiece(self.wKg))
        else:
            if not self.blackKinginCheck:
                for piece in self.activeBlackPieces:
                    legalMoves.append(self.getMovesByPiece(piece))
            else:
                legalMoves.append(self.getMovesByPiece(self.bKg))
        return legalMoves

    def getMovesByPiece(self, piece):
        if piece.getType == PieceTypes.KING:
            pass
            # Up
            # Down
            # Left
            # Right
            # TR
            # TL
            # BR
            # BL
            # Castle-King
            # Castle-Queen
        elif piece.getType == PieceTypes.QUEEN:
            pass
            # Up
            # Down
            # Left
            # Right
            # Slide TR
            # Slide TL
            # Slide BR
            # Slide BL
        elif piece.getType == PieceTypes.BISHOP:
            pass
            # Slide TR
            # Slide TL
            # Slide BR
            # Slide BL
        elif piece.getType == PieceTypes.KNIGHT:
            # 2U-1R
            # 2U-1L
            # 2D-1R
            # 2D-1L
            # 1U-2R
            # 1U-2L
            # 1D-2R
            # 1D-2L
            pass
        elif piece.getType == PieceTypes.ROOK:
            # Increment right
            # Increment left
            # Increment down
            # Increment up
            # Castle-King
            # Castle-Queen
            pass
        elif piece.getType == PieceTypes.PAWN:
            # 1-Forward
            # 1-Forward + Promotion
            # 2-Forward
            # TR-Capture-Normal
            # TL-Capture-Normal
            # TR-Capture-EP
            # TL-Capture-EP
            pass
        else:
            pass
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
        print(board.getLegalMoves())
        return

    if __name__ == "__main__":
        main()
