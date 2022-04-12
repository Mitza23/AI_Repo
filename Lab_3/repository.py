# -*- coding: utf-8 -*-

from domain import *


class repository():
    def __init__(self):
        self.__populations = []
        self.cmap = Map()

    def createPopulation(self, population_size=100, individual_size=10, map=None, x=10, y=10):
        self.__populations.append(Population(population_size, individual_size, map, x, y))

    def get_first_population(self):
        return self.__populations[0]

    def get_populations(self):
        return self.__populations
    # TO DO : add the other components for the repository: 
    #    load and save from file, etc
