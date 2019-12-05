import pygame
import random

from Chess.Chess import Chess

pygame.init()

purple = (128, 0, 128)
pink = (255, 170, 255)
light_blue = (82, 200, 220)
red = (255, 0, 0)
white = (255, 255, 255)
green = (0, 102, 0)
margin_w = 77
margin_h = 66
screen_width = 900
screen_height = 618


def next_colour(colour):
    """Gives out 3 integers each randomly selected. This
    is used to randomize color.
    """
    rand1 = random.randint(100, 255)
    rand2 = random.randint(100, 255)
    rand3 = random.randint(100, 255)

    return rand1, rand2, rand3


def create_board():
    """Creates an 8x8 board.
    """
    colour = pink
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill(green)
    for row in range(8):
        for col in range(8):
            pygame.draw.rect(screen, colour,
                             (col * margin_w + (col + 1) * 10, row * margin_h + (row + 1) * 10, margin_w, margin_h))
            colour = next_colour(colour)

    colour = (230, 230, 230)

    # Restart Button
    pygame.draw.rect(screen, colour,
                     (720, 50, 150, 50))

    # Quit Button
    pygame.draw.rect(screen, colour,
                     (720, 130, 150, 50))

    font = pygame.font.Font(None, 45)
    text = font.render("Restart", True, (0, 0, 0))
    screen.blit(text, [730, 60])

    text = font.render("Quit", True, (0, 0, 0))
    screen.blit(text, [750, 140])

    return screen


def add_pieces(screen):
    """Adds chess pieces to the 8x8 board.
    """
    queen_b = pygame.image.load("queen_black.png")
    queen_b = pygame.transform.scale(queen_b, (margin_w, margin_h))

    pawn_b = pygame.image.load("pawn_black.png")
    pawn_b = pygame.transform.scale(pawn_b, (margin_w, margin_h))

    rook_b = pygame.image.load("rook_black.png")
    rook_b = pygame.transform.scale(rook_b, (margin_w, margin_h))

    knight_b = pygame.image.load("knight_black.png")
    knight_b = pygame.transform.scale(knight_b, (margin_w, margin_h))

    king_b = pygame.image.load("king_black.png")
    king_b = pygame.transform.scale(king_b, (margin_w, margin_h))

    bishop_b = pygame.image.load("bishop_black.png")
    bishop_b = pygame.transform.scale(bishop_b, (margin_w, margin_h))

    for i in range(8):  # black pawns
        screen.blit(pawn_b, (margin_w * i + 10 * (i + 1), margin_h + 20))

    for i in range(8):  # Other black pieces
        if i == 0:
            piece = rook_b
        elif i == 1:
            piece = knight_b
        elif i == 2:
            piece = bishop_b
        elif i == 3:
            piece = king_b
        elif i == 4:
            piece = queen_b
        elif i == 5:
            piece = bishop_b
        elif i == 6:
            piece = knight_b
        elif i == 7:
            piece = rook_b
        screen.blit(piece, (margin_w * i + 10 * (i + 1), 10))

        queen_w = pygame.image.load("queen_white.png")
        queen_w = pygame.transform.scale(queen_w, (margin_w, margin_h))

        pawn_w = pygame.image.load("pawn_white.png")
        pawn_w = pygame.transform.scale(pawn_w, (margin_w, margin_h))

        rook_w = pygame.image.load("rook_white.png")
        rook_w = pygame.transform.scale(rook_w, (margin_w, margin_h))

        knight_w = pygame.image.load("knight_white.png")
        knight_w = pygame.transform.scale(knight_w, (margin_w, margin_h))

        king_w = pygame.image.load("king_white.png")
        king_w = pygame.transform.scale(king_w, (margin_w, margin_h))

        bishop_w = pygame.image.load("bishop_white.png")
        bishop_w = pygame.transform.scale(bishop_w, (margin_w, margin_h))

        for i in range(8):  # white pawns
            screen.blit(pawn_w, (margin_w * i + 10 * (i + 1), screen_height - (margin_h * 2) - 20))
        for i in range(8):  # Other white pieces
            if i == 0:
                piece = rook_w
            elif i == 1:
                piece = knight_w
            elif i == 2:
                piece = bishop_w
            elif i == 3:
                piece = king_w
            elif i == 4:
                piece = queen_w
            elif i == 5:
                piece = bishop_w
            elif i == 6:
                piece = knight_w
            elif i == 7:
                piece = rook_w
            screen.blit(piece, (margin_w * i + 10 * (i + 1), screen_height - margin_h - 10))


def main():
    pygame.init()
    screen = create_board()
    pygame.display.set_caption("CHESS")
    add_pieces(screen)
    run = True
    chess = Chess()
    selected = False
    selectedPiece = 0

    while run:

        pygame.display.flip()

        # Check for mouse clicks on buttons
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if 720 < mouse_pos[0] < 870:
                    if 130 < mouse_pos[1] < 180:
                        run = False
                        quit()

                for row in range(8):
                    for col in range(8):
                        start_button_x = margin_w * col + 10 * (col + 1)
                        end_button_x = margin_w * col + 10 * (col + 1) + 77
                        start_button_y = margin_h * row + 10 * (row + 1)
                        end_button_y = row * margin_h + 10 * (row + 1) + margin_h
                        if start_button_x < mouse_pos[0] < end_button_x:
                            if start_button_y < mouse_pos[1] < end_button_y:

                                print(chess.get_piece(row, col))
                                if selected:
                                    chess.change_turn()
                                    print(selected_piece.get_position())

                                if chess.get_piece(row, col) == "" and selected:
                                    selected = False

                                elif chess.get_piece(row, col) == "":
                                    print("Invalid move")

                                elif chess.get_current_turn() == chess.get_piece(row, col).get_color():
                                    selected_piece = chess.get_piece(row, col)
                                    selected = True

    pygame.quit()


if __name__ == '__main__':
    main()
