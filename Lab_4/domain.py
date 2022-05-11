# -*- coding: utf-8 -*-
import random
from random import *
from random import shuffle

import numpy as np
# the glass gene can be replaced with int or float, or other types
# depending on your problem's representation
import numpy.random
from matplotlib import pyplot as plt

import utils


class Drone:
    def __init__(self, x=0, y=0, energy=0):
        self.x = x
        self.y = y
        self.energy = energy


class Map:
    def __init__(self, n=20, m=20):
        self.n = n
        self.m = m
        self.surface = np.zeros((self.n, self.m))
        self.sensors = []
        self.sensor_count = 0

    def randomMap(self, fill=0.2, x=10, y=10):
        for i in range(self.n):
            for j in range(self.m):
                if random() <= fill:
                    self.surface[i][j] = 1
                else:
                    self.surface[i][j] = 0
        self.surface[x][y] = 0

    def __str__(self):
        string = ""
        for i in range(self.n):
            for j in range(self.m):
                string = string + str(int(self.surface[i][j]))
            string = string + "\n"
        return string

    def set_cell(self, i, j, val):
        self.surface[i][j] = val

    def add_sensor(self, i, j):
        self.sensors.append((i, j))

    def compute_charge(self, sensor, charge):
        r = 0
        pos = 1
        sensor = self.sensors[sensor]
        x = sensor[0]
        y = sensor[1]
        # UP
        while pos <= charge:
            if (x - pos) >= 0 and self.surface[x - pos][y] == 0:
                r += 1
            else:
                break

        # RIGHT
        while pos <= charge:
            if (y + pos) < self.m and self.surface[x][y + pos] == 0:
                r += 1
            else:
                break

        # DOWN
        while pos <= charge:
            if (x + pos) < self.n and self.surface[x + pos][y] == 0:
                r += 1
            else:
                break

        # LEFT
        while pos <= charge:
            if (y - pos) >= 0 and self.surface[x][y - pos] == 0:
                r += 1
            else:
                break

        return r


if __name__ == '__main__':
    pass
