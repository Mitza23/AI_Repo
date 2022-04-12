# -*- coding: utf-8 -*-
import random

import matplotlib.pyplot as plt

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
        self.iterations = 100
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

    def run(self):
        evaluations = self.controller.run(iterations=self.iterations, crossover_probability=self.crossover_probability,
                                          mutate_probability=self.mutation_probability)
        plt.plot(evaluations, color='magenta', marker='o', mfc='pink')  # plot the data
        plt.xticks(range(0, len(evaluations) + 1, 1))  # set the tick frequency on x-axis

        plt.ylabel('data')  # set the label for y axis
        plt.xlabel('index')  # set the label for x-axis
        plt.title("Plotting a list")  # set the title of the graph
        plt.show()  # display the graph


if __name__ == '__main__':
    random.seed(10)
    ui = gui()
    ui.run()
