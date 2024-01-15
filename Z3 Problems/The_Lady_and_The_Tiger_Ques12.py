## Author : 22200727
# Ques 12.

from z3 import *

def solve_king_puzzle():
    # Rooms (True for lady, False for tiger or empty)
    r1, r2, r3, r4, r5, r6, r7, r8, r9 = Bools("r1 r2 r3 r4 r5 r6 r7 r8 r9")
    
    s = Solver()

    # Apply given information and deductions
    # Room VIII contains a tiger (False), so Sign VIII is false
    s.add(r8 == False)
    
    # Room IX is not empty and does not contain the lady, so it's false (tiger or empty)
    s.add(r9 == False)

    # Sign VI must be true
    # Sign III is false, implying Sign V is false and Sign VII is true
    # Signs II and IV are false
    # Sign I is true
    s.add(Implies(r6, r3) == True)  # Sign VI
    s.add(Implies(r3, r5) == False) # Sign III
    s.add(r5 == False)              # Sign V
    s.add(Implies(r7, r5) == True)  # Sign VII
    s.add(Implies(r2, r4) == False) # Sign II
    s.add(Implies(r4, r1) == False) # Sign IV
    s.add(r1 == True)               # Sign I is true

    # Lady is in either Room I, VI, or VII
    s.add(Or(r1, r6, r7))

    if s.check() == sat:
        m = s.model()
        rooms = [m[room] for room in [r1, r2, r3, r4, r5, r6, r7, r8, r9]]
        return rooms
    else:
        return "No solution found"

# Execute the function
rooms_containing_lady = solve_king_puzzle()
rooms_containing_lady

