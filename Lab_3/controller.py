from repository import repository


class controller():
    def __init__(self, population_size=100, individual_size=10, map=None, x=10, y=10):
        self.repo = repository()
        self.repo.createPopulation(population_size, individual_size, map, x, y)
        pass

    def iteration(self, args):
        # args - list of parameters needed to run one iteration
        # a iteration:
        # selection of the parents
        # create offsprings by crossover of the parents
        # apply some mutations
        # selection of the survivors
        population = self.repo.get_populations()[0]
        pass

    def run(self, args):
        # args - list of parameters needed in order to run the algorithm

        # until stop condition
        #    perform an iteration
        #    save the information need it for the satistics

        # return the results and the info for statistics
        pass

    def solver(self, args):
        # args - list of parameters needed in order to run the solver

        # create the population,
        # run the algorithm
        # return the results and the statistics
        pass
