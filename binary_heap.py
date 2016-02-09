"""
Python implementation of a 
binary heap, used to implement a 
priority queue data structure, where the
minimum item is always removed first.

An easier way to implement a priority queue 
would be to use a combination of sorting functions and lists. 
However, inserting into a list is O(n) and sorting a list is O(nlogn)
Using a binary heap allows us to 
both enqueue and dequeue items in O(log⁡n).

Building the heap is done in O(n).
"""

class BinHeap(object):
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0


    def perc_up(self, i):
        while i // 2 > 0:
          if self.heap_list[i] < self.heap_list[i // 2]:
             tmp = self.heap_list[i // 2]
             self.heap_list[i // 2] = self.heap_list[i]
             self.heap_list[i] = tmp
          i = i // 2

    def insert(self, k):
      self.heap_list.append(k)
      self.current_size = self.current_size + 1
      self.perc_up(self.current_size)

    def perc_down(self, i):
      while (i * 2) <= self.current_size:
          mc = self.min_child(i)
          if self.heap_list[i] > self.heap_list[mc]:
              tmp = self.heap_list[i]
              self.heap_list[i] = self.heap_list[mc]
              self.heap_list[mc] = tmp
          i = mc

    def min_child(self, i):
      if i * 2 + 1 > self.current_size:
          return i * 2
      else:
          if self.heap_list[i*2] < self.heap_list[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1

    def del_min(self):
      retval = self.heap_list[1]
      self.heap_list[1] = self.heap_list[self.current_size]
      self.current_size = self.current_size - 1
      self.heap_list.pop()
      self.perc_down(1)
      return retval

    def build_heap(self, alist):
      i = len(alist) // 2
      self.current_size = len(alist)
      self.heap_list = [0] + alist[:]
      while (i > 0):
          self.perc_down(i)
          i = i - 1

bh = BinHeap()
bh.build_heap([9,5,6,2,3])

print bh.del_min()
print bh.del_min()
print bh.del_min()
print bh.del_min()
print bh.del_min()
