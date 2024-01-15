## Author : 22200727
# Ques 5. 

from z3 import *

def solve_puzzle_with_revised_logic():
    r1, r2 = Bools("r1 r2")
    # r1, r2 True means there is a lady in room 1, 2 respectively
    # r1, r2 False means tiger!

    # Define the signs
    # Sign 1: At least one is true: Tiger in Room I or Lady in Room II
    sign1 = Or(Not(r1), r2)  
    
    # Sign 2: If there is a tiger in Room II, then Room I contains a lady
    sign2 = Implies(Not(r2), r1)  

    s = Solver()

    # Add constraints based on the logic provided
    # It's impossible for Room I to contain a tiger, so Room I must contain a lady
    s.add(r1)

    # Since Room I contains a lady, we check the condition of Room II
    s.add(sign2)

    if s.check() == sat:
        m = s.model()
        room1 = m[r1]
        room2 = m[r2]
        return f"Room 1 contains {'a lady' if room1 else 'a tiger'}, Room 2 contains {'a lady' if room2 else 'a tiger'}"
    else:
        return "No solution found"

# Execute the function
result = solve_puzzle_with_revised_logic()
print(result)
