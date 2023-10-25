## Author : 22200727
## Question 5
# Can you modify 4. so that it works for strings?

def rotateRx(my_string):
    last_element = my_string[-1]  # Get the last element or character
    my_string = last_element + my_string[:-1]  # Rotate to the right
    return my_string

s = "Hello"
s = rotateRx(s)
print(s)  # Output: "oHell"
