import pygame

# Creating some colors
from pygame import KEYDOWN

from Controller.Controller import Controller

BLUE = (0, 0, 255)
GRAYBLUE = (50, 120, 120)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def main():
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("drone exploration")

    screen = pygame.display.set_mode((800, 400))
    screen.fill(WHITE)
    screen.blit(e.image(), (0, 0))

    controller = Controller()

    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            if event.type == KEYDOWN:
                # use this function instead of move
                controller.move_drone()
                # d.move(m)
        screen.blit(m.image(d.x, d.y), (400, 0))
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()