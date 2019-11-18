import pygame
import random

purple = (128, 0, 128)
pink = (255, 170, 255)
light_blue = (82, 200, 220)
red = (255, 0, 0)
margin_w = 77
margin_h = 66


def next_colour(colour):
    rand1 = random.randint(100, 255)
    rand2 = random.randint(100, 255)
    rand3 = random.randint(100, 255)

    return rand1, rand2, rand3


def create_board():

    screen_width = 709
    screen_height = 620
    colour = pink
    screen = pygame.display.set_mode((screen_width, screen_height))
    for row in range(8):
        for col in range(8):
            pygame.draw.rect(screen, colour, (col*margin_w + (col+1)*10, row*margin_h+(row+1)*10, margin_w, margin_h))
            colour = next_colour(colour)
    return screen

def add_pieces(screen):
    queen = pygame.image.load("queen_black.png")
    queen = pygame.transform.scale(queen, (margin_w, margin_h))
    screen.blit(queen, (margin_w*3+(10*4), 10))

def main():

    screen = create_board()
    pygame.display.set_caption("Chess???? CHESSSS!!!!!!")
    add_pieces(screen)
    run = True
    while run:
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()


if __name__ == '__main__':
    main()
