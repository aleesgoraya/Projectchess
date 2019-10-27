from abc import ABC, abstractclassmethod


class ChessPieces(ABC):

    def __init__(self, color):
        self.color = color
        super().__init__()

    def return_color(self):
        return self.color
