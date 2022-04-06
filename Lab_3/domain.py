# -*- coding: utf-8 -*-

from random import *

import numpy as np


# the glass gene can be replaced with int or float, or other types
# depending on your problem's representation
import utils


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


class gene:
    def __init__(self):
        self.value = randint(0, 3)

    def mutate(self):
        self.value = randint(0, 3)


class Individual:
    def __init__(self, size=0, map=Map(), x=0, y=0):
        self.__size = size
        self.__x = [gene() for i in range(self.__size)]
        self.__f = None
        self._sx = x
        self._sy = y
        self._map = map

    def fitness(self):
        # compute the fitness for the individual
        # and save it in self.__f
        viz = np.zeros((self._map.n, self._map.m))
        x = self._sx
        y = self._sy
        viz[x][y] = 1
        r = 1
        for g in self.__x:
            x += utils.v[g.value][0]
            y += utils.v[g.value][1]
            if self._map.surface[x][y] == 1:
                return 0
            if viz[x][y] == 0:
                r += 1
            viz[x][y] = 1
        return r

    def mutate(self, mutateProbability=0.04):
        if random() < mutateProbability:
            pos = randint(0, self.__size)
            self.__x[pos].mutate()
            # perform a mutation with respect to the representation

    def crossover(self, otherParent, crossoverProbability=0.8):
        offspring1, offspring2 = Individual(self.__size), Individual(self.__size)
        if random() < crossoverProbability:
            for i in range(self.__size // 2):
                offspring1.__x[i] = self.__x[i]
                offspring2.__x[i] = otherParent.__x[i]
            for i in range(self.__size // 2 + 1, self.__size - 1):
                offspring1.__x[i] = otherParent.__x[i]
                offspring2.__x[i] = self.__x[i]
            # perform the crossover between the self and the otherParent 

        return offspring1, offspring2


class Population():
    def __init__(self, populationSize=0, individualSize=0):
        self.__populationSize = populationSize
        self.__v = [Individual(individualSize) for x in range(populationSize)]

    def evaluate(self):
        # evaluates the population
        r = 0
        for x in self.__v:
            r += x.fitness()
        return r

    def selection(self, k=0):
        # perform a selection of k individuals from the population
        # and returns that selection
        selected_indexes = []
        selected_individuals = []
        for i in range(k):
            pos = randint(0, k - 1)
            while pos in selected_indexes:
                pos = randint(0, k - 1)
            selected_individuals.append(self.__v[pos])
        return selected_individuals
