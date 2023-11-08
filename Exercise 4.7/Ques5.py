## Author : 22200727
## Question 5
# Implement a Python function that solves the 8 queens puzzle. The 8 queen puzzle consists of placing 8 queens on a chess board, so that, none of the queens could capture any other. Note that queens can move orthogonally or diagonally in any direction. E.g. a possible solution looks like this:
##QZ0Z0Z0Z Z0Z0L0Z0 0Z0Z0Z0L Z0Z0ZQZ0 0ZQZ0Z0Z Z0Z0Z0L0 0L0Z0Z0Z Z0ZQZ0Z0
#You should implement a function solve() that when called, it prints the first solution of the puzzle and then it awaits for input. Once the user presses ’enter’, the next solution is printed and so on. Hence solve() should produce: 103 4 Recursion and backtracking
#Q . . . . . . . . . . . Q . . . . . . . . . . Q . . . . . Q . . . . Q . . . . . . . . . . . Q . . Q . . . . . . . . . Q . . . . more?
#• Your program should be able to find all the solutions for the puzzle and each solution only once.
#• It should be easy to modify your program, so that, it works for different board sizes.

# boardSize = 7 # 40 solutions
boardSize = 8  # 92 solutions
# boardSize = 9 # 352 solutions
# boardSize = 10 # 724 solutions
debugOnlySOlutionCount = False


def solve():
    solution = []
    allSolutions = []
    solveRecursivly(solution, allSolutions)

    if debugOnlySOlutionCount:
        print("Board size: " + str(boardSize))
        print("Solutions: " + str(len(allSolutions)))
    else:
        for displaySolution in allSolutions:
            for y in range(boardSize):
                for x in range(boardSize):
                    if displaySolution[x] == y:
                        print("Q  ", end="")
                    else:
                        print(".  ", end="")
                print()
            input("more?")
            for _ in range(20):  # clear screen
                print()


def getNextStates(solutionInProgress):
    nextQueenX = len(solutionInProgress)
    possibleNextYStates = list(range(boardSize))

    for queenX, queenY in enumerate(solutionInProgress):

        if queenY in possibleNextYStates:
            possibleNextYStates.remove(queenY)  # remove same row

        distX = nextQueenX - queenX
        # distance of x vaules is the same as distance of y values for diagonals
        distYIfDiagonal = distX

        diagonalY1 = queenY - distYIfDiagonal
        # (1, -1) is the diagonal up right, thats why -diagonal
        if diagonalY1 in possibleNextYStates:
            possibleNextYStates.remove(diagonalY1)

        diagonalY2 = queenY + distYIfDiagonal
        # (xDist, xDist) is the diagonal right down
        if diagonalY2 in possibleNextYStates:
            # (1, 1) is the diagonal down right , thats why +diagonal
            possibleNextYStates.remove(diagonalY2)

    return possibleNextYStates


def solveRecursivly(solution, allSolutions):
    if len(solution) == boardSize:  # base case
        allSolutions.append(solution[:])
        return

    for nextY in getNextStates(solution):
        solution.append(nextY)
        solveRecursivly(solution, allSolutions)
        solution.pop()  # backtracking


solve()
