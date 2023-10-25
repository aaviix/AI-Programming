## Author : 22200727
## Question 4
# Define a function rotateRx that rotates a list to the right in-place:

def rotateRx(my_list):
    if my_list:
        last_element = my_list.pop()  # Remove the last element
        my_list.insert(0, last_element)  # Insert the last element at the beginning

l = [1, 2, 3, 4]
rotateRx(l)
print(l)  # Output: [4, 1, 2, 3]
