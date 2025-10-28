import math
import sys
import ast
import numpy as np

# Copy your code for input_row(prompt) from exercise1.py here.
def input_row(x):
    try:
        S = input(x)
        L = ast.literal_eval(S)
        V = []
        for i in L:
            V.append(float(i))
        return V
    except Exception:
        return []
# Put your code for input_matrix(row) here.
def input_matrix(num_row):
    matrix = []
    for i in range(num_row):
        row = input_row(f"input row {i+1} of the matrix: ")
        print(row)
        matrix.append(row)

    return np.array(matrix)

#
# This is test code. Leave this code in so you can test input_row.
# if it works, you will see nothing but the prompt strings.
#
if __name__ == "__main__":
    with open("tmp.txt", "w") as f:
        f.write("[4]\n")
        f.write("1.1, 2.3, 4.5\n")
        f.write("4.4, 5.1, 6.8\n")
        f.write("1.9, 2.8, 3.7\n")
    console = sys.stdin
    sys.stdin = open('tmp.txt', 'r')
    x = input_matrix(1)
    if x[0][0] != 4:
        print("ERROR")
    
    x = input_matrix(3)
    v = [[1.1, 2.3, 4.5], [4.4, 5.1, 6.8], [1.9, 2.8, 3.7]]
    for i in range(3):
        for j in range(3):
            if not math.isclose(x[i][j], v[i][j]):
                print("ERROR")

    sys.stdin.close()
    sys.stdin = console