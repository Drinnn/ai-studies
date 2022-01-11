from ordered_vector import OrderedVector


class AStar:
    def __init__(self, objective):
        self.objective = objective
        self.found = False

    def search(self, actual):
        print('--------------------------')
        print('Actual: {}'.format(actual.label))
        actual.visited = True

        if actual == self.objective:
            self.found = True
        else:
            ordered_vector = OrderedVector(len(actual.adjacent))
            for adjacent in actual.adjacent:
                if adjacent.vertex.visited == False:
                    adjacent.vertex.visited = True
                    ordered_vector.insert(adjacent)
            ordered_vector.show()

            if ordered_vector.values[0] != None:
                self.search(ordered_vector.values[0].vertex)
