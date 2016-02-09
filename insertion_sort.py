"""
Python implementation of 
insertion sort algorithm.

Running time: O(n**2)
"""

def insertion_sort(alist):
   for index in range(1, len(alist)):

     current_val = alist[index]
     pos = index

     while pos > 0 and alist[pos - 1] > current_val:
         alist[pos]=alist[pos - 1]
         pos = pos - 1

     alist[pos ] = current_val