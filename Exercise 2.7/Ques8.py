## Author : 22200727
## Question 8
# Can you create a list l that prints as [[1, 2, 3], [1, 2, 3]] but when I rotate only the first part by rotateRx(l[1]) and then print l it turns out that both parts have been rotated, i.e. I get [[3, 1, 2], [3, 1, 2]]

# Initial list
l = [[1, 2, 3], [1, 2, 3]]

# Rotating the first part of the list using rotateRx
rotateRx(l[0])

# Printing the modified list
print(l)  # Output: [[3, 1, 2], [1, 2, 3]]
