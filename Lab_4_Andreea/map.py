import pickle
from random import *
import numpy as np
import queue
from utils import *
from queue import PriorityQueue


class Map:
    def __init__(self, n=20, m=20, x=0, y=19):
        self.n = n
        self.m = m
        self.x = x
        self.y = y
        self.surface = np.zeros((self.n, self.m))
        self.nr_sensors = 0
        self.sensors = []
        self.loadMap()
        # self.randomMap()
        # self.saveMap()
        self.sensors_paths = []
        self.reached = []

    def set_sensors_paths(self, paths):
        self.sensors_paths = paths

    def randomMap(self, fill=0.2, sensors=0.04):
        sum = fill + sensors
        for i in range(self.n):
            for j in range(self.m):
                nr = random()
                if nr < sensors:
                    self.surface[i][j] = 2
                if sensors < nr < sum:
                    self.surface[i][j] = 1

    def get_nr_sensors(self):
        if self.nr_sensors != 0:
            return self.nr_sensors
        for i in range(self.n):
            for j in range(self.m):
                if self.surface[i][j] == 2:
                    self.nr_sensors += 1
        return self.nr_sensors

    def get_sensors(self):
        if not self.sensors:
            for i in range(self.n):
                for j in range(self.m):
                    if self.surface[i][j] == 2:
                        self.sensors.append((i, j))
        self.nr_sensors = len(self.sensors)
        return self.sensors

    def loadMap(self):
        with open("map.map", "rb") as file:
            self.surface = pickle.load(file)
            file.close()

    def saveMap(self):
        with open("map2.map", "wb") as file:
            pickle.dump(self.surface, file)
            file.close()

    def positionDrone(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        string = ""
        for i in range(self.n):
            for j in range(self.m):
                string = string + str(int(self.surface[i][j]))
            string = string + "\n"
        return string

