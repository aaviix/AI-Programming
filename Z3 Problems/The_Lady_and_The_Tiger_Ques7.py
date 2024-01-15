## Author : 22200727
# Ques 7.

from z3 import *

def solve_puzzle_new_logic():
    r1, r2 = Bools("r1 r2")
    # r1, r2 True means there is a lady in room 1, 2 respectively
    # r1, r2 False means tiger!

    s = Solver()

    # Based on new interpretation:
    # Room II must contain a tiger
    s.add(Not(r2))

    # Since Room II contains a tiger, Sign II is true, so Room I must contain a lady
    s.add(r1)

    if s.check() == sat:
        m = s.model()
        room1 = m[r1]
        room2 = m[r2]
        return f"Room 1 contains {'a lady' if is_true(room1) else 'a tiger'}, Room 2 contains {'a tiger' if is_true(room2) else 'a lady'}"
    else:
        return "No solution found"

# Execute the function
result = solve_puzzle_new_logic()
print(result)
