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

constraints_input = "s[69] == s[68] > s[58] == s[26] > s[18] == s[43] > s[28] == s[48] == s[78] > s[5] == s[62] == s[72] > s[70] == s[51] == s[2] > s[31] == s[57] > s[41] == s[10] > s[24] == s[55] == s[36] == s[39] > 0 != s[45] != 0 != s[30] != 0 != s[32] != 0 != s[42] != 0 != s[16] != 0 != s[80] != 0 != s[44] != 0 != s[8] != 0 != s[72] != 0 != s[43] != 0 != s[4] != 0 != s[12] != 0 != s[78] != 0 != s[79] != 0 != s[66] != 0 != s[62] != 0 != s[41] != 0 != s[25] != 0 != s[31] != 0 != s[34] != 0 != s[1] != 0 != s[77] != 0 != s[69] != 0 != s[68] != 0 != s[5] != 0 != s[11] != 0 != s[18] != 0 != s[65] != 0 != s[59] != 0 != s[3] != 0 != s[55] != 0 != s[73] != 0 != s[39] != 0 != s[21] != 0 != s[76] != 0 != s[54] != 0 != s[22] != 0 != s[27] != 0 != s[60] != 0 != s[67] != 0 != s[61] != 0 != s[63] != 0 != s[19] != 0 != s[9] != 0 != s[6] != 0 != s[57] != 0 != s[50] != 0 != s[29] != 0 != s[52] != 0 != s[14] != 0 != s[49] != 0 != s[53] != 0 != s[64] != 0 != s[13] != 0 != s[36] != 0 != s[74] != 0 != s[15] != 0 != s[7] != 0 != s[47] != 0 != s[2] != 0 != s[26] != 0 != s[37] != 0 != s[10] != 0 != s[28] != 0 != s[51] != 0 != s[71] != 0 != s[17] != 0 != s[75] != 0 != s[24] != 0 != s[33] != 0 != s[70] != 0 != s[35] != 0 != s[46] != 0 != s[58] != 0 != s[56] != 0 != s[48] != 0 != s[38] != 0 != s[20] != 0 != s[0] != 0 != s[40] != 0 != s[23] != s[31] != s[53] != s[43] != s[24] != s[48] != s[74] != s[50] != s[29] != s[42] != s[7] != s[29] != s[44] != s[68] != s[67] != s[37] != s[48] != s[22] != s[28] != s[72] != s[13] != s[67] != s[65] != s[61] != s[35] != s[59] != s[54] != s[18] != s[53] != s[6] != s[72] != s[76] != s[64] != s[7] != s[33] != s[43] != s[61] != s[49] != s[65] != s[43] != s[37] != s[1] != s[65] != s[6] != s[31] != s[2] != s[9] != s[73] != s[60] != s[25] != s[26] != s[78] != s[76] != s[70] != s[16] != s[12] != s[17] != s[57] != s[48] != s[43] != s[35] != s[15] != s[80] != s[69] != s[52] != s[46] != s[63] != s[25] != s[17] != s[2] != s[66] != s[52] != s[9] != s[59] != s[8] != s[35] != s[67] != s[51] != s[55] != s[14] != s[75] != s[4] != s[14] != s[10] != s[5] != s[66] != s[47] != s[31] != s[43] != s[64] != s[44] != s[11] != s[2] != s[3] != s[52] != s[30] != s[27] != s[35] != s[32] != s[8] != s[20] != s[46] != s[4] != s[36] != s[71] != s[59] != s[5] != s[56] != s[17] != s[50] != s[25] != s[47] != s[11] != s[28] != s[30] != s[13] != s[7] != s[28] != s[42] != s[1] != s[25] != s[19] != s[71] != s[60] != s[8] != s[34] != s[64] != s[30] != s[76] != s[29] != s[41] != s[70] != s[15] != s[13] != s[60] != s[33] != s[71] != s[23] != s[2] != s[57] != s[78] != s[69] != s[33] != s[64] != s[79] != s[20] != s[44] != s[75] != s[30] != s[11] != s[3] != s[72] != s[15] != s[79] != s[41] != s[36] != s[32] != s[44] != s[71] != s[34] != s[50] != s[78] != s[12] != s[2] != s[73] != s[33] != s[8] != s[49] != s[24] != s[17] != s[21] != s[40] != s[30] != s[4] != s[72] != s[31] != s[40] != s[65] != s[8] != s[18] != s[75] != s[53] != s[14] != s[18] != s[4] != s[41] != s[17] != s[18] != s[23] != s[9] != s[71] != s[68] != s[55] != s[64] != s[32] != s[29] != s[75] != s[3] != s[23] != s[56] != s[25] != s[42] != s[32] != s[28] != s[10] != s[53] != s[4] != s[11] != s[0] != s[61] != s[27] != s[69] != s[25] != s[57] != s[58] != s[16] != s[50] != s[71] != s[13] != s[68] != s[1] != s[24] != s[41] != s[19] != s[78] != s[73] != s[39] != s[53] != s[37] != s[70] != s[13] != s[36] != s[20] != s[15] != s[49] != s[48] != s[77] != s[17] != s[8] != s[12] != s[19] != s[59] != s[20] != s[41] != s[76] != s[21] != s[16] != s[61] != s[44] != s[60] != s[62] != s[66] != s[22] != s[49] != s[35] != s[51] != s[49] != s[53] != s[40] != s[9] != s[27] != s[31] != s[11] != s[29] != s[37] != s[12] != s[18] != s[69] != s[2] != s[5] != s[18] != s[10] != s[4] != s[28] != s[9] != s[50] != s[46] != s[16] != s[48] != s[58] != s[0] != s[72] != s[10] != s[13] != s[79] != s[34] != s[9] != s[66] != s[17] != s[45] != s[75] != s[7] != s[15] != s[59] != s[50] != s[12] != s[74] != s[65] != s[51] != s[79] != s[33] != s[80] != s[78] != s[56] != s[57] != s[26] != s[80] != s[20] != s[4] != s[3] != s[31] != s[67] != s[36] != s[7] != s[51] != s[58] != s[63] != s[13] != s[54] != s[66] != s[8] != s[80] != s[47] != s[23] != s[69] != s[47] != s[73] != s[4] != s[79] != s[7] != s[44] != s[28] != s[66] != s[40] != s[55] != s[79] != s[43] != s[68] != s[40] != s[6] != s[27] != s[16] != s[26] != s[17] != s[76] != s[15] != s[36] != s[60] != s[67] != s[53] != s[24] != s[77] != s[51] != s[27] != s[22] != s[53] != s[73] != s[18] != s[57] != s[50] != s[26] != s[37] != s[58] != s[25] != s[12] != s[26] != s[70] != s[63] != s[45] != s[70] != s[12] != s[29] != s[28] != s[52] != s[22] != s[24] != s[45] != s[19] != s[56] != s[71] != s[67] != s[49] != s[68] != s[61] != s[77] != s[19] != s[23] != s[34] != s[33] != s[59] != s[34] != s[51] != s[43] != s[62] != s[59] != s[32] != s[75] != s[11] != s[6] != s[74] != s[70] != s[29] != s[46] != s[12] != s[54] != s[60] != s[26] != s[56] != s[58] != s[77] != s[1] != s[48] != s[53] != s[27] != s[40] != s[0] != s[47] != s[3] != s[6] != s[39] != s[40] != s[1] != s[14] != s[27] != s[28] != s[69] != s[30] != s[70] != s[42] != s[41] != s[52] != s[11] != s[32] != s[13] != s[61] != s[67] != s[24] != s[37] != s[21] != s[74] != s[1] != s[6] != s[47] != s[5] != s[50] != s[37] != s[16] != s[1] != s[55] != s[6] != s[21] != s[65] != s[32] != s[15] != s[10] != s[30] != s[22] != s[37] != s[31] != s[39] != s[77] != s[78] != s[21] != s[58] != s[42] != s[46] != s[76] != s[77] != s[16] != s[39] != s[75] != s[28] != s[3] != s[79] != s[52] != s[10] != s[64] != s[72] != s[47] != s[9] != s[69] != s[22] != s[6] != s[68] != s[51] != s[16] != s[29] != s[45] != s[32] != s[7] != s[62] != s[80] != s[49] != s[32] != s[20] != s[7] != s[55] != s[35] != s[16] != s[24] != s[78] != s[60] != s[69] != s[26] != s[74] != s[77] != s[35] != s[65] != s[14] != s[22] != s[39] != s[10] != s[73] != s[14] != s[74] != s[46] != s[38] != s[52] != s[20] != s[35] != s[39] != s[51] != s[64] != s[62] != s[34] != s[7] != s[45] != s[11] != s[23] != s[66] != s[12] != s[56] != s[63] != s[29] != s[26] != s[73] != s[5] != s[23] != s[72] != s[63] != s[30] != s[15] != s[44] != s[79] != s[38] != s[76] != s[45] != s[21] != s[41] != s[46] != s[37] != s[74] != s[24] != s[19] != s[34] != s[54] != s[36] != s[79] != s[32] != s[80] != s[71] != s[61] != s[55] != s[74] != s[58] != s[1] != s[38] != s[42] != s[45] != s[77] != s[27] != s[39] != s[14] != s[6] != s[23] != s[0] != s[22] != s[43] != s[55] != s[65] != s[15] != s[8] != s[62] != s[12] != s[57] != s[38] != s[4] != s[39] != s[18] != s[9] != s[5] != s[75] != s[52] != s[27] != s[58] != s[35] != s[80] != s[54] != s[71] != s[5] != s[53] != s[0] != s[3] != s[46] != s[79] != s[62] != s[54] != s[17] != s[62] != s[33] != s[47] != s[2] != s[6] != s[0] != s[39] != s[61] != s[60] != s[47] != s[78] != s[41] != s[77] != s[0] != s[16] != s[74] != s[29] != s[38] != s[58] != s[39] != s[5] != s[19] != s[21] != s[48] != s[63] != s[38] != s[56] != s[34] != s[60] != s[80] != s[34] != s[55] != s[21] != s[24] != s[31] != s[49] != s[55] != s[62] != s[51] != s[33] != s[78] != s[17] != s[19] != s[76] != s[24] != s[58] != s[61] != s[51] != s[0] != s[14] != s[5] != s[4] != s[52] != s[72] != s[75] != s[42] != s[63] != s[41] != s[3] != s[20] != s[13] != s[76] != s[63] != s[15] != s[64] != s[36] != s[68] != s[21] != s[1] != s[56] != s[59] != s[49] != s[37] != s[77] != s[21] != s[14] != s[40] != s[52] != s[36] != s[61] != s[54] != s[57] != s[8] != s[54] != s[67] != s[55] != s[33] != s[25] != s[48] != s[38] != s[25] != s[78] != s[45] != s[46] != s[36] != s[3] != s[30] != s[9] != s[19] != s[57] != s[66] != s[73] != s[69] != s[40] != s[28] != s[45] != s[38] != s[70] != s[10] != s[76] != s[42] != s[44] != s[54] != s[2] != s[62] != s[18] != s[47] != s[26] != s[46] != s[70] != s[64] != s[13] != s[44] != s[45] != s[41] != s[38] != s[20] != s[49] != s[43] != s[7] != s[11] != s[42] != s[57] != s[1] != s[63] != s[64] != s[20] != s[65] != s[68] != s[35] != s[0] != s[2] != s[72] != s[30] != s[66] != s[69] != s[5] != s[34] != s[43] != s[67] != s[22] != s[9] != s[56] != s[42] != s[48] != s[31] != s[22] != s[40] != s[74] != s[68] != s[14] != s[31] != s[0] != s[27] != s[66] != s[18] != s[2] != s[8] != s[71] != s[62] != s[57] != s[63] != s[10] != s[11] != s[72] != s[70] != s[50] != s[19] != s[26] != s[33] != s[54] != s[68] != s[60] != s[59] != s[65] != s[80] != s[73] != s[23] != s[50] != s[56] != s[48] != s[67] != s[44] != s[36] != s[38] != s[3] != s[10] != s[75] != s[73] != s[25] != s[80] != s[59] != s[23]"
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