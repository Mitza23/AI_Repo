import pickle
from random import random
import pygame
import numpy as np

# Creating some colors
BLUE = (0, 0, 255)
GRAYBLUE = (50, 120, 120)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Environment:
    def __init__(self, n=20, m=20):
        self.__n = n
        self.__m = m
        self.__surface = np.zeros((self.__n, self.__m))

    @property
    def width(self):
        return self.__n

    @property
    def height(self):
        return self.__m

    @property
    def surface(self):
        return self.__surface

    # def get_width(self):
    #     return self.__n
    #
    # def get_height(self):
    #     return self.__m
    #
    # def get_surface(self):
    #     return self.__surface

    def random_map(self, fill=0.2):
        for i in range(self.__n):
            for j in range(self.__m):
                if random() <= fill:
                    self.__surface[i][j] = 1

    def __str__(self):
        string = ""
        for i in range(self.__n):
            for j in range(self.__m):
                string = string + str(int(self.__surface[i][j]))
            string = string + "\n"
        return string

    def save_environment(self, numFile):
        with open(numFile, 'wb') as f:
            pickle.dump(self, f)
            f.close()

    def load_environment(self, numfile):
        with open(numfile, "rb") as f:
            dummy = pickle.load(f)
            self.__n = dummy.__n
            self.__m = dummy.__m
            self.__surface = dummy.__surface
            f.close()

    def image(self, colour=BLUE, background=WHITE):
        imagine = pygame.Surface((420, 420))
        brick = pygame.Surface((20, 20))
        brick.fill(BLUE)
        imagine.fill(WHITE)
        for i in range(self.__n):
            for j in range(self.__m):
                if self.__surface[i][j] == 1:
                    imagine.blit(brick, (j * 20, i * 20))
        return imagine
