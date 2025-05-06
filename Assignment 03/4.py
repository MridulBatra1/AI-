def ids_blocks_world(initial, goal):
    depth = 0
    while True:
        result = dls_blocks_world(initial, goal, depth)
        if result is not None:
            return depth, result
        depth += 1

# Example usage:
initial = (('A', 'C', 'B'), ('A',), ())
goal = (('C', 'B', 'A'), (), ())
depth, path = ids_blocks_world(initial, goal)
print(f"IDS Solution found at depth {depth}:", path)