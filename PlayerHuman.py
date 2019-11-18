import Player


class PlayerHuman(Player):
    """This is a subclass of Player class that represents the
    Human Player.
    """

    def __init__(self, chess, color):
        super().__init__(chess, color)

    @staticmethod
    def get_move() -> tuple:
        """Get the move from the console.
        """
        try:
            row = int(input("row position: "))
            col = int(input("col position: "))
        except InvalidInputException:
            print("invalid input")
        else:
            move_position = (row, col)
            return move_position


class InvalidInputException:
    """A class representing InvalidInputException.
    """
    pass
