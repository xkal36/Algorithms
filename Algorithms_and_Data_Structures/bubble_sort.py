"""
Two very similar version of bubble 
sort. Both modify the original list.

Running time is of course O(n**2)
"""

# Swapping method using temporary storage:
def bubble_sort_mod(alist):
    for passnum in range(len(alist) - 1, 0,  -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp


# Using Python's simultaneous assignment for swapping:
def bubble_sort_sim(alist):
	for passnum in range(len(alist)-1, 0, -1):
		for i in range(passnum):
			if alist[i] > alist[i + 1]:
				alist[i], alist[i + 1] = alist[i + 1], alist[i]
	
