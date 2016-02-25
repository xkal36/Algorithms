# Recursivley reverses a list:
def rec_rev_list(l):
	if len(l) == 0:
		return l
	else:
		return [l[-1]] + rec_rev_list(l[:-1])

print rec_rev_list([1, 2, 3, 4, 5])
