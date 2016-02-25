"""
Iterative and recursive approaches to binary search.
Assumes the list is sorted of course.

Theoretically they run in O(log n) time,
but slicing in python is O(k), where k is
teh size (length) of the list to slice.
"""

# Non-recursive binary search:
def binary_serach(alist, item):
	first = 0
	last = len(alist) - 1
	found = False

	while first <= last and not found:
		midpoint = (first + last) // 2
		if alist[midpoint] == item:
			found = True
		else:
			if item < alist[midpoint]:
				last = midpoint - 1
			else:
				first = midpoint + 1
	return found


# Recursive binary search:
def rec_binary_search(alist, item):
	if len(alist) == 0:
		return False
	else:
		midpoint = len(alist) // 2
		if alist[midpoint] == item:
			return True
		else:
			if item < alist[midpoint]:
				return rec_binary_search(alist[:midpoint], item)
			else:
				return rec_binary_search(alist[midpoint + 1:], item)


# Improved recursive binary search - actually O(log n):
def rec_binary_search(alist, item):
	first = 0
	last = len(alist) - 1

	if len(alist) == 0:
		return False
	else:
		midpoint = (first + last) // 2
		if alist[midpoint] == item:
			return True
		else:
			if item < alist[midpoint]:
				return rec_binary_search(alist[:midpoint], item)
			else:
				return rec_binary_search(alist[midpoint + 1:], item)