maze = [
    ["S", ".", ".", "#"],
    ["#", ".", ".", "#"],
    [".", ".", ".", "G"],
]

initial_state = (0, 0)
goal = (2, 3)


def get_possible_moves(state):
    row, col = state

    possible_moves = {
        "up": (row - 1, col),
        "down": (row + 1, col),
        "left": (row, col - 1),
        "right": (row, col + 1),
    }

    return possible_moves


def is_in_bounds(state, maze):
    row, col = state
    num_rows = len(maze)
    num_cols = len(maze[0])
    return 0 <= row < num_rows and 0 <= col < num_cols


def is_valid_state(state, maze):
    if not is_in_bounds(state, maze):
        return False
    row, col = state
    return maze[row][col] != "#"


def get_valid_next_states(state, maze):
    possible_moves = get_possible_moves(state)
    valid_next_states = {}

    for move, next_state in possible_moves.items():
        if is_valid_state(next_state, maze):
            valid_next_states[move] = next_state

    return valid_next_states


def is_goal(state, goal):
    return state == goal


def heuristic(state, goal):
    row, col = state
    goal_row, goal_col = goal
    return abs(row - goal_row) + abs(col - goal_col)


def bfs_search(maze, initial_state, goal):
    # FRONTIER
    # Stores states that BFS has discovered but has not explored yet.
    #
    # Each frontier item contains TWO things:
    #
    # 1. The state
    # 2. The path used to reach that state
    #
    # At the beginning:
    #
    # state = initial_state
    # path = [initial_state]
    #
    # Example:
    # ((0, 0), [(0, 0)])
    frontier = [(initial_state, [initial_state])]

    # VISITED STATES
    # Stores states that BFS has already explored.
    #
    # This prevents BFS from repeatedly visiting
    # the same places and getting stuck in loops.
    visited = set()

    # Keep searching as long as there are states
    # waiting inside the frontier.
    while frontier:
        # BFS uses FIFO:
        # First In, First Out.
        #
        # pop(0) removes the OLDEST item from the frontier.
        #
        # The item contains:
        #
        # current_state = the state we will explore now
        # current_path = the path used to reach that state
        current_state, current_path = frontier.pop(0)

        # GOAL TEST
        # Check whether the state we are currently exploring
        # is the goal.
        #
        # If yes, return the path that reached this state.
        if is_goal(current_state, goal):
            return current_path

        # VISITED CHECK
        # If we already explored this state before,
        # skip it.
        if current_state in visited:
            continue

        # We are now exploring this state,
        # so remember it as visited.
        visited.add(current_state)

        # NEXT STATES
        # Find every valid state we can move to
        # from the current state.
        #
        # Example:
        #
        # current_state = (0, 1)
        #
        # valid_next_states might be:
        #
        # {
        #     "right": (0, 2),
        #     "down": (1, 1)
        # }
        valid_next_states = get_valid_next_states(
            current_state,
            maze,
        )

        # Explore every valid next state.
        #
        # We don't currently need the action name,
        # so "_" means:
        #
        # "There is a value here, but I am not using it."
        for _, next_state in valid_next_states.items():
            # Only add a state if it has not already
            # been explored.
            if next_state not in visited:
                # PATH TRACKING
                #
                # Take the path used to reach current_state
                # and create a NEW path for next_state.
                #
                # Example:
                #
                # current_path:
                # [(0, 0), (0, 1)]
                #
                # next_state:
                # (1, 1)
                #
                # new_path:
                # [(0, 0), (0, 1), (1, 1)]
                #
                # current_path stays unchanged.
                new_path = current_path + [next_state]

                # Add BOTH:
                #
                # next_state
                # +
                # the path used to reach next_state
                #
                # to the frontier.
                #
                # Example:
                #
                # (
                #     (1, 1),
                #     [(0, 0), (0, 1), (1, 1)]
                # )
                frontier.append((next_state, new_path))

    # If the while loop finishes,
    # the frontier became empty.
    #
    # That means BFS explored everything it could
    # but never found the goal.
    return None


def dfs_search(maze, initial_state, goal): ...


def greedy_search(maze, initial_state, goal): ...


def evaluate_solution(path): ...


def run_searches(): ...


