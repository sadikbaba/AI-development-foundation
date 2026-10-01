# Phase 1 Project:
# Build a small rule-based AI agent that navigates a grid
# toward a goal using rules and a Manhattan-distance heuristic.


# ============================================================
# ENVIRONMENT
# ============================================================
# The grid is the world the agent interacts with.
#
# S = starting position
# G = goal
# # = obstacle
# . = open cell

grid = [
    ["S", ".", ".", "."],
    [".", "#", ".", "."],
    [".", "#", ".", "."],
    [".", ".", ".", "G"],
]


# The goal is represented using (row, column).
goal = (3, 3)


# ============================================================
# POSSIBLE MOVES
# ============================================================
# Generate the four positions the agent could try from
# its current position.
#
# This function does not check whether those positions
# are valid yet.

def get_possible_moves(current_position):
    row, col = current_position

    possible_moves = {
        "up": (row - 1, col),
        "down": (row + 1, col),
        "left": (row, col - 1),
        "right": (row, col + 1),
    }

    return possible_moves


# ============================================================
# BOUNDARY CHECK
# ============================================================
# Check whether a position exists inside the grid.
#
# Positions outside the grid cannot be used by the agent.

def is_in_bounds(position, grid):
    row, col = position

    num_rows = len(grid)
    num_cols = len(grid[0])

    return 0 <= row < num_rows and 0 <= col < num_cols


# ============================================================
# VALID MOVE CHECK
# ============================================================
# A move is valid when:
#
# 1. The position is inside the grid.
# 2. The cell is not an obstacle.

def is_valid_move(position, grid, obstacle="#"):
    row, col = position

    if not is_in_bounds(position, grid):
        return False

    cell = grid[row][col]

    return cell != obstacle


# ============================================================
# VALID MOVE FILTERING
# ============================================================
# Start with every possible move and keep only the moves
# the agent is actually allowed to make.

def get_valid_moves(possible_moves, grid):
    valid_moves = {}

    for action, (row, col) in possible_moves.items():
        if is_valid_move((row, col), grid):
            valid_moves[action] = (row, col)

    return valid_moves


# ============================================================
# HEURISTIC
# ============================================================
# Use Manhattan distance to estimate how far a position
# is from the goal.
#
# The robot can move only:
#
# up
# down
# left
# right
#
# A smaller score means the position appears closer
# to the goal.

def heuristic(position, goal):
    row, col = position
    goal_row, goal_col = goal

    return abs(row - goal_row) + abs(col - goal_col)


# ============================================================
# DECISION MAKING
# ============================================================
# Compare every valid move using the heuristic.
#
# Remember the action with the smallest score.
#
# best_score stores the smallest score found so far.
# best_move stores the action that produced that score.

def choose_best_move(valid_moves, goal):
    best_move = None
    best_score = None

    for action, (row, col) in valid_moves.items():
        score = heuristic((row, col), goal)

        if best_score is None or score < best_score:
            best_score = score
            best_move = action

    return best_move


# ============================================================
# GOAL CHECK
# ============================================================
# The goal is reached when the agent's current position
# is the same as the goal position.

def is_goal(current_position, goal):
    return current_position == goal


# ============================================================
# MOVEMENT
# ============================================================
# Convert the chosen action into the position that the
# agent should move to.

def move_agent(best_move, valid_moves):
    return valid_moves[best_move]


# ============================================================
# MAIN AGENT LOOP
# ============================================================
# This function connects all the smaller functions.
#
# Each loop represents one decision cycle:
#
# 1. Observe the current position.
# 2. Generate possible moves.
# 3. Keep only valid moves.
# 4. Score the valid moves.
# 5. Choose the best move.
# 6. Move to the selected position.
# 7. Record the new position.
# 8. Repeat until the goal is reached.

def run_agent():
    current_position = (0, 0)

    # The path records every position visited by the agent.
    # It begins with the starting position.
    path = [current_position]

    # Continue making decisions until the goal is reached.
    while not is_goal(current_position, goal):

        # Generate possible actions from the current position.
        possible_moves = get_possible_moves(current_position)

        # Remove moves that leave the grid or hit obstacles.
        valid_moves = get_valid_moves(possible_moves, grid)

        # Use the heuristic to choose the most promising move.
        best_move = choose_best_move(valid_moves, goal)

        # Move the agent to the position belonging to that action.
        current_position = move_agent(best_move, valid_moves)

        # Remember where the agent moved.
        path.append(current_position)

        # Show the current decision cycle.
        print(f"current position: {current_position}")
        print(f"valid moves: {valid_moves}")
        print(f"best move: {best_move}")
        print(f"path: {path}")
        print()

    # The loop ends when current_position equals goal.
    print("Goal reached.")
    print("path:", path)


# ============================================================
# START THE AGENT
# ============================================================

run_agent()