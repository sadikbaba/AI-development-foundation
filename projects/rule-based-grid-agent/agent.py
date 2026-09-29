# Phase project: Build a mini robot agent that navigates a grid
# toward its goal using rules and a simple heuristic.


# ENVIRONMENT
# The grid is the world the agent interacts with.
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


# AGENT POSITION
# Represents where the agent is in the environment.
def agent_position(row, col):
    return (row, col)


# VALID-MOVE RULE
# The agent cannot move into an obstacle.
def is_valid_move(cell):
    return cell != "#"


# GOAL TEST
# Checks whether a cell is the goal.
def is_goal(cell):
    return cell == "G"


# BOUNDARY RULE
# Prevents the agent from moving outside the grid.
def in_bounds(row, col, grid):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])


# HEURISTIC
# Manhattan distance estimates how far a position is from the goal.
# Lower score means the position appears closer to the goal.
def heuristic(current, goal):
    current_row = current[0]
    current_col = current[1]
    goal_row = goal[0]
    goal_col = goal[1]

    return abs(current_row - goal_row) + abs(current_col - goal_col)


# CURRENT STATE
# The agent currently starts at (0, 0).
row = 0
col = 0

# The goal position in the grid.
goal = (3, 3)


# DECISION-MAKING MEMORY
# These will remember the best move found while comparing valid moves.
# None means no move has been selected yet.
best_action = None
best_score = None


# POSSIBLE ACTIONS
# Each action maps to the position the agent would reach if it moved there.
move = {
    "up": (row - 1, col),
    "down": (row + 1, col),
    "left": (row, col - 1),
    "right": (row, col + 1),
}


# VALID ACTIONS
# This will contain only moves that stay inside the grid
# and do not hit an obstacle.
valid_moves = {}


# PERCEPTION + RULE CHECKING
# Inspect every possible move and keep only valid ones.
for action, position in move.items():
    row, col = position

    # Reject positions outside the environment.
    if not in_bounds(row, col, grid):
        continue

    # Perceive what exists at this position.
    cell = grid[row][col]

    # Reject obstacles and keep valid actions.
    if is_valid_move(cell):
        valid_moves[action] = position


# DECISION MAKING
# Compare the valid moves and keep the one with the lowest heuristic score.
for action, position in valid_moves.items():
    row, col = position

    # Perceive the cell belonging to this valid position.
    cell = grid[row][col]

    # If this move reaches G, the goal has been found.
    if is_goal(cell):
        print(f"Goal reached at {position}")
        break

    # Estimate how far this possible position is from the goal.
    score = heuristic(position, goal)

    # If there is no winner yet, or this move has a lower score,
    # make this action the new best choice.
    if best_score is None or score < best_score:
        best_score = score
        best_action = action


print("valid moves:", valid_moves)
print(f"Best Move {best_action}  Best score {best_score}")