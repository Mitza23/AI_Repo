import time

import pygame

from Controller.controller import Controller
from Model.map import Map

BLUE = (0, 0, 255)
GRAYBLUE = (50, 120, 120)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class View:
    def __init__(self):
        self.controller = Controller()
        self.screen = None

    def displayWithPath(self, image, path):
        mark = pygame.Surface((20, 20))
        mark.fill(GREEN)
        for move in path:
            image.blit(mark, (move[1] * 20, move[0] * 20))
            time.sleep(0.1)

        return image

    def loadEnvironment(self):
        self.controller.map = Map()
        # m.randomMap()
        # m.saveMap("test2.map")
        self.controller.map.loadMap("test1.map")

        # initialize the pygame module
        pygame.init()
        # load and set the logo
        logo = pygame.image.load("logo32x32.png")
        pygame.display.set_icon(logo)
        pygame.display.set_caption("Path in simple environment")

        self.screen = pygame.display.set_mode((400, 400))
        self.screen.fill(WHITE)

    def a_star_search(self, sx, sy, fx, fy):
        path = self.controller.searchAStar(sx, sy, fx, fy)
        self.screen.blit(self.displayWithPath(self.controller.map.image(), path), (0, 0))

    def greedy_search(self, sx, sy, fx, fy):
        path = self.controller.searchGreedy(sx, sy, fx, fy)
        self.screen.blit(self.displayWithPath(self.controller.map.image(), path), (0, 0))