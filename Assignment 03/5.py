def ucs_blocks_world(initial, goal):
    heap = []
    heapq.heappush(heap, (0, initial, []))
    visited = set()
    
    while heap:
        cost, state, path = heapq.heappop(heap)
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
                        heapq.heappush(heap, (cost + 1, tuple(tuple(stack) for stack in next_state), path + [(block, i, j)]))
    return None

# Example usage:
initial = (('S',), ('S',), ('G',))
goal = ((), (), ('G', 'S', 'S'))
print("UCS Solution:", ucs_blocks_world(initial, goal))