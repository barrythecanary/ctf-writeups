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
