class Vertex:
    def __init__(self, label, distance_from_objective):
        self.label = label
        self.distance_from_objective = distance_from_objective
        self.visited = False
        self.adjacent = []
    
    def add_adjacent(self, adjacent):
        self.adjacent.append(adjacent)

    def show_adjacent(self):
        for i in self.adjacent:
            print(i.vertex.label, i.cost)