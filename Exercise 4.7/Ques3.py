## Author : 22200727
## Use recursion to calculate the number of shortest paths from the bottom left to the top right corner in an x × ygrid. E.g. shortest path in a 2 × 3-grid are: or Implement a function nsp with two parameters s.t. nsp(x,y) calculates the number of shortest paths in a x × y-grid. E.g. nsp(3,2) should return 10.

def recursion(currentPostion,destination):
    if currentPostion == destination:
        return 1
    
    x,y = currentPostion
    maxX = destination[0]
    
    pathCount1 = 0
    pathCount2 = 0
    
    if x < maxX:
        moveRight = (x+1,y)
        pathCount1 = recursion(moveRight,destination)
        
    if y > 0:
        moveUp = (x,y-1)
        pathCount2 = recursion(moveUp,destination)
        
    return pathCount1+pathCount2


def nsp(x,y):    
    return recursion((0,y),(x,0))
            
print(nsp(3,2))

