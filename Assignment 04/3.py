def correctly_placed_tiles(state, goal):
    return sum(1 for i in range(3) for j in range(3) if state[i][j] == goal[i][j] and state[i][j] != 0)

def a_star_search(initial, goal):
    visited = set()
    priority_queue = PriorityQueue()
    priority_queue.put((0 + correctly_placed_tiles(initial, goal), 0, initial, []))
    
    while not priority_queue.empty():
        _, cost, state, path = priority_queue.get()
        if state == goal:
            return path, len(path)
        if tuple(map(tuple, state)) in visited:
            continue
        visited.add(tuple(map(tuple, state)))
        
        zero_i, zero_j = next((i, j) for i in range(3) for j in range(3) if state[i][j] == 0)
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_i, new_j = zero_i + di, zero_j + dj
            if 0 <= new_i < 3 and 0 <= new_j < 3:
                new_state = [list(row) for row in state]
                new_state[zero_i][zero_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[zero_i][zero_j]
                priority_queue.put((cost + 1 + correctly_placed_tiles(new_state, goal), cost + 1, new_state, path + [new_state]))
    return None, 0

# Example usage:
initial = [[1, 2, 3], [0, 4, 6], [7, 5, 8]]
goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
path, moves = a_star_search(initial, goal)
print("A* Search Path:")
for step in path:
    print(step)
print("Total Moves:", moves)