import math

def evaluate_solution(solution, clauses):
    a, b, c, d = solution
    satisfied = 0
    for clause in clauses:
        if eval(clause):
            satisfied += 1
    return satisfied

def simulated_annealing(clauses, initial_solution, T, cooling_rate, random_numbers):
    current_solution = initial_solution
    current_energy = evaluate_solution(current_solution, clauses)
    iteration = 0
    
    while T > 0:
        # Generate neighbor by flipping one variable
        variable_to_flip = iteration % 4
        neighbor = list(current_solution)
        neighbor[variable_to_flip] = not neighbor[variable_to_flip]
        neighbor_energy = evaluate_solution(neighbor, clauses)
        
        # Decide acceptance
        delta_energy = neighbor_energy - current_energy
        if delta_energy > 0 or (delta_energy <= 0 and random_numbers[iteration % len(random_numbers)] > 0.5):
            current_solution = neighbor
            current_energy = neighbor_energy
        
        T -= cooling_rate
        iteration += 1
    
    return current_solution, current_energy

# Problem data
clauses = [
    '(not a or d)',
    '(c or b)',
    '(not c or not d)',
    '(not d or not b)',
    '(not a or not d)'
]
initial_solution = [True, True, True, True]  # a, b, c, d
T = 500
cooling_rate = 50
random_numbers = [0.655, 0.254, 0.432]

best_solution, clauses_satisfied = simulated_annealing(clauses, initial_solution, T, cooling_rate, random_numbers)
print("Best Solution:", ['a' if x else '~a' for x in best_solution])
print("Clauses Satisfied:", clauses_satisfied)