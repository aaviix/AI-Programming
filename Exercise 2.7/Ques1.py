## Author : 22200727
## Question 1. 
# Define a function rotateR for strings:

def rotateR(s):
    return s[-1] + s[:-1]
    
# Example usage:
result1 = rotateR("Thor")
print(result1)  # Output: "rTho"
