import mlrose_hiive
from representation import fitness_function

fitness = mlrose_hiive.CustomFitness(fitness_function)
problem_representation = mlrose_hiive.DiscreteOpt(
    length=12, fitness_fn=fitness, maximize=False, max_val=10)

best_solution, best_cost, _ = mlrose_hiive.genetic_alg(
    problem_representation, pop_size=500, mutation_prob=0.2)
print(best_solution, best_cost)
