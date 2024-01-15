## Author : 22200727
# Ques 3.

from z3 import *

def solve_puzzle_with_generous_king():
    r1, r2 = Bools("r1 r2")
    # r1, r2 True means there is a lady in room 1, 2 respectively
    # r1, r2 False means tiger!

    # Define the signs
    sign1 = Or(Not(r1), r2)  # At least one: Tiger in Room I or Lady in Room II
    sign2 = r1  # Lady in Room I

    s = Solver()

    # Add constraints that both signs are true
    s.add(sign1, sign2)

    if s.check() == sat:
        m = s.model()
        room1 = m[r1]
        room2 = m[r2]
        return f"Room 1 contains {'a lady' if room1 else 'a tiger'}, Room 2 contains {'a lady' if room2 else 'a tiger'}"
    else:
        return "No solution found"

# Execute the function
result = solve_puzzle_with_generous_king()
print(result)
