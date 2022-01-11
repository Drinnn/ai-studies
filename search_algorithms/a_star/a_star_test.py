from arad_to_bucharest_graph import Graph as BucharestGraph
from porto_uniao_to_curitiba_graph import Graph as CuritibaGraph
from a_star import AStar

arad_bucharest_graph = BucharestGraph()
search = AStar(arad_bucharest_graph.bucharest)
search.search(arad_bucharest_graph.arad)

porto_uniao_curitiba_graph = CuritibaGraph()
search = AStar(porto_uniao_curitiba_graph.curitiba)
search.search(porto_uniao_curitiba_graph.portoUniao)
