import pygame

purple = (128, 0, 128)
pink = (255, 170, 255)
light_blue = (82, 200, 220)

def next_colour(colour):

    if colour == purple:
        return pink
    elif colour == pink:
        return light_blue
    else:
        return purple



def create_board():

    margin_w = 800/11
    margin_h = 650/11
    screen_width = 670
    screen_height = 560
    colour = pink
    screen = pygame.display.set_mode((screen_width, screen_height))
    for row in range(8):
        for col in range(8):
            pygame.draw.rect(screen, colour, (col*margin_w + (col+1)*10, row*margin_h+(row+1)*10, margin_w, margin_h))
            colour = next_colour(colour)
    return screen



def main():

    screen = create_board()
    pygame.display.set_caption("Chess???? CHESSSS!!!!!!")
    pygame.display.flip()

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()


if __name__ == '__main__':
    main()
