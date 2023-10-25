# 22200727, 22201100, 

# set board size
n = 8


def isGoal(s):
    return len(s) == n


def nextStates(s):
    return [s + [j] for j in range(n) if allowed(s, j)]


def allowed(s, j):
    next_ = len(s)
    if j in s:
        return False
    for col, row in enumerate(s):
        if abs(j - row) == abs(next_ - col):
            return False
    return True


def find_state(state, path, todo):
    sip = state in path
    if sip == True:
        return False
    for p in todo:
        if state in p:
            return False
    return True


def BreadthFirstSearch(s):
    solutions = []
    toDo = [[s]]
    while len(toDo) != 0:
        path = toDo.pop(0)
        current = path[-1]
        if isGoal(current):
            solutions.append(path[-1])
        for state in nextStates(current):
            if find_state(state, path, toDo):
                new_path = list(path)
                new_path.append(state)
                toDo.append(new_path)
    return solutions


def collect_solutions(n):
    ALL_SOLUTIONS = []
    for i in range(n):
        try:
            solutions = BreadthFirstSearch([i])
            ALL_SOLUTIONS += solutions
            for solution in solutions:
                # print(solution)
                pass
        except Exception:
            pass
    return ALL_SOLUTIONS


def showBoard(solution, show_bare=True):
    if show_bare == True:
        print(solution)
    else:
        display_chessboard(solution)


def display_chessboard(arr):
    n = len(arr)

    for row in range(n):
        print("|", end=" ")
        for col in range(n):
            if col == arr[row]:
                print("X |", end=" ")
            else:
                print("  |", end=" ")
        print()
        print("+---" * n + "+")

# array = [7, 3, 0, 2, 5, 1, 6, 4]
# display_chessboard(array)


def run_program(n):
    solutions = collect_solutions(n)
    for solution in solutions:
        showBoard(solution, show_bare=False)
        continue_showing = input("Want more? [Y/n]")
        if continue_showing.lower() == "y" or continue_showing.lower() == "":
            continue
        else:
            break


run_program(n)
