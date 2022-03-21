from random import randint

from Model.Drone import Drone
from Model.Environment import Environment


class Controller:
    def __init__(self):
        self.environment = Environment()
        self.environment.load_environment("../test2.map")
        x = randint(0, self.environment.width)
        y = randint(0, self.environment.height)
        while self.environment.surface[x][y] == 1:
            x = randint(0, self.environment.width)
            y = randint(0, self.environment.height)
        self.drone = Drone(x, y, self.environment)

    def move_drone(self):
        self.drone.moveDFS()

