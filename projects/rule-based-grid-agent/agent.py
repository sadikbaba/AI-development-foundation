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


# The agent's current position is stored as a row and column coordinate


def agent_position(row, col):
    return (row, col)


print(agent_position(0, 0))

row = 2
col = 2

up = (row - 1, col)
down = (row + 1, col)
left = (row, col - 1)
right = (row, col + 1)

print("UP", up)
print("DOWN", down)
print("LEFT", left)
print("RIGHT", right)


up_cell = grid[up[0]][up[1]]
down_cell = grid[down[0]][down[1]]
left_cell = grid[left[0]][left[1]]
right_cell = grid[right[0]][right[1]]


def is_valid_move(cell):
    return cell != "#"


def is_goal(cell):
    return cell == "G"


print(is_valid_move(right_cell))


def heuristic(current, goal):
    current_row = current[0]
    current_col = current[1]
    goal_row = goal[0]
    goal_col = goal[1]
    return abs(current_row - goal_row) + abs(current_col - goal_col)

    
print(heuristic((2, 3), (3, 3)))
print(heuristic((1, 1), (3, 3)))