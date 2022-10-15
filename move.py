from pieces import Piece


class Move():
    def __init__(self, startSquare: int, endSquare: int, startPiece: Piece, endPiece, moveType: int) -> None:
        self.startSquare = startSquare
        self.endSquare = endSquare
        self.startPiece = startPiece
        self.endPiece = endPiece
        self.moveType = moveType
