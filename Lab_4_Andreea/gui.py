# -*- coding: utf-8 -*-

from pygame.locals import *
import pygame, time
from utils import *
from map import *


def initPyGame(dimension):
    # init the pygame
    pygame.init()
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("ACO")

    # create a surface on screen that has the size of 800 x 480
    screen = pygame.display.set_mode(dimension)
    screen.fill(WHITE)
    return screen


def closePyGame():
    # closes the pygame
    running = True
    # loop for events
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
    pygame.quit()


def movingDrone(currentMap, path, speed=0.1, markSeen=True):
    # animation of a drone on a path
    screen = initPyGame((currentMap.n * 20, currentMap.m * 20))

    drona = pygame.image.load("drona.png")
    screen.blit(drona, (0, 0))

    for i in range(len(path)):
        screen.blit(image(currentMap), (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if markSeen:
            brick = pygame.Surface((20, 20))
            brick.fill(GREEN)
            for j in range(i + 1):
                for var in directions:
                    x = path[j][0]
                    y = path[j][1]
                    e = path[j][2]
                    while e > 0 and (0 <= x + var[0] < currentMap.n and 0 <= y + var[1] < currentMap.m and currentMap.surface[x + var[0]][y + var[1]] == 0):
                        e -= 1
                        x = x + var[0]
                        y = y + var[1]
                        screen.blit(brick, (y * 20, x * 20))
        screen.blit(drona, (path[i][1] * 20, path[i][0] * 20))
        pygame.display.flip()
        time.sleep(0.01 * speed)
    closePyGame()


def image(currentMap, colour=BLUE, background=WHITE):
    imagine = pygame.Surface((currentMap.n * 20, currentMap.m * 20))
    brick = pygame.Surface((20, 20))
    brick.fill(colour)
    sensor = pygame.Surface((20, 20))
    sensor.fill(RED)
    imagine.fill(background)
    for i in range(currentMap.n):
        for j in range(currentMap.m):
            if (currentMap.surface[i][j] == 1):
                imagine.blit(brick, (j * 20, i * 20))
            if (currentMap.surface[i][j] == 2):
                imagine.blit(sensor, (j * 20, i * 20))

    return imagine


def visualiseMap(map):
    drone_pos = map.x, map.y
    screen = initPyGame((map.n * 20, map.m * 20))
    screen.blit(image(map), (0, 0))
    drone = pygame.image.load("drona.png")
    screen.blit(drone, (drone_pos[1] * 20, drone_pos[0] * 20))
    pygame.display.flip()
    closePyGame()
