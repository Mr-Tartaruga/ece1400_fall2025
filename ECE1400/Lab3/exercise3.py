import math
import ast

# Put your code for write_matrix(matrix) here.
def write_matrix(mat, file_name):
    f = open(file_name , "w")
    for row in mat:
        # issue with reading in the values. Need to ensure that 'flat_row' is a tuple of floats
        flat_row = tuple(float(x) for x in row) # flat_row, tuple of floats
        x = "%g , %g , %g\n" % tuple(float(x) for x in row)
        f.write(x)

    f.close()
#
# This is test code. Leave this code in so you can test write_matrix.
# if it works, the program will finish quietly without error.
#
if __name__ == "__main__":
    ''' Test Code. Create a matrix and write it to a file. Check that
        file to see it is correct. Print ERROR if anything is amiss.'''
    mat = [[1.1, 2.3, 3.5], [5.0, 4.0, 3.0], [6.6, 4.3, 1.2]]
    write_matrix(mat, "tmp.csv")
    with open("tmp.csv", "r") as f:
        s = f.readlines()
        for i in range(len(s)):
            t = ast.literal_eval(s[i].strip())
            for j in range(len(t)):
                if not math.isclose(t[j], mat[i][j]):
                    print("ERROR")