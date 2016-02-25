
"""
Python implementation of
a linked list along with
various operations on 
said data type.
"""


class Node:
    """
    Building block: linked
    lists are a collection of 
    Node objects.
    """
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class UnorderedList:

    def __init__(self):
        self.head = None
        self.last = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

        if self.size() == 0:
            self.last = temp


    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def index(self, item):
        """
        Returns the index of the
        given item
        """
        current = self.head
        found = False
        index  = 0
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
            index += 1
        return index
        
    def insert(self, item, index):
        """
        Inserts the given item in
        the given index.
        """
        item = Node(item)
        current = self.head
        previous = None
        curr_index  = 0
        
        while curr_index <= index -2 :
            previous = current
            current = current.getNext()
            curr_index += 1

        item.setNext(current)
        previous.setNext(item)

        
    # Appending in O(n) running time:   
    def append_n(self, item):
        """
        Adds the given item to 
        the end of the linked list
        """
        item = Node(item)
        current = self.head
        previous = None
        curr_index = 0
        size = self.size()
        while curr_index < size:
            previous = current
            current = current.getNext()
            curr_index += 1
        previous.setNext(item)

    # Appending in O(1) running time:
    def append_1(self, item):
        item = Node(item)
        self.last.setNext(item)
        item.setNext(None)
        self.last = item

    def pop(self, pos):
        to_pop = []
        current = self.head
        previous = None
        curr_index  = 0
        
        while curr_index <= pos - 2:
            previous = current
            current = current.getNext()
            curr_index += 1

        next = current.getNext()
        previous.setNext(next)
        return current


    def pop(self):
        """
        Removes and returns
        the last item from the linked
        list.
        """
        current = self.head
        curr_index = 0
        size = self.size()
        while curr_index < size - 1:
            previous = current
            current = current.getNext()
            curr_index += 1
        previous.setNext(None)
        return current.getData()

   


# Simple tests:        

mylist = UnorderedList()

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)


print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))

mylist.add(100)
print(mylist.search(100))
print(mylist.size())

mylist.remove(54)
print(mylist.size())
mylist.remove(93)
print(mylist.size())
mylist.remove(31)
print(mylist.size())
print(mylist.search(93))


mylist.append_n(2)
mylist.append_n(45)
print mylist.size()
print mylist.pop()
print mylist.size()
print mylist.pop()
print mylist.size()
mylist.insert(312, 3)
print mylist.size()
print mylist.index(312)
