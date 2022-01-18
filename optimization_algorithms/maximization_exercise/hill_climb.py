import mlrose_hiive
from representation import print_shipped_products, fitness_function

fitness = mlrose_hiive.CustomFitness(fitness_function)
problem_representation = mlrose_hiive.DiscreteOpt(
    length=14, fitness_fn=fitness, maximize=True, max_val=2)

best_solution, best_cost, _ = mlrose_hiive.hill_climb(problem_representation)
print_shipped_products(best_solution)
