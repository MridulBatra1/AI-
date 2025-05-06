def bfs_blocks_world(initial, goal):
    queue = deque([(initial, [])])
    visited = set()
    
    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path
        if tuple(tuple(stack) for stack in state) in visited:
            continue
        visited.add(tuple(tuple(stack) for stack in state))
        
        for i in range(len(state)):
            if state[i]:
                block = state[i][-1]
                new_state = [list(stack) for stack in state]
                new_state[i].pop()
                for j in range(len(new_state)):
                    if j != i:
                        next_state = [list(stack) for stack in new_state]
                        next_state[j].append(block)
                        queue.append((tuple(tuple(stack) for stack in next_state), path + [(block, i, j)]))
    return None

# Example usage:
initial = (('A', 'C', 'B'), ('A',), ())
goal = (('C', 'B', 'A'), (), ())
print("BFS Solution:", bfs_blocks_world(initial, goal))