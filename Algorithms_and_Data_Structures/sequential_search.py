# Sequential serach using while loop:
def sequential_search_while(alist, item):
	pos = 0
	found = False
	l_len = len(alist)

	while pos < l_len and not found:
		if alist[pos] == item:
			found = True
		else:
			pos += 1
	return found

# Sequential search using python's for loop construct:
def sequential_serach_for(alist, item):
	for el in alist:
		if el == item:
			return True
	return False

# Sequential search using python's range function:
def sequential_serach_generic(alist, item):
	for i in range(len(alist)):
		if alist[i] == item:
			return True
	return False
