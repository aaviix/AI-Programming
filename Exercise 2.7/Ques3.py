## Author : 22200727
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
