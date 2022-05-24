import csv
import random
from matplotlib import pyplot as plt

from numpy import sqrt


class Point:
    def __init__(self, x, y, classification=None):
        self.x = x
        self.y = y
        self.classification = classification

    def distance(self, another):
        return sqrt((self.x - another.x)** 2 + (self.y - another.y)** 2)

    def __str__(self) -> str:
        return self.x + ' ' + self.y + ' -> ' + self.classification


class Cluster:
    def __init__(self, centroid):
        self.points = []
        self.centroid = centroid
        self.deviation = -1
        self.count = 0
        self.frequency = {}

    def add(self, point):
        self.points.append(point)
        self.count += 1
        if point.classification not in self.frequency.keys():
            self.frequency[point.classification] = 1
        else:
            self.frequency[point.classification] += 1

    def find_centroid(self):
        x = 0
        y = 0
        for p in self.points:
            x += p.x
            y += p.y
        x = x / self.count
        y = y / self.count
        self.centroid = Point(x, y)

    def compute_deviation(self):
        self.deviation = 0
        for p in self.points:
            self.deviation += p.distance(self.centroid)
        return self.deviation

    def converge(self):
        initial_deviation = self.compute_deviation()
        self.find_centroid()
        new_deviation = self.compute_deviation()
        while initial_deviation > new_deviation:
            initial_deviation = new_deviation
            self.find_centroid()
            new_deviation = self.compute_deviation()

    def find_majority(self):
        classification, appearance = ' ', -1
        for key in self.frequency.keys():
            if self.frequency[key] > appearance:
                appearance = self.frequency[key]
                classification = key
        return classification


def read_file(filename):
    points = []
    with open(filename) as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            points.append(Point(float(row[1]), float(row[2]), row[0]))
            # print(row)
    return points


def create_clusters(points, k):
    clusters = []
    for i in range(k):
        pos = random.randint(0, len(points) - 1)
        clusters.append(Cluster(points[pos]))
    for p in points:
        c = None
        d = 100000
        for cluster in clusters:
            if p.distance(cluster.centroid) < d:
                d = p.distance(cluster.centroid)
                c = cluster
        c.add(p)

    total_deviation = 0
    for cluster in clusters:
        cluster.converge()
        total_deviation += cluster.deviation

    return clusters, total_deviation


def find_clusters(points, k, epochs):
    initial_clusters, initial_deviation = create_clusters(points, k)
    for i in range(epochs):
        new_clusters, new_deviation = create_clusters(points, k)
        if new_deviation < initial_deviation:
            initial_deviation = new_deviation
            initial_clusters = new_clusters

    return initial_clusters

def plot_points(points):
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    color = "black"
    for p in points:
        if p.classification == 'A':
            color = "red"
        elif p.classification == 'B':
            color = "blue"
        elif p.classification == 'C':
            color = "green"
        elif p.classification == 'D':
            color = "yellow"
        plt.plot(p.x, p.y, marker="o", markersize=4, markeredgecolor="black", markerfacecolor=color)
    plt.show()

if __name__ == '__main__':
    points = read_file('dataset.csv')
    clusters = find_clusters(points, 4, 80)
    for cluster in clusters:
        print(cluster.frequency)
        plot_points(cluster.points)
    # plot_points(points)


