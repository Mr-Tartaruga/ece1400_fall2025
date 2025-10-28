import random
# x = 0
# loop
# compute f(x)
# if |f(x)| < 10-6 then break
# x = x – f(x)/f’(x)
# print(x)

# x = 0   # intial guess

# f_x = x**3 - (3 * x**2) + (3 * x) - 2
# print(x)
# while abs(f_x) > 1e-6:
#     # calculate new value of x
#     x_1 = x - ((x**3 - (3 * x**2) + (3 * x) - 2)/
#                ((3 * x**2) - (6 * x) + 3))
#     x = x_1 
#     f_x = x**3 - (3 * x**2) + (3 * x) - 2
#     print(x)


# x=0
# f_x = x**3 - (3 * x**2) + (3 * x) - 2
# while abs(f_x) > 1e-6:
#     f_x2 = 3*x**2 - 6*x +3
#     x= x - f_x / f_x2
#     f_x = x**3 - (3 * x**2) + (3 * x) - 2
#     print(x)
import ast
A = "1,2"
L = ast.literal_eval(A)
print(L)