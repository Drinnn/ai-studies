class Adjacent:
    def __init__(self, vertex, cost):
        self.vertex = vertex
        self.cost = cost
        self.a_star_distance = vertex.distance_from_objective + self.cost