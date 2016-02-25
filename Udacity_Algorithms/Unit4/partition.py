#
# Write partition to return a new array with 
# all values less then `v` to the left 
# and all values greater then `v` to the right
#

def partition(L, v):
    P_left = filter(lambda x: x < v, L)
    P_right = filter(lambda x: x > v, L)
    P = P_left + P_right
    P.insert(rank(L, v), v)
    return P

def rank(L, v):
    pos = 0
    for val in L:
        if val < v:
            pos += 1
    return pos
