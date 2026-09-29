# Phase project: Build a mini robot agent that navigates a grid toward its goal using rules and a simple heuristic.


# The grid represents the agent's environment.

# Environment: the grid the agent interacts with.

# S = starting position
# G = goal
# # = obstacle
# . = open cell


# The agent perceives nearby cells before choosing an action.

# The agent uses rules and a heuristic to choose its next move.
grid = [
    ["S", ".", ".", "."],
    [".", "#", ".", "."],
    [".", "#", ".", "."],
    [".", ".", ".", "G"],
]


def agent_position(row, col):
    return (row, col)


def is_valid_move(cell):
    return cell != "#"


def is_goal(cell):
    return cell == "G"


def in_bounds(row, col, grid):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])


def heuristic(current, goal):
    current_row = current[0]
    current_col = current[1]
    goal_row = goal[0]
    goal_col = goal[1]
    return abs(current_row - goal_row) + abs(current_col - goal_col)


row = 0
col = 0
goal = (3, 3)


best_action = None
best_score = None


move = {
    "up": (row - 1, col),
    "down": (row + 1, col),
    "left": (row, col - 1),
    "right": (row, col + 1),
}

valid_moves = {}


for action, position in move.items():
    row, col = position

    if not in_bounds(row, col, grid):
        continue
    cell = grid[row][col]

    if is_valid_move(cell):
        valid_moves[action] = position
        

for action, position in valid_moves.items():
    row, col = position
    cell = grid[row][col]
    if is_goal(cell):
        print(f"Goal reached at {position}")
        break

    score = heuristic(position, goal)
  
    if best_score is None or score < best_score:
        best_score = score
        best_action = action


print("valid moves:", valid_moves)
print(f"Best Move {best_action}  Best score {best_score}")





