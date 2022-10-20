from enums import PieceTypes, Squares


class Piece():
    def __init__(self, position: Squares, color: int, type: int) -> None:
        self.type = type
        self.color = color
        self.position = position.value
        self.attackMap = 0
        self.hasMoved = False

    def setSquare(self, position: int):
        self.position = position

    def getSquare(self) -> int:
        return self.position

    def getType(self):
        return self.type

    def getColor(self):
        return self.color

    def getHasMoved(self):
        return self.hasMoved;
    
    def setHasMoved(self):
        self.hasMoved = True;
      

class Pawn(Piece):
    def __init__(self, position: int, color: str) -> None:
        self.canEp = False
        self.epDir = None
        self.epMove = None
        super().__init__(position, color, PieceTypes.PAWN)

    def setEp(self, epDir: int, epMove: int):
        self.canEp = True
        self.epDir = epDir
        self.epMove = epMove


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
