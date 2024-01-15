## Author : 22200727
# Ques 10.

from z3 import *

def solve_three_room_puzzle():
    r1, r2, r3 = Bools("r1 r2 r3")
    # r1, r2, r3 True means there is a lady in room 1, 2, 3 respectively
    # r1, r2, r3 False means no lady

    s = Solver()

    # Add constraints based on the logic provided
    # The lady is in Room I
    s.add(r1)
    # Ensure at least one sign is false
    s.add(Or(Not(r2), Not(r3)))

    if s.check() == sat:
        m = s.model()
        room1 = m[r1]
        room2 = m[r2]
        room3 = m[r3]
        return (f"Room 1 contains {'a lady' if is_true(room1) else 'no lady'}, "
                f"Room 2 contains {'a lady' if is_true(room2) else 'no lady'}, "
                f"Room 3 contains {'a lady' if is_true(room3) else 'no lady'}")
    else:
        return "No solution found"

# Execute the function
result = solve_three_room_puzzle()
print(result)
