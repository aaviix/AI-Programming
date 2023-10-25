# 22200727, 22201100,

import copy


def isGoal(s):
    for row in s:
        if 0 in row:
            return False
    return True


def find_empty_cell(s):
    for row in range(len(s)):
        for col in range(len(s[row])):
            if s[row][col] == 0:
                return row, col


def nextStates(s):
    i, j = find_empty_cell(s)
    return [fill(s, i, j, n) for n in range(1, 10) if allowed(s, i, j, n)]


def fill(s, i, j, n):
    new_s = copy.deepcopy(s)
    new_s[i][j] = n
    return new_s


def check_line(s, row, n):
    if n in s[row]:
        return True
    else:
        return False


def check_box(s, row, col, n):
    row = (row // 3)*3
    col = (col // 3)*3
    for i in range(row, row+3):
        for j in range(col, col+3):
            if s[i][j] == n:
                return True
    return False


def allowed(s, i, j, n):
    if check_line(s, i, n):
        return False
    elif check_line(transpose(s), j, n):
        return False
    elif check_box(s, i, j, n):
        return False
    else:
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
    toDo = [[s]]
    while len(toDo) != 0:
        path = toDo.pop(-1)
        current = path[-1]
        if isGoal(current):
            return path[-1]
        for state in nextStates(current):
            if find_state(state, path, toDo):
                new_path = list(path)
                new_path.append(state)
                toDo.append(new_path)


def transpose(matrix):
    transposed_matrix = [[row[i] for row in matrix]
                         for i in range(len(matrix[0]))]
    return transposed_matrix


def print_sudoku(grid):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(grid[i][j], end=" ")
        print()


grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 0, 0]]
result = BreadthFirstSearch(grid)
print_sudoku(result)
