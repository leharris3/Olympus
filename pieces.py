class Piece():
    def __init__(self, position: int, color: str, type: str) -> None:
        self.type = type
        self.color = color
        self.position = position

    def getSquare(self):
        return self.position

    def getType(self):
        return self.type


class Pawn(Piece):
    def __init__(self, position: int, color: str) -> None:
        super().__init__(position, color, "Pawn")


class Bishop(Piece):
    def __init__(self, position: int, color: str) -> None:
        super().__init__(position, color, "Bishop")


class Knight(Piece):
    def __init__(self, position: int, color: str) -> None:
        super().__init__(position, color, "Knight")


class Rook(Piece):
    def __init__(self, position: int, color: str) -> None:
        super().__init__(position, color, "Rook")


class Queen(Piece):
    def __init__(self, position: int, color: str) -> None:
        super().__init__(position, color, "Queen")


class King(Piece):
    def __init__(self, position: int, color: str) -> None:
        super().__init__(position, color, "King")
