"""
Two similar Python implementationms
of selection sort.

Running time is of course O(n**2)
"""


# Canonical use of temperoprary variable for switching values:
def selection_sort(alist):
	for fill_slot in range(len(alist) - 1, 0, -1):
		pos_of_max = 0
		for location in range(1, fill_slot + 1):
			if alist[location] > alist[pos_of_max]

	temp = alist[fill_slot]
	alist[fill_slot] = alist[pos_of_max]
	alist[pos_of_max] = temp



# Using Python's simultaneous assignment for switching:
def selection_sort_sim(alist):
	for fill_slot in range(len(alist) - 1, 0, -1):
		pos_of_max = 0
		for location in range(1, fill_slot + 1):
			if alist[location] > alist[pos_of_max]
	
	alist[fill_slot], alist[pos_of_max] = alist[pos_of_max], alist[fill_slot]