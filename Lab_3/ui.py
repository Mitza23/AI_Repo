# -*- coding: utf-8 -*-

from controller import controller
# imports


# create a menu
#   1. map options:
#         a. create random map
#         b. load a map
#         c. save a map
#         d visualise map
#   2. EA options:
#         a. parameters setup
#         b. run the solver
#         c. visualise the statistics
#         d. view the drone moving on a path
#              function gui.movingDrone(currentMap, path, speed, markseen)
#              ATENTION! the function doesn't check if the path passes trough walls

class gui:
    def __init__(self):
        self.controller = controller()
        self.population_size = 100
        self.individual_size = 10
        self.epochs = 1000
        self.mutation_probability = 0.04
        self.crossover_probability = 0.8

    def print_menu(self):
        print("1. Map options")
        print("2. EA Options")
        print("3. Run")

    def print_map_options(self):
        print("1. random map")
        print("2. load map")
        print("3. save map")
        print("4. visualise map")

    def print_ea_options(self):
        print("1. Population size")
        print("2. Individual size")
        print("2. Epochs")
