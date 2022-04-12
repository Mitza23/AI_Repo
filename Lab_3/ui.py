# -*- coding: utf-8 -*-
import random

import matplotlib.pyplot as plt
import numpy

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
#         b. run_once the solver
#         c. visualise the statistics
#         d. view the drone moving on a path
#              function gui.movingDrone(currentMap, path, speed, markseen)
#              ATENTION! the function doesn't check if the path passes trough walls

class gui:
    def __init__(self):
        self.controller = controller()
        self.population_size = 100
        self.individual_size = 10
        self.iterations = 200
        self.mutation_probability = 0.04
        self.crossover_probability = 0.8
        self.civilizations = 30

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

    def run_once(self):
        evaluations = self.controller.run(iterations=self.iterations, crossover_probability=self.crossover_probability,
                                          mutate_probability=self.mutation_probability)
        # print(evaluations[0], evaluations[-1])
        plt.plot(evaluations, color='magenta', marker='.', mfc='pink')  # plot the data
        # plt.xticks(range(0, len(evaluations) + 1, 1))  # set the tick frequency on x-axis

        plt.ylabel('total fitness')  # set the label for y axis
        plt.xlabel('iteration')  # set the label for x-axis
        plt.title("Evolution")  # set the title of the graph
        plt.show()  # display the graph
        # return numpy.average(evaluations)
        return evaluations

    def run_more(self):
        averages = []
        for i in range(self.civilizations):
            seed = random.randint(0, 10000)
            random.seed(seed)
            ui = gui()
            averages.append(ui.run_once())
        print("Average: " + numpy.average(averages))
        print("Deviation: " + numpy.std(averages))


if __name__ == '__main__':
    ui = gui()
    ui.run_more()
    exit(0)
