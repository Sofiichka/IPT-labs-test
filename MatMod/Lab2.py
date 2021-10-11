#Variant #13
from scipy.optimize import linprog

target = [-2, 1, -3, 2, 1] #target equation

coefs_1 = [[-1, 1, 1, 0, 0], #coefs of left side 
          [1, -1, 0, 1, 0],  
          [1, 1, 0, 0, 1]]

coefs_2 = [1, 1, 2] # coefs of right side


bnd = [(0, float("inf")), #bounds for founded x
       (0, float("inf")), 
       (0, float("inf")), 
       (0, float("inf")), 
       (0, float("inf"))]
#cast to simplex method
solution = linprog(c = target, A_eq = coefs_1, b_eq = coefs_2, bounds = bnd, method = "simplex") 

print(solution)

# Some description of output
# con - ramainders of equtation limitation 
# fun - optimal values for function
# message - operational status
# nit - count of iterations for solving
# slack - difference between left and right sides
# status - status code of resolution
# success - resolution of solving system
# x - array of optimal values