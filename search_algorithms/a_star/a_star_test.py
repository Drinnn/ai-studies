from test_graph import Graph
from a_star import AStar

graph = Graph()
search = AStar(graph.bucharest)
search.search(graph.arad)
