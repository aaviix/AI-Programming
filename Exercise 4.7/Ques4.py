## Author : 22200727
##  Use backtracking to calculate the number of all paths from the bottom left to the top right corner in a x × y102 4.9 Exercises grid. This includes path like Note that every point can only be visited once. Write a function np(x,y) that returns the number of paths in a x × y-grid. E.g. np(2,3) should return 38.

def np(x, y):

    # I add one so that each state represents a point in the grid
    x += 1
    y += 1

    def backtrack(current_Row, current_Column, visited):
        if current_Row == x-1 and current_Column == y-1:  # Check if its the goal
            return 1

        visited[current_Row][current_Column] = True
        count = 0

        for x_offset, y_offset in [(1, 0), (0, 1), (-1, 0), (0, -1)]:  # checking up, right, left and down
            new_i, new_j = current_Row + x_offset, current_Column + y_offset

            if 0 <= new_i < x and 0 <= new_j < y and not visited[new_i][new_j]:  # Check if its in bounds and not visited
                count += backtrack(new_i, new_j, visited)  # Moving

        visited[current_Row][current_Column] = False 
        return count # the number of paths

    visited = [[False for _ in range(y)] for _ in range(x)]
    return backtrack(0, 0, visited)


result = np(2, 3) # desired output is 38
print(result)
