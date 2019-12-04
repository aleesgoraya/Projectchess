from Chess.ChessPiece import ChessPiece


class Rook(ChessPiece):
    """A class representing the Rook piece in the chess game.
    """

    def get_valid_coordinates(self) -> list:
        """Return a list of valid moves that the Rook has.
        """
        ans = []

        for d_row in [-1, 1]:
            current_position = self.get_position()
            current_row, current_col = current_position[0], current_position[1]
            while 0 <= current_row < 8:
                current_row += d_row
                ans.append((current_row, current_col))

        for d_col in [-1, 1]:
            current_position = self.get_position()
            current_row, current_col = current_position[0], current_position[1]
            while 0 <= current_col < 8:
                current_col += d_col
                ans.append((current_row, current_col))

        return ans











