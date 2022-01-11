import numpy as np


class OrderedVector:

    def __init__(self, capacity):
        self.capacity = capacity
        self.last_position = -1
        self.values = np.empty(self.capacity, dtype=object)

    def insert(self, adjacent):
        if self.last_position == self.capacity - 1:
            print("Maximum capacity reached.")
            return

        position = 0
        for i in range(self.last_position + 1):
            position = i
            if self.values[i].a_star_distance > adjacent.a_star_distance:
                break
            if i == self.last_position:
                position = i + 1

        x = self.last_position
        while x >= position:
            self.values[x + 1] = self.values[x]
            x -= 1

        self.values[position] = adjacent
        self.last_position += 1

    def show(self):
        if self.last_position == -1:
            print("Vector is empty.")
        else:
            for i in range(self.last_position + 1):
                print('{} - {} - {} - {} - {}'.format(i, self.values[i].vertex.label, self.values[i].cost,
                      self.values[i].vertex.distance_from_objective, self.values[i].a_star_distance))
