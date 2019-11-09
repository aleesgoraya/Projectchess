from ChessPiece import ChessPiece


class Pawn(ChessPiece):
    """
    A class representing the Pawn piece in the chess class.
    """

    def get_valid_coordinates(self) -> list:
        """Return a list of valid moves that a Pawn has. Return an empty list
        if there is no valid moves.
        """
        ans = []
        current_position = self.get_position()
        current_row, current_col = current_position[0], current_position[1]

        if self.get_color() == "black":
            # check if it is in the starting position
            if current_row == 1 and current_col in [col for col in range(8)]:
                ans.append((current_row + 2, current_col))
                return ans
            current_row += 1
            if 0 <= current_row < 8:
                ans.append((current_row + 1, current_col))
            return ans

        if self.get_color() == "white":
            # check if it is in the starting position
            if current_row == 6 and current_col in [col for col in range(8)]:
                ans.append((current_row - 2, current_col))
                return ans
            current_row -= 1
            if 0 <= current_row < 8:
                ans.append((current_row - 1, current_col))
            return ans

