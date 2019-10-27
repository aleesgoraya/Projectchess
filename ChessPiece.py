from abc import ABC, abstractclassmethod


class ChessPiece(ABC):

    # position is an array containing row and col e.g [0,1] 0 is row and 1 is col
    def __init__(self, color, position):
        self.color = color
        self.position = position
        super().__init__()

    def return_color(self):
        return self.color

    def return_position(self):
        return self.position
