import heapq

import numpy as np

from Model.drone import Drone
from Model.map import Map


class Controller:
    def __init__(self):
        self.map = Map()
        self.drone = Drone()

    @staticmethod
    def manhattan_distance(initialX, initialY, finalX, finalY):
        return abs(initialX - finalX) + abs(initialY - finalY)

    @staticmethod
    def h(initialX, initialY, finalX, finalY):
        return Controller.manhattan_distance(initialX, initialY, finalX, finalY)

    def searchAStar(self, initialX, initialY, finalX, finalY):
        # TO DO
        # implement the search function and put it in controller
        # returns a list of moves as a list of pairs [x,y]
        v = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        g = 0
        n = self.map.n
        m = self.map.m
        visited = np.zeros((n, m))
        initial_c = Controller.h(initialX, initialY, finalX, finalY)
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
                    if 0 <= tx < n and 0 <= ty < m and self.map.surface[tx][ty] == 0:
                        if visited[tx][ty] == 0:
                            c = g + Controller.h(tx, ty, finalX, finalY)
                            heapq.heappush(queue, (c, tx, ty, g + 1))

    def searchGreedy(self, initialX, initialY, finalX, finalY):
        # TO DO
        # implement the search function and put it in controller
        # returns a list of moves as a list of pairs [x,y]
        v = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        g = 0
        n = self.map.n
        m = self.map.m
        visited = np.zeros((n, m))
        initial_c = Controller.h(initialX, initialY, finalX, finalY)
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
                    if 0 <= tx < n and 0 <= ty < m and self.map.surface[tx][ty] == 0:
                        if visited[tx][ty] == 0:
                            c = Controller.h(tx, ty, finalX, finalY)
                            heapq.heappush(queue, (c, tx, ty))

    @staticmethod
    def dummysearch():
        # example of some path in test1.map from [5,7] to [7,11]
        return [[5, 7], [5, 8], [5, 9], [5, 10], [5, 11], [6, 11], [7, 11]]

    def set_path(self, path):
        self.drone.set_path(path)

    def map_with_move(self):
        return self.drone.mapWithDrone(self.map.image())