def water_jug_problem(jug1_cap, jug2_cap, jug3_cap, target_amount):
    # Initialize the jugs and the possible actions
    j1 = 12
    j2 = 0
    j3 = 0
    actions = [("pour", 2, 1), ("pour", 3, 1), ("pour", 2, 3), ("pour", 3, 2)]
    # Create an empty set to store visited states
    visited = set()
    # Create a queue to store states to visit
    queue = [(j1, j2, j3, [])]

    while queue:
        # Dequeue the front state from the queue
        j1, j2, j3, seq = queue.pop(0)
        # If this state has not been visited before, mark it as visited
        if (j1, j2, j3) not in visited:
            visited.add((j1, j2, j3))
            # If this state matches the target amount, return the sequence of actions taken to get to this state
            if j1 == target_amount or j2 == target_amount or j3 == target_amount:
                return seq
            # Generate all possible next states from this state
            for action in actions:
                # Pour action
                source_jug = action[1]
                target_jug = action[2]
                capacities = [(j1, jug1_cap), (j2, jug2_cap), (j3, jug3_cap)]
                amount = min(capacities[source_jug - 1][0], capacities[target_jug - 1][1] - capacities[target_jug - 1][0])
                next_state = list((j1, j2, j3))
                next_state[source_jug - 1] -= amount
                next_state[target_jug - 1] += amount
                next_state = tuple(next_state)

                # Add the next state to the queue if it has not been visited before
                if next_state not in visited:
                    next_seq = seq + [(action, next_state)]
                    queue.append((next_state[0], next_state[1], next_state[2], next_seq))
    # If the queue becomes empty without finding a solution, return None
    return None

result = water_jug_problem(12, 8, 5, 6)

if result:
    for step in result:
        action, state = step
        print(f"{action}: {state}")
else:
    print("No solution")
