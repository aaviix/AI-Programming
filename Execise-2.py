## Question 1. 
# Define a function rotateR for strings:

def rotateR(s):
    return s[-1] + s[:-1]
    
# Example usage:
result1 = rotateR("Thor")
print(result1)  # Output: "rTho"

## Question 2
# Define a function rotateL for lists:

def rotateL(lst):
    return lst[1:] + [lst[0]]

# Example usage:
result2 = rotateL([1, 2, 3, 4])
print(result2)  # Output: [2, 3, 4, 1]

## Question 3
# Do both functions work for lists and strings? If not, how can you fix that?

#Modified rotateR for strings and lists:

def rotateR(input_data):
    if isinstance(input_data, str):
        return input_data[-1] + input_data[:-1]
    elif isinstance(input_data, list):
        return input_data[-1] + input_data[:-1]
    else:
        return "Invalid input type"

# Example usage:
result_str = rotateR("Thor")
print(result_str)  # Output: "rTho"

result_list = rotateR([1, 2, 3, 4])
print(result_list)  # Output: [4, 1, 2, 3]

#Modified rotateL for strings and lists:

def rotateL(input_data):
    if isinstance(input_data, list):
        return input_data[1:] + [input_data[0]]
    elif isinstance(input_data, str):
        return input_data[1:] + input_data[0]
    else:
        return "Invalid input type"

# Example usage:
result_str = rotateL("Thor")
print(result_str)  # Output: "horT"

result_list = rotateL([1, 2, 3, 4])
print(result_list)  # Output: [2, 3, 4, 1]

## Question 4
# Define a function rotateRx that rotates a list to the right in-place:

