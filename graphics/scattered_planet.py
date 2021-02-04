import math
import random

import matplotlib.pyplot as plt


class ProbabilisticRoadMap:
    def __init__(self, n_points, length, droppout=0.2):
        self.n_points = n_points
        self.length = length
        self.dropout = droppout
        self.point_neighbours = None
        self._coordinate_pairs = self._generate_random_coordinates()

    def _generate_random_coordinates(self):
        return [(random.random(), random.random()) for _ in range(self.n_points)]

    @staticmethod
    def _calculate_euclidean_distance(point_0, point_1):
        return math.sqrt((point_0[0]-point_1[0])**2 + (point_0[1]-point_1[1])**2)

    def _find_neighbouring_points(self, point):
        return {
            coord for coord in self._coordinate_pairs
            if self._calculate_euclidean_distance(point, coord) < self.length
            and random.random() > self.dropout
        }

    def _generate_point_neighbour_coordinate_pairs(self, point):
        neighbours = self._find_neighbouring_points(point)
        return [[point, neighbour] for neighbour in neighbours]

    def get_random_point(self):
        return random.choice(self._coordinate_pairs)

    def plot(self):
        plt.scatter(
            [coord[0] for coord in self._coordinate_pairs],
            [coord[1] for coord in self._coordinate_pairs],
            marker='.'
        )
        plt.show()


if __name__ == '__main__':
    prm = ProbabilisticRoadMap(1000, 0.2, 0.9)
    point = prm.get_random_point()
    neighbours = prm._find_neighbouring_points(point)
    neighbour_coords = prm._generate_point_neighbour_coordinate_pairs(point)

    x_vals = []
    y_vals = []
    for neighbour in neighbour_coords:
        x_vals.append(neighbour[0][0])
        x_vals.append(neighbour[1][0])
        y_vals.append(neighbour[0][1])
        y_vals.append(neighbour[1][1])

    plt.scatter(
        [coord[0] for coord in prm._coordinate_pairs],
        [coord[1] for coord in prm._coordinate_pairs],
        marker='.'
    )
    plt.scatter(
        [coord[0] for coord in neighbours],
        [coord[1] for coord in neighbours],
        marker='.'
    )
    plt.plot(x_vals, y_vals)
    plt.show()

