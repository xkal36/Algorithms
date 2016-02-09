def shellSort(alist):
    sublist_count = len(alist) // 2
    while sublist_count > 0:

      for start_pos in range(sublistcount):
        gap_insertion_sort(alist, start_pos, sublist_count)

      print("After increments of size", sublist_count,
                                   "The list is", alist)

      sublist_count = sublist_count // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start + gap, len(alist), gap):

        current_val = alist[i]
        pos = i

        while pos >= gap and alist[pos - gap] > current_val:
            alist[pos] = alist[pos - gap]
            pos = pos - gap

        alist[pos] = current_val