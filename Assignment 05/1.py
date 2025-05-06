import random

def fitness(chromosome, weights, values, max_weight):
    total_weight = sum(w * int(c) for w, c in zip(weights, chromosome))
    total_value = sum(v * int(c) for v, c in zip(values, chromosome))
    return total_value if total_weight <= max_weight else 0

def genetic_algorithm_knapsack(weights, values, max_weight, initial_pop, iterations):
    population = initial_pop.copy()
    mutation_order = ['x_D', 'x_C', 'x_B', 'x_A']
    mutation_index = 0
    
    for _ in range(iterations):
        
        fitness_scores = [fitness(ind, weights, values, max_weight) for ind in population]
        sorted_pop = [x for _, x in sorted(zip(fitness_scores, population), reverse=True)]
        
        new_pop = sorted_pop[:2]
        parent1, parent2 = sorted_pop[2], sorted_pop[3]
        
        
        crossover_point = len(parent1) // 2
        offspring1 = parent1[:crossover_point] + parent2[crossover_point:]
        offspring2 = parent2[:crossover_point] + parent1[crossover_point:]
        
        bit_to_mutate = mutation_order[mutation_index % 4]
        mutation_pos = ['x_A', 'x_B', 'x_C', 'x_D'].index(bit_to_mutate)
        offspring1 = offspring1[:mutation_pos] + ('1' if offspring1[mutation_pos] == '0' else '0') + offspring1[mutation_pos+1:]
        mutation_index += 1
        
        new_pop.extend([offspring1, offspring2])
        population = new_pop
    
    best_solution = max(population, key=lambda x: fitness(x, weights, values, max_weight))
    return best_solution, fitness(best_solution, weights, values, max_weight)


weights = [45, 40, 50, 90]
values = [3, 5, 8, 10]
max_weight = 100
initial_pop = ['1111', '1000', '1010', '1001']
iterations = 10

best_solution, best_value = genetic_algorithm_knapsack(weights, values, max_weight, initial_pop, iterations)
print("Best Solution:", best_solution)
print("Total Value:", best_value)