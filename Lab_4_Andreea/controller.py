from AntSystem import *
from queue import PriorityQueue


class Controller:
    def __init__(self, map):
        self.map = map
        self.sensors_paths = {}
        self.get_paths()
        self.reached = self.determine_reached_squares()
        self.map.reached = self.reached

    def determine_reached_squares(self):
        n = self.map.n
        m = self.map.m
        reached = [[[] for j in range(m)] for i in range(n)]
        surface = self.map.surface
        for x in range(n):
            for y in range(m):
                if surface[x][y] == 2:
                    for k in range(6):
                        count = 0
                        for d in directions:
                            steps = 0
                            new_x = x + d[0]
                            new_y = y + d[1]
                            while 0 <= new_x < n and 0 <= new_y < m and surface[new_x][new_y] == 0 and steps < k:
                                count += 1
                                new_x += d[0]
                                new_y += d[1]
                                steps += 1
                        reached[x][y].append(count)
        reached[self.map.x][self.map.y] = [0 for i in range(6)]
        return reached

    def epoch(self, noAnts, trace, alpha, beta, q0, rho):
        antSet = [Ant(self.map) for i in range(noAnts)]
        for i in range(self.map.get_nr_sensors()):
            for x in antSet:
                x.addMove(q0, trace, alpha, beta)
        dTrace = [antSet[i].fitness() for i in range(len(antSet))]
        sensors = self.map.get_sensors()
        for i in sensors:
            for j in sensors:
                for e in range(0,6):
                    trace[i][j][e] = (1 - rho) * trace[i][j][e]

        for i in range(len(antSet)):
            for j in range(len(antSet[i].path) - 1):
                x = antSet[i].path[j]
                y = antSet[i].path[j + 1]
                trace[x[0]][y[0]][y[1]] = trace[x[0]][y[0]][y[1]] + dTrace[i]
        f = [[antSet[i].fitness(), i] for i in range(len(antSet))]
        f = max(f)
        return antSet[f[1]].path, antSet[f[1]].fitness()

    def get_paths(self):
        stops = self.map.get_sensors()
        stops.append((self.map.x, self.map.y))
        for s1 in stops:
            for s2 in stops:
                if s1 != s2:
                    self.sensors_paths[(s1, s2)] = self.searchAStar(s1[0], s1[1], s2[0], s2[1])
        self.map.set_sensors_paths(self.sensors_paths)

    def h(self, cell1, cell2):
        return abs(cell1[0] - cell2[0]) + abs(cell1[1] - cell2[1])

    def searchAStar(self,initialX, initialY, finalX, finalY):
        path = {}
        queue = PriorityQueue()
        start = (initialX, initialY)
        end = (finalX, finalY)
        g_cost = {}
        f_cost = {}
        n = self.map.n
        m = self.map.m
        for i in range(n):
            for j in range(m):
                g_cost[(i, j)] = float('inf')
                f_cost[(i, j)] = float('inf')
        g_cost[start] = 0
        f_cost[start] = self.h(start, end)
        queue.put((f_cost[start], f_cost[start], start))
        current = start
        while not queue.empty():
            current = queue.get()[2]
            if current == end:
                break
            for d in directions:
                neighbor = (current[0] + d[0], current[1] + d[1])
                if 0 <= neighbor[0] <= 19 and 0 <= neighbor[1] <= 19:
                    if self.map.surface[neighbor] != 1:
                        temp_g_cost = g_cost[current] + 1
                        temp_f_cost = temp_g_cost + self.h(neighbor, end)
                        if temp_f_cost < f_cost[neighbor]:
                            g_cost[neighbor] = temp_g_cost
                            f_cost[neighbor] = temp_f_cost
                            queue.put((temp_f_cost, self.h(neighbor, end), neighbor))
                            path[neighbor] = current
        if current != end:
            return []
        result = []
        cell = end
        while cell != start:
            result.append(cell)
            cell = path[cell]
        result.append(start)
        result.reverse()
        return result



