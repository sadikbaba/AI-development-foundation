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

print(grid[0][0])
