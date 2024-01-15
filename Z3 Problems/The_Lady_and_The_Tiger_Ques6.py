## Author : 22200727
# Ques 6.

from z3 import *

def solve_puzzle_latest_logic():
    r1, r2 = Bools("r1 r2")
    # r1, r2 True means there is a lady in room 1, 2 respectively
    # r1, r2 False means tiger!

    s = Solver()

    # Add constraints based on the logic provided
    # Room II must contain a lady regardless of Room I
    s.add(r2)

    # Since Room II contains a lady, Sign II is false
    # Therefore, Room I must contain a tiger
    s.add(Not(r1))

    if s.check() == sat:
        m = s.model()
        room1 = m[r1]
        room2 = m[r2]
        return f"Room 1 contains {'a lady' if room1 else 'a tiger'}, Room 2 contains {'a lady' if room2 else 'a tiger'}"
    else:
        return "No solution found"

# Execute the function
result = solve_puzzle_latest_logic()
print(result)
