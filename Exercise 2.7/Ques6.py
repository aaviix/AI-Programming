## Author : 22200727
## Question 6
# Write a function rotateR2 that gets a string as an argument and returns the string rotated to the left twice, using only the function rotateR from the 1st exercise. E.g. rotateR2("Thor") should return 'orTh'.

def rotateR2(s):
    return rotateR(rotateR(s))

# Example usage:
result = rotateR2("Thor")
print(result)  # Output: "orTh"
