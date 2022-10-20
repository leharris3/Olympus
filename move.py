from pieces import Piece


class Move():
    def __init__(self, startSquare: int, endSquare: int, startPiece: Piece, endPiece, moveType: int) -> None:
        self.startSquare = startSquare
        self.endSquare = endSquare
        self.startPiece = startPiece
        self.endPiece = endPiece
        self.moveType = moveType

    def getStartPiece(self):
        return self.startPiece

    def getEndPiece(self):
        return self.endPiece

    def getStartSquare(self):
        return self.startSquare

    def getEndSquare(self):
        return self.endSquare

    def getMoveType(self):
        return self.moveType
