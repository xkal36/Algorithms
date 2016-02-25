#
# Write `max`
# 

def max(L):
    max_so_far = L[0]
    for i in range(1, len(L)):
        if L[i] > max_so_far:
            max_so_far = L[i]
    return max_so_far

def test():
    L = [1, 2, 3, 4]
    assert 4 == max(L)
    L = [3, 6, 10, 9, 3]
    assert 10 == max(L)
