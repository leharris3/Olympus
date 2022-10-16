from chess import PAWN
from enums import PieceTypes


class Piece():
    def __init__(self, position: int, color: int, type: int) -> None:
        self.type = type
        self.color = color
        self.position = position
        self.attackMap = 0

    def getSquare(self):
        return self.position

    def getType(self):
        return self.type

    def getColor(self):
        return self.color


class Pawn(Piece):
    def __init__(self, position: int, color: str) -> None:
        super().__init__(position, color, PieceTypes.PAWN)


class Bishop(Piece):
    def __init__(self, position: int, color: str) -> None:
        super().__init__(position, color, PieceTypes.BISHOP)


class Knight(Piece):
    def __init__(self, position: int, color: str) -> None:
        super().__init__(position, color, PieceTypes.KNIGHT)


class Rook(Piece):
    def __init__(self, position: int, color: str) -> None:
        super().__init__(position, color, PieceTypes.ROOK)


class Queen(Piece):
    def __init__(self, position: int, color: str) -> None:
        super().__init__(position, color, PieceTypes.QUEEN)


class King(Piece):
    def __init__(self, position: int, color: str) -> None:
        super().__init__(position, color, PieceTypes.KING)
