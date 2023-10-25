## Author : 22200727
## Question 6
# Write a function rotateR2 that gets a string as an argument and returns the string rotated to the left twice, using only the function rotateR from the 1st exercise. E.g. rotateR2("Thor") should return 'orTh'.

import importlib

rotateR = getattr(importlib.import_module("1"), "rotateR")

def rotateR2(s):
    return rotateR(rotateR(s))

print(rotateR2("Thor"))
