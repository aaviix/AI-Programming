## Author : 22200727

import bfs

## Breath First Search
N = 3
goal = [[i*N+j for j in range(N)] for i in range(N)]


def isGoal(state):
    return state == goal


def nextStates(state):
    i, j = None, None

    # FindING th empty one
    for row in range(N):
        for col in range(N):
            if state[row][col] == 0:
                i, j = row, col
                break

    # the directions
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    next_states = []

    for di, dj in dirs:
        new_i, new_j = i + di, j + dj

        # Check if the new position is within bounds
        if 0 <= new_i < N and 0 <= new_j < N:
            new_state = [row[:] for row in state]
            new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
            next_states.append(new_state)

    return next_states


if __name__ == "__main__":

    # initial_state = [[1, 0, 2], [3, 4, 5], [6, 7, 8]]

    # this one takes a lot of time to give the result
    initial_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    path = bfs.BreadthFirstSearch(isGoal, nextStates, initial_state)

    if path != "NO PATH FOUND":
        print("Path:")
        for state in path:
            print(state)

    else:
        print("NO PATH FOUND")
