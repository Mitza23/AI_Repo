from random import *
from utils import *


class Ant:
    def __init__(self, map):
        self.map = map
        self.start_x = map.x
        self.start_y = map.y
        self.path = [((self.start_x, self.start_y), 0)]
        self.visited = [(self.start_x, self.start_y)]
        self.battery = BATTERY

    def nextMoves(self, current):
        new = []
        n = self.map.n
        m = self.map.m
        for s in self.map.get_sensors():
            if s != current and s != (self.map.x, self.map.y) and s not in self.visited:
                path = self.map.sensors_paths[current, s]
                if path:
                    new.append(s)
        return new.copy()

    def distMove(self, s):
        return 1 / len(self.map.sensors_paths[(self.path[-1][0], s)])

    def addMove(self, q0, trace, alpha, beta):
        p = {}
        nextSteps = self.nextMoves(self.path[-1][0]).copy()
        if len(nextSteps) == 0:
            return False
        for s in nextSteps:
            for e in range(0, 6):
                p[(s, e)] = self.distMove(s)
        for s, e in p:
            p[(s, e)] = (p[(s, e)] ** beta) * (trace[self.path[-1][0]][s][e] ** alpha)
        if random() < q0:
            max = [[(0, 0), 0], 0]
            for move in p.keys():
                if p[move] > max[1]:
                    max = [[move[0], move[1]], p[move]]
            max[0][1] = min(max[0][1], self.battery)
            self.battery -= max[0][1]
            self.path.append((max[0][0], max[0][1]))
            self.visited.append(max[0][0])
        else:
            s = sum(p.values())
            if s == 0:
                s = choice(nextSteps)
                e = min(randint(0, 5), self.battery)
                self.battery -= e
                return s, e

            p = {k: p[k] / s for k in p.keys()}
            roulette_sum = 0
            for k in p.keys():
                roulette_sum += p[k]
                p[k] = roulette_sum
            r = random()
            best = ()
            for k in p.keys():
                if r <= p[k]:
                    best = k
                    break

            energy = min(best[1], self.battery)
            self.battery -= energy
            self.path.append((best[0], energy))
            self.visited.append(best[0])
        return True

    def fitness(self):
        sum = 1
        length = 0
        for i in range(len(self.path)):
            step = self.path[i]
            x, y = step[0][0], step[0][1]
            if i < len(self.path) - 1:
                step2 = self.path[i + 1]
                x2, y2 = step2[0][0], step2[0][1]
                length += len(self.map.sensors_paths[(x, y), (x2, y2)])
            energy = step[1]
            sum += self.map.reached[x][y][energy]

        return sum / length
