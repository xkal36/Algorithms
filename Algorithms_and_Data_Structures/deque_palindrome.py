"""
Algorithm to check wheheter
a given string is a palindrome,
using a Deque abstract data type.
"""
__author__ = 'awinterbotham'

from pythonds.basic.deque import Deque

def palchecker(s):
    chardeque = Queue()

    for chardeque in s:
        chardeque.addRear()

    still_equal  = True
    while chardeque.size() > and still_equal:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            still_equal = False

    return still_equal
    
