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
    frontier = [(initial_state, [initial_state])]
    visited = set()

    while frontier:
        current_state, current_path = frontier.pop(0)

        if is_goal(current_state, goal):
            return current_path

        if current_state in visited:
            continue
        visited.add(current_state)

        valid_next_states = get_valid_next_states(current_state, maze)

        for _, next_state in valid_next_states.items():
            if next_state not in visited:
                new_path = current_path + [next_state]

                frontier.append((next_state, new_path))

        return None


def dfs_search(maze, initial_state, goal): ...


def greedy_search(maze, initial_state, goal): ...


def evaluate_solution(path): ...


def run_searches(): ...
