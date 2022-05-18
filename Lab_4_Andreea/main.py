from collections import defaultdict

from controller import Controller
from map import Map
from gui import *


# Evaporation diminishes differences between the likelihood of choosing different paths if rho is large and both
# have been recently used, else it ignores inefficient paths

def run():
    drone_map = Map()
    visualiseMap(drone_map)
    controller = Controller(drone_map)
    sensor_list = drone_map.get_sensors()

    noEpoch = 100
    noAnts = 50
    alpha = 1.1
    beta = 1.5
    rho = 0.05
    q0 = 0.5

    sol = []
    bestSol = []
    bestFitness = 0

    # trace = np.zeros((len(sensor_list), len(sensor_list),5))
    trace = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: 1)))

    for sensor1 in sensor_list:
        for sensor2 in sensor_list:
            for energy in range(0, 6):
                trace[sensor1][sensor2][energy] = 1
    print("RUNNING...")
    for i in range(noEpoch):
        if i % 10 == 0:
            print(i, end=" ")
        sol, fitness = controller.epoch(noAnts, trace, alpha, beta, q0, rho)
        sol = sol.copy()
        if len(sol) > len(bestSol):
            bestSol = sol.copy()
            bestFitness = fitness

    path = [(bestSol[0][0][0], bestSol[0][0][1], bestSol[0][1])]
    bestSol = bestSol[1:]
    for step in bestSol:
        cell = step[0]
        energy = step[1]
        path_to_this = controller.sensors_paths[((path[-1][0], path[-1][1]), cell)]
        to_append = [(i[0], i[1], 0) for i in path_to_this]
        path.extend(to_append)
        path.append((cell[0], cell[1], energy))

    print("Fitness: ", bestFitness)
    print("Length of best solution:", len(path))
    print("Detected path:", bestSol)
    movingDrone(drone_map, path, speed=10)


run()
