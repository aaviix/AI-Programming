## Author : 22200727
## Question 2
# Define a function rotateL for lists:

def rotateL(lst):
    return lst[1:] + [lst[0]]

# Example usage:
result2 = rotateL([1, 2, 3, 4])
print(result2)  # Output: [2, 3, 4, 1]
