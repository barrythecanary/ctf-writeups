# sudoku - Writeup

| Author           | Title             | Category   | Difficulty |
|------------------|-------------------|------------|------------|
| barrythecanary | sudoku | nyt | - |

I played solo as the team [ZHAW Cooks](https://umdctf.io/profile/6a602420-0ed3-4bcc-9dae-7b1d5b5837d4).

## Description

try this numbers game, minus the math

`nc challs.umdctf.io 31602`

## Solution

I connected with netcat and was asked for an input. I just typed in 10 and was greeted by a gigantic if condition. Overall It seems to check each digit of the input for specific conditions.

Based on that I probably need to write a program that can give me a number that satisfies every constraint. Solving for a number using z3 would in this case be the most straighforward solution.

 To make it a little more readable I copied it and used a Python script to list each condition seperately.

[parse_constraints.py](./parse_constraints.py)
```
def parse_constraints(constraints_str):
    components = constraints_str.split()
    
    constraints = []
    for i in range(0, len(components) - 2, 2):
        left = components[i]
        operator = components[i+1]
        right = components[i+2]
        constraints.append(f"{left} {operator} {right}")
    
    return constraints

def save_to_file(constraints, filename="constraints.txt"):
    with open(filename, "w") as file:
        for constraint in constraints:
            file.write(constraint + "\n")
    print(f"Saved {len(constraints)} constraints to '{filename}'")

constraints_input = "huge constraint" # copy paste constraint from error msg
save_to_file(parse_constraints(constraints_input))
```

Afterwards I used the z3 library to solve the constraints for me with another script. This script essentially loaded in all the statements and tried to find numbers for each s\[n\] that would satisfy the conditions.

[constraints_solver.py](./constraint_solver.py)
```
from z3 import *

solver = Solver()
s = [Int(f's_{i}') for i in range(81)]

for var in s:
    solver.add(var >= 0, var <= 9)

constraint_file_path = 'constraints.txt'

with open(constraint_file_path, 'r') as file:
    for line in file:
        line = line.strip()
        try:
            solver.add(eval(line))
        except:
            print(f"Error can't eval line {line}")
            exit()

if solver.check() == sat:
    model = solver.model()
    result = [str(model.evaluate(s[i]).as_long()) for i in range(81)]
    output = ''.join(result)
    print(f"Solution: {output}")
else:
    print("No solution found.")
```

This outputted me the following solution number:

`224945891227236799775446158763132236157152174561681439614389755963829948537883684`

Inputting it into the sudoku program gave me the flag:

`UMDCTF{has_operator_chaining_gone_too_far}`