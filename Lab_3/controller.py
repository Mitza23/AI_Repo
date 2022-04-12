from repository import repository


class controller():
    def __init__(self, population_size=100, individual_size=10, map=None, x=10, y=10, crossover_probability=0.8,
                 mutate_probability=0.04, iterations=200):
        self.repo = repository()
        self.repo.createPopulation(population_size, individual_size, map, x, y)
        self.crossover_probability = crossover_probability
        self.mutate_probability = mutate_probability
        self.iterations = iterations
        pass

    def iteration(self, crossover_probability=0.8, mutate_probability=0.04):
        # args - list of parameters needed to run_once one iteration
        # a iteration:
        # selection of the parents
        # create offsprings by crossover of the parents
        # apply some mutations
        # selection of the survivors
        population = self.repo.get_first_population()
        return population.next_generation(crossover_probability=self.crossover_probability,
                                          mutate_probability=self.mutate_probability)

    def run(self):
        # args - list of parameters needed in order to run_once the algorithm

        # until stop condition
        #    perform an iteration
        #    save the information need it for the satistics

        # return the results and the info for statistics
        evaluations = []
        for i in range(self.iterations):
            evaluations.append(self.iteration(self.crossover_probability, self.mutate_probability))
        return evaluations

    def solver(self, args):
        # args - list of parameters needed in order to run_once the solver

        # create the population,
        # run_once the algorithm
        # return the results and the statistics
        pass
