import math
from enums import MoveCodes, Squares, PieceTypes
from pieces import Pawn, Rook, Knight, Queen, King, Bishop, Piece
from move import Move
import queue

LEGAL = True
ILLEGAL = False
WHITE_TURN = 0
BLACK_TURN = 1
WHITE = 0
BLACK = 1
NONE = 0
POSITIVE = 1
NEGATIVE = 1

FILE_BIT = 8
RANK_BIT = 1
FIRST_SQUARE = 1
LAST_SQUARE = 9223372036854775808


class Board:

    def __init__(self) -> None:
        self.pieceSet = {}
        self.positions = {}  # Set of position ID's for 3-Fold
        self.moveQueue = queue.Queue()
        self.activePieces = []
        self.legalMoves = []

        self.turn = WHITE_TURN
        self.gameOver = False
        self.whiteCastleKing = LEGAL
        self.whiteCastleQueen = LEGAL
        self.blackCastleKing = LEGAL
        self.blackCastleQueen = LEGAL

        self.moveCounter = NONE
        self.movesWithoutCapture = NONE
        self.movesRepeated = NONE
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

        for p in self.activeWhitePieces:
            self.pieceSet[p.getSquare()] = p
        for p in self.activeBlackPieces:
            self.pieceSet[p.getSquare()] = p

    def move(self, move: Move):
        if move in self.generateLegalMoves():
            if self.turn == WHITE:
                self.moveCounter += 1
            if self.isCheck(move):
                if self.turn == WHITE:
                    self.whiteKinginCheck = True
                else:
                    self.blackKinginCheck = True
            self.turn = ~self.turn
            move.getStartPiece().setSquare(move.getEndSquare())
        else:
            raise ValueError("Invalid Move")

        # Update flags
        # isGameOver
        # Draws: stalemate / 50-move
        # 3 - Fold

    def pop(self):
        self.moveQueue.pop()

    def generateLegalMoves(self):

        if self.turn == WHITE:
            if not self.whiteKinginCheck:
                for piece in self.activeWhitePieces:
                    self.getMovesByPiece(piece)
            else:
                self.getMovesByPiece(self.wKg)
        else:
            if not self.blackKinginCheck:
                for piece in self.activeBlackPieces:
                    self.getMovesByPiece(piece)
            else:
                self.getMovesByPiece(self.bKg)
        return self.legalMoves

    def getMovesByPiece(self, startPiece: Piece):

        sign = POSITIVE
        startSquare: int = startPiece.getSquare()
        endSquare: int = NONE
        endPiece = None

        # 0 0 0 0 0 0 0 0
        # 0 0 0 0 0 0 0 0
        # 0 0 0 0 0 0 0 0
        # 0 0 0 0 0 0 0 0
        # 0 0 0 0 0 0 0 0
        # 0 0 0 0 0 0 0 0
        # 0 0 0 0 0 0 0 0
        # 1 2 0 0 0 0 0 0

        if startPiece.getColor:
            sign = NEGATIVE
        if startPiece.getType() == PieceTypes.KING:
            pass

            # Move up rank, SR 8
            # Move down rank, SL 8

            # Up
            endSquare = startSquare >> FILE_BIT
            self.normalProbe(startPiece, endSquare)
            # Down
            # Left
            # Right
            # TR
            # TL
            # BL
            # BR

            # Down
            # Left
            # Right
            # TR
            # TL
            # BR
            # BL
            # Castle-King
            # Castle-Queen
        elif startPiece.getType() == PieceTypes.QUEEN:
            pass
            # Up
            # Down
            # Left
            # Right
            # Slide TR
            # Slide TL
            # Slide BR
            # Slide BL
        elif startPiece.getType() == PieceTypes.BISHOP:
            pass
            # Slide TR
            # Slide TL
            # Slide BR
            # Slide BL
        elif startPiece.getType() == PieceTypes.KNIGHT:
            # 2U-1R
            # 2U-1L
            # 2D-1R
            # 2D-1L
            # 1U-2R
            # 1U-2L
            # 1D-2R
            # 1D-2L
            pass
        elif startPiece.getType() == PieceTypes.ROOK:
            # Increment right
            # Increment left
            # Increment down
            # Increment up
            # Castle-King
            # Castle-Queen
            pass
        elif startPiece.getType() == PieceTypes.PAWN:
            # 1-Forward
            endSquare = startSquare << 1 * sign
            self.normalProbe(startPiece, endSquare)
            # 1-Forward + Promotion
            # 2-Forward
            # TR-Capture-Normal
            # TL-Capture-Normal
            # TR-Capture-EP
            # TL-Capture-EP
            pass
        else:
            pass

    def normalProbe(self, startPiece: Piece, endSquare: int):
        # Probes hash table at endSqaure location, adds moves
        endPiece: Piece
        startSquare: int = startPiece.getSquare()
        if self.onBoard(endSquare):
            if endSquare in self.pieceSet:
                endPiece = self.pieceSet[startPiece.getSquare()]
                if endPiece.getColor() != startPiece.getColor():
                    self.legalMoves.append(
                        Move(startSquare, endSquare, startPiece, endPiece, MoveCodes.CAPTURES))
            else:
                self.legalMoves.append(
                    Move(startSquare, endSquare, startPiece, None, MoveCodes.QUIET_MOVE))

    def onBoard(self, i: int):
        return i >= FIRST_SQUARE and i <= LAST_SQUARE and math.log(i, 2) % 1 == 0

    def generateOppAttackMaps(self):
        attackMaps = []
        if self.turn == WHITE:
            pass
        else:
            pass
        return attackMaps

    def isCheck(self, move: Move):
        # If king in piece attack map --> return true
        # Only generate attack map for moves made
        return False

    def isCheckMate(self, move: Move):
        if self.isCheck(move):
            for move in self.generateOppAttackMaps():
                pass
            # Generate opposite color attack maps
            # If all king moves in at least one attack map: mate
            pass
        return False

    def setBoard(self, fen: str):
        return

    def getTurn(self):
        if self.turn == WHITE:
            return "White"
        else:
            return "Black"

    def printBoard(self):
        flag = WHITE
        temp, p = "", ""
        i = 1
        for square in Squares:
            if square in self.pieceSet:
                if self.pieceSet[square].getType() == PieceTypes.BISHOP:
                    p = "B"
                elif self.pieceSet[square].getType() == PieceTypes.KING:
                    p = "K"
                elif self.pieceSet[square].getType() == PieceTypes.KNIGHT:
                    p = "K"
                elif self.pieceSet[square].getType() == PieceTypes.ROOK:
                    p = "R"
                elif self.pieceSet[square].getType() == PieceTypes.PAWN:
                    p = "P"
                elif self.pieceSet[square].getType() == PieceTypes.QUEEN:
                    p = "Q"
                if self.pieceSet[square].getColor() == BLACK:
                    p = p.lower()
                temp += p
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
        print(board.generateLegalMoves())

        # board.printBoard()
        return

    if __name__ == "__main__":
        main()
