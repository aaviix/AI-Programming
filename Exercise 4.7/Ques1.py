## Author : 22200727
## Question 1
# Write a recursive function rev that reverses a list, e.g. rev([1,2,3]) should return [3,2,1]. You can analyse the problem by considering the case that the list is empty and that the list is non-empty. In the latter one you can use recursion to solve the problem. Can you write your function so that it works for strings as well?

def rev(data):
    # Base case: if the list or string is empty, return it as is
    if len(data) <= 1:
        return data
    # Recursive case: reverse the rest of the list and concatenate the first element at the end
    return rev(data[1:]) + [data[0]]

# Example usage for lists:
result_list = rev([1, 2, 3])
print(result_list)  # Output: [3, 2, 1]

# Example usage for strings:
result_string = rev("Hello")
print(result_string)  # Output: "olleH"
