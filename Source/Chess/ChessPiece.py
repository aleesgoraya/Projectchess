from abc import ABC, abstractclassmethod


class ChessPiece(ABC):
    """A class representing a chess piece in the chess game.

    ==Private Attribute==
    _color: the color of this chess piece
    _position: the position of the chess piece
    """
    _color: str
    _position: tuple

    # position is an array containing row and col
    # e.g (0,1) 0 is row and 1 is col
    def __init__(self, color, position) -> None:
        """Initialize a chess piece with <color> and <position>.
        """
        self._color = color
        self._position = position

    def get_color(self) -> str:
        """Return the color of this piece.
        """
        return self._color

    def get_position(self) -> tuple:
        """Return the position of this piece.
        """
        return self._position

    def move(self, position) -> None:
        """Change the position of this piece to <position>.
        """
        self._position = position

    def get_valid_coordinates(self) -> list:
        """Return a list of valid moves of this piece.
        """
        raise NotImplementedError

    def valid_coordinates(self, row, col) -> bool:
        """
        Return true iff the (row, col) is a position that the piece can move to.
        """
        valid = False

        for move in self.get_valid_coordinates():
            if row == move[0] and col == move[1]:
                valid = True

        return valid

    def check_move(self, row, col, board) -> bool:
        """
        Return true iff there's a piece on the way. Checks to see if there are
        any pieces between starting position and position the piece is being
        moved to. (row,col) is the desired position, and board is the board
        being used.
        """
        if not self.valid_coordinates(row, col):
            return False

        right = False
        left = False
        forward = False
        back = False

        check_position = [self._position[0], self._position[1]]
        # Piece moves right
        if col > self._position[1]:
            check_position[1] += 1
            right = True

        # Piece moves left
        if col < self._position[1]:
            check_position[1] += - 1
            left = True

        # Piece moves forward
        if row > self._position[0]:
            check_position[0] += 1
            forward = True

        # Piece moves backwards
        if row < self._position[0]:
            check_position[0] += -1
            back = True

        # check whether every square in between is empty
        while board[check_position[0]][check_position[1]] == "E" and \
                check_position[0] < row and check_position[1] < col:
            if left:
                check_position[1] -= 1
            if right:
                check_position[1] += 1
            if forward:
                check_position[0] += 1
            if back:
                check_position[0] -= 1

        return board[check_position[0]][check_position[1]] == 'E'
