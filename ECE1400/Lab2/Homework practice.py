import numpy as np
import ast
import sys
'''
'''
def input_row(x):
    try:
        S = input(x)
        L = ast.literal_eval(S)
        if not isinstance(L, list):
            return []
        V = []
        for i in L:
            V.append(float(i))
            return V
    except Exception:
        return []
    

    if __name__ == "__main__":
        ''' Test Code. Create a file of responses then direct it to console
        input. Print ERROR if anything is amiss. '''
        with open("tmp.txt","w") as f:
            f.write("1.1, 2.3, 4.5\n")
            f.write("4.4, [5], {6}\n")
            f.write("4.4, 5.5\n")
            f.write("456 789 123\n")
            f.write("1.9, 2.8, 3.7\n")
        console = sys.stdin
        sys.stdin = open('tmp.txt','r')
        x = input_row("Input row 1: ")
        if x != [1.1, 2.3, 4.5]:
            print("ERROR")
        x = input_row("Input row 2: ")
        if x != []:
            print("ERROR")
        x = input_row("Input row 2: ")
        if x != [4.4, 5.5]:
            print("ERROR")
        x = input_row("Input row 3: ")
        if x != []:
            print("ERROR")
        x = input_row("Input row 3: ")
        if x != [1.9, 2.8, 3.7]:
            print("ERROR")
        sys.stdin.close()
        sys.stdin = console