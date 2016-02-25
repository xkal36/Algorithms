#
# Given a list of numbers, L, find a number, x, that
# minimizes the sum of the square of the difference
# between each element in L and x: SUM_{i=0}^{n-1} (L[i] - x)^2
# 
# Your code should run in Theta(n) time
# 

def mean(l):
    return sum(l) / float(len(l))

def minimize_square(L):
    return mean(L)
    