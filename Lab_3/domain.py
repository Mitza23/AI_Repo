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
        self.surface[10][10] = 0

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
        prev = self.value
        while prev == self.value:
            self.value = randint(0, 3)

    def __str__(self) -> str:
        return str(self.value)


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
        self.__f = 0
        viz = np.zeros((self._map.n, self._map.m))
        x = self._sx
        y = self._sy
        viz[x][y] = 1
        r = 1
        for g in self.__x:
            x += utils.v[g.value][0]
            y += utils.v[g.value][1]
            if 0 <= x < self._map.n and 0 <= y < self._map.m:
                if self._map.surface[x][y] == 1:
                    return 0
                if viz[x][y] == 0:
                    r += 1
                viz[x][y] = 1
            else:
                return 0
        self.__f = r
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

    def __str__(self) -> str:
        result = str(self.__f) + ":  "
        for e in self.__x:
            result += str(e) + " "
        return result


class Population():
    def __init__(self, populationSize=0, individualSize=0, map=None, x=10, y=10):
        if map is None:
            map = Map()
        self.__populationSize = populationSize
        self.__v = [Individual(individualSize, map, x, y) for i in range(populationSize)]

    def get_list(self):
        return self.__v

    def evaluate(self):
        # evaluates the population
        r = 0
        for x in self.__v:
            r += x.fitness()
        return r

    def selection(self, k=0):
        # perform a selection of k individuals from the population
        # and returns that selection
        self.__v.sort(key=lambda a: a.fitness(), reverse=False)
        print(self.__v)
        # selected_indexes = []
        selected_individuals = []
        # for i in range(k):
        #     pos = randint(0, k - 1)
        #     while pos in selected_indexes:
        #         pos = randint(0, k - 1)
        #     selected_individuals.append(self.__v[pos])
        i = len(self.__v) - 1
        while i >= 0 and k >= 0:
            selected_individuals.append(self.__v[i])
            i -= 1
            k -= 1
        return selected_individuals

    def next_generation(self):
        # TODO implement logic for selection, crossover and mutation
        pass


if __name__ == '__main__':
    population = Population(10, 4)
    for e in population.selection(5):
        print(e)
