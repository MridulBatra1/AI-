def hill_climbing(initial, goal):
    current = initial
    path = [current]
    while True:
        if current == goal:
            return path, len(path) - 1
        zero_i, zero_j = next((i, j) for i in range(3) for j in range(3) if current[i][j] == 0)
        neighbors = []
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_i, new_j = zero_i + di, zero_j + dj
            if 0 <= new_i < 3 and 0 <= new_j < 3:
                new_state = [list(row) for row in current]
                new_state[zero_i][zero_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[zero_i][zero_j]
                neighbors.append(new_state)
        if not neighbors:
            return None, 0
        best_neighbor = min(neighbors, key=lambda x: misplaced_tiles(x, goal))
        if misplaced_tiles(best_neighbor, goal) >= misplaced_tiles(current, goal):
            return None, 0
        current = best_neighbor
        path.append(current)

# Example usage:
initial = [[1, 2, 3], [0, 4, 6], [7, 5, 8]]
goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
path, moves = hill_climbing(initial, goal)
print("Hill Climbing Path:")
for step in path:
    print(step)
print("Total Moves:", moves)