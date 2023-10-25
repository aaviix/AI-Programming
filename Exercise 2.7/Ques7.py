## Author : 22200727
## Question 7
#Write a function rotateRx2 that changes its parameter (a list) by rotating it twice to the right. The function should only use rotateRx from part 4. E.g. we assign l = [1,2,3,4] and then run rotateRx2(l) (which returns nothing). If we now check l it returns [3, 4, 1, 2].

def rotateRx2(lst):
    rotateRx(lst)
    rotateRx(lst)

# Example usage:
l = [1, 2, 3, 4]
rotateRx2(l)
print(l)  # Output: [3, 4, 1, 2]
