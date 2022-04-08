# -*- coding: utf-8 -*-

from random import *

import numpy as np
# the glass gene can be replaced with int or float, or other types
# depending on your problem's representation
import numpy.random

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
    def __init__(self, size=0, map=None, x=0, y=0):
        if map is None:
            map = Map()
        self.__size = size
        self.__x = [gene() for i in range(self.__size)]
        self.__f = None
        self._sx = x
        self._sy = y
        self._map = map

    def get_fitness(self):
        if self.__f is None:
            self.fitness()
        return self.__f

    def get_genes(self):
        return self.__x

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
                    self.__f = r
                    return r
                if viz[x][y] == 0:
                    r += 1
                viz[x][y] = 1
            else:
                self.__f = r
                return r
        self.__f = r
        return r

    def mutate(self, mutateProbability=0.04):
        if random() < mutateProbability:
            pos = randint(0, self.__size - 1)
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


class Population:
    def __init__(self, populationSize=0, individualSize=0, map=None, x=10, y=10):
        if map is None:
            map = Map()
        self.__map = map
        self.__x = x
        self.__y = y
        self.__populationSize = populationSize
        self.__individual_size = individualSize
        self.__v = [Individual(individualSize, map, x, y) for i in range(populationSize)]
        for individual in self.__v:
            individual.fitness()

    def get_list(self) -> list[Individual]:
        return self.__v

    def set_list(self, new_list):
        self.__v = new_list

    def evaluate(self):
        # evaluates the population
        r = 0
        for x in self.__v:
            if x.get_fitness() is None:
                x.fitness()
            r += x.get_fitness()
        return r

    def selection(self, k=0) -> list[Individual]:
        # perform a selection of k individuals from the population
        # and returns that selection
        # self.__v.sort(key=lambda a: a.fitness(), reverse=False)
        weights = []
        total_fintnss = 0
        for individual in self.__v:
            total_fintnss += individual.get_fitness()
            weights.append(individual.get_fitness())
        weights[:] = [w / total_fintnss for w in weights]
        selected_individuals = list(numpy.random.choice(self.get_list(), k, p=weights))
        return selected_individuals

    def next_generation(self):
        selected_parents = self.selection(self.__populationSize // 2)
        new_generation = selected_parents[:]
        for i in range(0, len(selected_parents) - 2, 2):
            off1, off2 = selected_parents[i].crossover(selected_parents[i + 1])
            new_generation.append(off1)
            new_generation.append(off2)
            # new_generation.extend([selected_parents[i].crossover(selected_parents[i + 1])])

        for individual in new_generation:
            individual.mutate()

        self.set_list(new_generation)
        return new_generation

    def __str__(self) -> str:
        result_string = ""
        for individual in self.get_list():
            result_string += str(individual) + '\n'
        return result_string


if __name__ == '__main__':
    population = Population(100, 10)
    print(population.evaluate())
    for i in range(100):
        population.next_generation()
    population.next_generation()
    print(population.evaluate())
