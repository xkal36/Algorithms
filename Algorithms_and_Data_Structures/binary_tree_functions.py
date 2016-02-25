"""
Several function sthat create and 
operate on a tree data structure.

Here a tree is represented as a 
list of lists, where the first element
is the root and the next two are the left 
and right children respectively.
"""


def create_binary_tree(r):
    return [r, [], []]

def insert_left(root, new_branch):
    """
    Makes new_branch the first
    left child of root.
    """
    
    # Get current left child:
    t = root.pop(1)
    
    # Check if left child is empty
    # If not empty, current left child
    # will become the left child of
    # the node we are inserting
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root

def insert_right(root, new_branch):
    """
    Makes new_branch the first
    right child of root.
    """

    # Get current right child:
    t = root.pop(2)
    
    # Check if right child is empty
    # If not empty, current right child
    # will become the right child of
    # the node we are inserting.
    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [],[]])
    return root


def get_root_val(root):
    return root[0]


def set_root_val(root, new_val):
    root[0] = new_val


def get_left_child(root):
    return root[1]


def get_right_child(root):
    return root[2]


# Some simple tests:
def run_tests():
    r = create_binary_tree(3)
    assert r == [3, [], []]

    insert_left(r, 4)
    assert r == [3, [4, [], []], []]


    insert_left(r, 5)
    assert r == [3, [5, [4, [], []], []], []]


    insert_right(r, 6)
    assert r == [3, [5, [4, [], []], []], [6, [], []]]


    insert_right(r, 7)
    assert r == [3, [5, [4, [], []], []], [7, [], [6, [], []]]]


    l = get_left_child(r)
    assert l == [5, [4, [], []], []]

    set_root_val(l, 9)
    assert r == [3, [9, [4, [], []], []], [7, [], [6, [], []]]]


    insert_left(l, 11)
    assert r == [3, [9, [11, [4, [], []], []], []], [7, [], [6, [], []]]] 

    assert get_right_child(get_right_child(r)) == [6, [], []]

    print "All tests pass!"

run_tests()

