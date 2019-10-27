from abc import ABC, abstractclassmethod


class ChessPiece(ABC):

    def __init__(self, color,position):
        self.color = color
        self.position = position
        super().__init__()

    def return_color(self):
        return self.color

    def return_position(self):
        return self.position
