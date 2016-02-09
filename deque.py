"""
Implementation of the Deque
abstract data type.

We use the left side (start) of the
list as the rear and the right side 
(end) as the front.
"""

class Deque(Object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return (len(self.items)) == 0

    def size(self):
        return len(items)

    def add_front(self, to_add):
        self.items.append(to_add)

    def add_rear(self, to_add):
        self.items.insert(0, to_add)

    def remove_rear(self):
        self.items.pop(0)

    def remove_front(self):
        self.items.pop()
