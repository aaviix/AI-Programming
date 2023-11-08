## Author : 22200727

import bfs
## Breath First Search
# boardSize = 7 = 40 solutions
boardSize = 8  # 92 solutions
# boardSize = 9 = 352 solutions
# boardSize = 10 = 724 solutions


def isGoal(boardState):
    return len(boardState) == boardSize


def nextStates(boardState):
    nextStates = []

    for yPos in range(boardSize):
        if isValidPosition(yPos, boardState):
            nextStates.append(boardState+[yPos])
    return nextStates


def isValidPosition(posY, boardState):
    posX = len(boardState)

    for queenX, queenY in enumerate(boardState):
        if queenY == posY:
            return False

        # I don't need abs() because I know posX will always be bigger than queenX
        distanceX = posX - queenX
        distanceY = abs(posY - queenY)
        distanceYIfDiagonal = distanceX

        if distanceYIfDiagonal == distanceY:
            return False
    return True


path = bfs.BreadthFirstSearch(isGoal, nextStates)
solution = path[-1]
print("Path:", path)
print("SOLUTION:", solution)
