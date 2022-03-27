# import the pygame module, so you can use it
import heapq
import pickle
import pygame
import time
from random import random, randint

import numpy as np
from pygame.locals import *

# Creating some colors
BLUE = (0, 0, 255)
GRAYBLUE = (50, 120, 120)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# define directions
UP = 0
DOWN = 1
LEFT = 3
RIGHT = 2

# define indexes variations
v = [[-1, 0], [1, 0], [0, 1], [0, -1]]


class Map():
    def __init__(self, n=20, m=20):
        self.n = n
        self.m = m
        self.surface = np.zeros((self.n, self.m))

    def randomMap(self, fill=0.2):
        for i in range(self.n):
            for j in range(self.m):
                if random() <= fill:
                    self.surface[i][j] = 1

    def __str__(self):
        string = ""
        for i in range(self.n):
            for j in range(self.m):
                string = string + str(int(self.surface[i][j]))
            string = string + "\n"
        return string

    def saveMap(self, numFile="test.map"):
        with open(numFile, 'wb') as f:
            pickle.dump(self, f)
            f.close()

    def loadMap(self, numfile):
        with open(numfile, "rb") as f:
            dummy = pickle.load(f)
            self.n = dummy.n
            self.m = dummy.m
            self.surface = dummy.surface
            f.close()

    def image(self, colour=BLUE, background=WHITE):
        imagine = pygame.Surface((400, 400))
        brick = pygame.Surface((20, 20))
        brick.fill(BLUE)
        imagine.fill(WHITE)
        for i in range(self.n):
            for j in range(self.m):
                if (self.surface[i][j] == 1):
                    imagine.blit(brick, (j * 20, i * 20))

        return imagine


class Drone():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_path(self, path):
        self.path = path
        self.pos = 0

    def move(self, detectedMap):
        pressed_keys = pygame.key.get_pressed()
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

    def mapWithDrone(self, mapImage):
        mark = pygame.Surface((20, 20))
        mark.fill(GREEN)
        for i in range(0, self.pos):
            mapImage.blit(mark, (self.path[i][1] * 20, self.path[i][0] * 20))
        drona = pygame.image.load("drona.png")
        self.x, self.y = self.path[self.pos]
        mapImage.blit(drona, (self.y * 20, self.x * 20))
        self.pos += 1
        return mapImage


def manhattan_distance(initialX, initialY, finalX, finalY):
    return abs(initialX - finalX) + abs(initialY - finalY)

def h(initialX, initialY, finalX, finalY):
    return manhattan_distance(initialX, initialY, finalX, finalY)

def searchAStar(mapM, initialX, initialY, finalX, finalY):
    # TO DO
    # implement the search function and put it in controller
    # returns a list of moves as a list of pairs [x,y]
    g = 0
    n = mapM.n
    m = mapM.m
    visited = np.zeros((n, m))
    initial_c = h(initialX, initialY, finalX, finalY)
    queue = [(initial_c, initialX, initialY, 0)]
    result = []
    while len(queue):
        f, x, y, g = heapq.heappop(queue)
        if x == finalX and y == finalY:
            result.append((x, y))
            return result
        if visited[x][y] == 0:
            visited[x][y] = 1
            result.append((x, y))
            for i in range(4):
                tx = x + v[i][0]
                ty = y + v[i][1]
                if 0 <= tx < n and 0 <= ty < m and mapM.surface[tx][ty] == 0:
                    if visited[tx][ty] == 0:
                        c = g + h(tx, ty, finalX, finalY)
                        heapq.heappush(queue, (c, tx, ty, g + 1))


def searchGreedy(mapM, initialX, initialY, finalX, finalY):
    # TO DO
    # implement the search function and put it in controller
    # returns a list of moves as a list of pairs [x,y]
    g = 0
    n = mapM.n
    m = mapM.m
    visited = np.zeros((n, m))
    initial_c = h(initialX, initialY, finalX, finalY)
    queue = [(initial_c, initialX, initialY)]
    result = []
    while len(queue):
        f, x, y = heapq.heappop(queue)
        if x == finalX and y == finalY:
            result.append((x, y))
            return result
        if visited[x][y] == 0:
            visited[x][y] = 1
            result.append((x, y))
            for i in range(4):
                tx = x + v[i][0]
                ty = y + v[i][1]
                if 0 <= tx < n and 0 <= ty < m and mapM.surface[tx][ty] == 0:
                    if visited[tx][ty] == 0:
                        c = h(tx, ty, finalX, finalY)
                        heapq.heappush(queue, (c, tx, ty))


def dummysearch():
    # example of some path in test1.map from [5,7] to [7,11]
    return [[5, 7], [5, 8], [5, 9], [5, 10], [5, 11], [6, 11], [7, 11]]


def displayWithPath(image, path):
    mark = pygame.Surface((20, 20))
    mark.fill(GREEN)
    for move in path:
        image.blit(mark, (move[1] * 20, move[0] * 20))
        time.sleep(0.1)

    return image


# define a main function
def main():
    # we create the map
    m = Map()
    # m.randomMap()
    # m.saveMap("test2.map")
    m.loadMap("test1.map")

    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Path in simple environment")

    # we position the drone somewhere in the area
    x = randint(0, 19)
    y = randint(0, 19)

    # create drona
    d = Drone(x, y)

    # create a surface on screen that has the size of 400 x 480
    screen = pygame.display.set_mode((400, 400))
    screen.fill(WHITE)

    start = time.time()
    searchGreedy(m, 0, 4, 19, 19)
    end = time.time()
    print("Greedy: ", end - start)

    start = time.time()
    searchAStar(m, 0, 4, 19, 19)
    end = time.time()
    print("A*: ", end - start)


    # define a variable to control the main loop
    running = True
    path = searchGreedy(m, 0, 4, 19, 19)
    d.set_path(path)
    # # main loop
    i = 0
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

            # if event.type == KEYDOWN:
            #     d.move(m)  # this call will be erased

        time.sleep(0.5)
        screen.blit(d.mapWithDrone(m.image()), (0, 0))
        pygame.display.flip()

    # path = dummysearch()
    # path = searchAStar(m, 0, 4, 19, 19)
    # print(path)
    # screen.blit(displayWithPath(m.image(), path), (0, 0))

    pygame.display.flip()
    time.sleep(100)
    pygame.quit()


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
