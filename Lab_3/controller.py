from repository import repository


class controller():
    def __init__(self, population_size=100, individual_size=10, map=None, x=10, y=10):
        self.repo = repository()
        self.repo.createPopulation(population_size, individual_size, map, x, y)
        pass

    def iteration(self, crossover_probability=0.8, mutate_probability=0.04):
        # args - list of parameters needed to run one iteration
        # a iteration:
        # selection of the parents
        # create offsprings by crossover of the parents
        # apply some mutations
        # selection of the survivors
        population = self.repo.get_first_population()
        return population.next_generation(crossover_probability=crossover_probability,
                                          mutate_probability=mutate_probability)

    def run(self, iterations=1000, crossover_probability=0.8, mutate_probability=0.04):
        # args - list of parameters needed in order to run the algorithm

        # until stop condition
        #    perform an iteration
        #    save the information need it for the satistics

        # return the results and the info for statistics
        evaluations = []
        for i in range(iterations):
            evaluations.append(self.iteration(crossover_probability, mutate_probability))
        return evaluations

    def solver(self, args):
        # args - list of parameters needed in order to run the solver

        # create the population,
        # run the algorithm
        # return the results and the statistics
        pass
