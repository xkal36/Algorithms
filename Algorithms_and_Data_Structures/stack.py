'''
The following stack implementation assumes
that the end of the list will
hold the top element of the stack. As the stack grows
(as push operations occur), new items will be added on the end of the list.
Pop operations will manipulate that same end.

Another implementation could make the top the beginning of the list,
instead of the end as is done above.

This is implementation is more efficient as popend and append
are done in constant timeit ie O(1), wheras the alternative
implementation using insert and popend would be O(n).
'''

class Stack(Object):
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
