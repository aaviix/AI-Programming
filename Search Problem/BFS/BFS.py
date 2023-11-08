def BreadthFirstSearch(isGoal, nextStates, state=[]):
    toDo = [[state]]  # Initialize a list with the initial state as a path

    while toDo:
        path = toDo.pop(0)  # Dequeue the first path
        # Last element of path is the current state to explore
        current = path[-1]

        if isGoal(current):  # Use the isGoal function passed as argument
            return path

        for state in nextStates(current):
            for todoPath in toDo:
                if state in todoPath:
                    continue
            if state not in path:
                toDo.append(path + [state])
    raise Exception("FAILURE: NO PATH FOUND")
