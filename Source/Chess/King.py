from Chess.ChessPiece import ChessPiece


class King(ChessPiece):
    """
    A class representing a King piece in the chess game on the chess board.
    A king can move in a 3*3 square centred by itself. It is the most important
    piece in the chess game. If it is checkmated, then game is over.
    """

    def get_valid_coordinates(self) -> list:
        """Return a list of valid moves that the King has.
        """
        ans = []
        current_position = self.get_position()
        current_row, current_col = current_position[0], current_position[1]

        for d_row in range(-1, 2):
            for d_col in range(-1, 2):
                while 0 <= current_row < 8 and 0 <= current_col < 8:
                    current_row += d_row
                    current_col += d_col
                    ans.append((current_row, current_col))

        # this is not a valid move
        ans.remove((current_position[0], current_position[1]))
        return ans

