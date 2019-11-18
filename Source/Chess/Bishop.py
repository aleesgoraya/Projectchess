from ChessPiece import ChessPiece


class Bishop(ChessPiece):
    """
    A class representing Bishop piece in the chess game. It can move in a
    straight line diagonally.
    """

    def get_valid_coordinates(self) -> list:
        """Return a list of valid moves that the Bishop have.
        """
        ans = []
        current_position = self.get_position()
        current_row, current_col = current_position[0], current_position[1]

        for d_row in [-1, 1]:
            for d_col in [-1, 1]:
                while 0 <= current_row < 8 and 0 <= current_col < 8:
                    current_row += d_row
                    current_col += d_col
                    ans.append((current_row, current_col))

        # this is not a valid move
        ans.remove((current_position[0], current_position[1]))
        return ans











