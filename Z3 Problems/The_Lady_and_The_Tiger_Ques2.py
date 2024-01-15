## Author : 22200727
# Ques 2.

from z3 import *

def solve_puzzle():
    r1, r2 = Bools("r1 r2")
    # r1, r2 True means there is a lady in room 1, 2 respectively
    # r1, r2 False means tiger!

    # Define the signs
    sign1 = r2  # Sign 1 says there's a lady in Room 2
    sign2 = Not(r1)  # Sign 2 says there's a tiger in Room 1

    s = Solver()

    # Add constraint that both signs are either true or false
    s.add(Or(And(sign1, sign2), And(Not(sign1), Not(sign2))))

    if s.check() == sat:
        m = s.model()
        room1 = m[r1]
        room2 = m[r2]
        return f"Room 1 contains {'a lady' if room1 else 'a tiger'}, Room 2 contains {'a lady' if room2 else 'a tiger'}"
    else:
        return "No solution found"

# Execute the function
result = solve_puzzle()
print(result)
