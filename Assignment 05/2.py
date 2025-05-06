def genetic_algorithm_thief(items, max_weight, initial_pop, iterations):
    names, weights, values = zip(*items)
    mutation_order = ['X_C', 'X_A', 'X_D', 'X_B']
    mutation_index = 0
    population = initial_pop.copy()
    
    for _ in range(iterations):

        fitness_scores = [fitness(ind, weights, values, max_weight) for ind in population]
        sorted_pop = [x for _, x in sorted(zip(fitness_scores, population), reverse=True)]
        
        new_pop = sorted_pop[:2]
        parent1, parent2 = sorted_pop[2], sorted_pop[3]
        
        crossover_point = len(parent1) // 2
        offspring1 = parent1[:crossover_point] + parent2[crossover_point:]
        offspring2 = parent2[:crossover_point] + parent1[crossover_point:]
        
        bit_to_mutate = mutation_order[mutation_index % 4]
        mutation_pos = ['X_A', 'X_B', 'X_C', 'X_D'].index(bit_to_mutate)
        offspring1 = offspring1[:mutation_pos] + ('1' if offspring1[mutation_pos] == '0' else '0') + offspring1[mutation_pos+1:]
        mutation_index += 1
        
        new_pop.extend([offspring1, offspring2])
        population = new_pop
    
    best_solution = max(population, key=lambda x: fitness(x, weights, values, max_weight))
    return best_solution, fitness(best_solution, weights, values, max_weight)

items = [('A', 2, 3), ('B', 3, 5), ('C', 4, 7), ('D', 5, 9)]
max_weight = 9
initial_pop = ['1111', '1000', '1010', '1001']
iterations = 4

best_solution, best_value = genetic_algorithm_thief(items, max_weight, initial_pop, iterations)
print("Best Solution:", best_solution)
print("Total Value:", best_value)