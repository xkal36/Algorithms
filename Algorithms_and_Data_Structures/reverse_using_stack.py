from test import testEqual
from pythonds.basic.stack import Stack

# My implementation:
def revstring_mine(mystr):
    s = Stack()
    for char in mystr:
        s.push(char)
    rev_chars = [s.pop() for i in range(len(mystr))]
    return ''.join(l)


# Example given in the book:
def revstring_mine(mystr):
    s = Stack()
    for char in mystr:
        s.push(char)
    revstr = ''
    while not s.isEmpty():
        revstr += s.pop()
    return revstr


testEqual(revstring('apple'),'elppa')
testEqual(revstring('x'),'x')
testEqual(revstring('1234567890'),'0987654321')
