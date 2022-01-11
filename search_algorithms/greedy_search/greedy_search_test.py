from test_graph import Graph
from greedy_search import GreedySearch

graph = Graph()
search = GreedySearch(graph.bucharest)
search.search(graph.arad)