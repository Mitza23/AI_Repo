import numpy as np
import pygame
from pygame import K_UP, K_DOWN, K_LEFT, K_RIGHT

import Environment

# define directions
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# Creating some colors
BLUE = (0, 0, 255)
GRAYBLUE = (50, 120, 120)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Drone:
    def __init__(self, x, y, environment):
        self.__n = None
        self.x = x
        self.y = y
        self.environment = environment
        self.detected_map = np.ones((environment.width, environment.height))
        self.visited = np.zeros((environment.width, environment.height))
        self.stack = [(x, y)]

    def read_udm_sensors(self):
        readings = [0, 0, 0, 0]
        x = self.x
        y = self.y
        self.detected_map[x][y] = 0
        # UP 
        xf = x - 1
        while (xf >= 0) and (self.environment.surface[xf][y] == 0):
            self.detected_map[xf][y] = 0
            xf = xf - 1
            readings[UP] = readings[UP] + 1
        # RIGHT
        yf = y + 1
        while (yf < self.environment.height) and (self.environment.surface[x][yf] == 0):
            self.detected_map[x][yf] = 0
            yf = yf + 1
            readings[RIGHT] = readings[RIGHT] + 1
        # DOWN
        xf = x + 1
        while (xf < self.environment.width) and (self.environment.surface[xf][y] == 0):
            self.detected_map[xf][y] = 0
            xf = xf + 1
            readings[DOWN] = readings[DOWN] + 1
        # LEFT
        yf = y - 1
        while (yf >= 0) and (self.environment.surface[x][yf] == 0):
            self.detected_map[x][yf] = 0
            yf = yf - 1
            readings[LEFT] = readings[LEFT] + 1

    def image(self, x, y):
        imagine = pygame.Surface((420, 420))
        brick = pygame.Surface((20, 20))
        empty = pygame.Surface((20, 20))
        empty.fill(WHITE)
        brick.fill(BLACK)
        imagine.fill(GRAYBLUE)

        for i in range(self.environment.width):
            for j in range(self.environment.height):
                if self.detected_map[i][j] == 1:
                    imagine.blit(brick, (j * 20, i * 20))
                elif self.detected_map[i][j] == 0:
                    imagine.blit(empty, (j * 20, i * 20))

        drona = pygame.image.load("drona.png")
        imagine.blit(drona, (y * 20, x * 20))
        return imagine

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        detectedMap = self.detected_map
        if self.x > 0:
            if pressed_keys[K_UP] and detectedMap.surface[self.x - 1][self.y] == 0:
                self.x = self.x - 1
        if self.x < 19:
            if pressed_keys[K_DOWN] and detectedMap.surface[self.x + 1][self.y] == 0:
                self.x = self.x + 1

        if self.y > 0:
            if pressed_keys[K_LEFT] and detectedMap.surface[self.x][self.y - 1] == 0:
                self.y = self.y - 1
        if self.y < 19:
            if pressed_keys[K_RIGHT] and detectedMap.surface[self.x][self.y + 1] == 0:
                self.y = self.y + 1

    def recursive_dfs(self):
        stack = self.stack
        if len(stack) > 0:
            (x, y) = stack.pop()
            self.x = x
            self.y = y
            self.visited[x][y] = 1
            self.read_udm_sensors()
            detected_map = self.detected_map
            # UP
            if x - 1 >= 0:
                if detected_map[x - 1][y] == 0 and self.visited[x - 1][y] == 0:
                    stack.append((x - 1, y))
            # LEFT
            if y - 1 >= 0:
                if detected_map[x][y - 1] == 0 and self.visited[x][y - 1] == 0:
                    stack.append((x, y - 1))
            # DOWN
            if x + 1 < 20:
                if detected_map[x + 1][y] == 0 and self.visited[x + 1][y] == 0:
                    stack.append((x + 1, y))
            # RIGHT
            if y + 1 < 20:
                if detected_map[x][y + 1] == 0 and self.visited[x][y + 1] == 0:
                    stack.append((x, y + 1))

    def moveDFS(self):
        self.recursive_dfs()
        print("move: ", self.stack)
