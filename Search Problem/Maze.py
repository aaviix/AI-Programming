# 22200849, 22207839, 22211514

maze = [[' ', 'W', ' ', ' ', 'G'],
        [' ', 'W', ' ', 'W', ' '],
        [' ', 'W', ' ', ' ', ' '],
        [' ', ' ', 'W', 'W', ' '],
        [' ', ' ', ' ', ' ', ' ']]

rows = len(maze)
cols = len(maze[0])


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
        path = toDo.pop(0)
        current = path[-1]
        if isGoal(current):
            return path
        for state in nextStates(current):
            if find_state(state, path, toDo):
                new_path = list(path)
                new_path.append(state)
                toDo.append(new_path)
    raise Exception("FAILURE: NO PATH FOUND")


directions = {
    'Up': [-1, 0],
    'Down': [1, 0],
    'Left': [0, -1],
    'Right': [0, 1],
}


def isGoal(s):
    i, j = s
    return maze[i][j] == 'G'


def nextStates(s):
    dirs = ['Up', 'Down', 'Left', 'Right']
    return [move(s, d) for d in dirs if allowed(s, d)]


def move(s, d):
    moveI, moveJ = directions[d]
    i, j = s
    return [i + moveI, j + moveJ]


def allowed(s, d):
    moveI, moveJ = directions[d]
    i, j = s
    if i + moveI >= cols or i + moveI < 0:
        return False
    elif j + moveJ >= rows or j + moveJ < 0:
        return False
    elif maze[i + moveI][j + moveJ] == 'W':
        return False
    else:
        return True


print(BreadthFirstSearch([0, 0]))
