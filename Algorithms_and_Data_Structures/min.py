"""
Write two Python functions to find the 
minimum number in a list.
The first function should compare 
each number to every other number in the list ie O(n). 
The second function should be linear ie O(n).
"""

__author__ = 'awinterbotham'
import time
from random import randrange


# First function O(n**2):
# Stupid algorithm (wouldn't use in real life)
def min_quadratic(l):
    overall_min = l[0]
    for i in l:
        is_smallest = True
        for j in l:
            if i > j:
                is_smallest = False
        if is_smallest:
            overall_min = i
    return overall_min


# Second function: O(n)
def min_linear(l):
    min_so_far = l[0]
    for i in range(1, len(l)):
        if l[i] < min_so_far:
            min_so_far = l[i]
    return min_so_far


print min_quadratic([5, 4, 2, 1, 0])
print min_quadratic([0, 4, 2, 1 5])

# Measuring how running time increases:
for list_size in range(1000, 100001, 1000):
    alist = [randrange(100000) for x in range(list_size)]
    start = time.time()
    print min_quadratic(alist)
    end = time.time()
    print "size: %d time: %f" % (list_size, end - start)
