"""
Sequential search of a list 
assuming the list is sorted 
in ascending order.
"""

# Ordered sequential search using while loop:
def ordered_sequential_serach(alist, item):
    pos = 0
    found = False
    stop = False

    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
	    found = True
	else:
	    if alist[pos] > item:
	        stop = True
	    else:
	        pos += 1
    return found


# Ordered sequential search using for loop:
def ordered_sequential_search_for(alist, item):
    for el in alist:
        if el == item:
	    return True
	elif el > item:
	    return False
    return False


# Ordered sequential search using python's range function:
def ordered_sequential_search_range(alist, item):
    for i in range(len(alist)):
        if alist[i] == item:
	    return True
	elif alist[i] > item:
	    return False
    return False
