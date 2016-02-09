"""
Objected Oriented approach of
implementing the binary tree data
structure.

When we add a child, we are adding
a new instance of the BinaryTree class,
staying true to the recursive nature of the
data structure.
"""

class BinaryTree(object):
    def __init__(self, root_obj):
        self.key = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.key = obj

    def get_root_val(self):
        return self.key


# Some simple tests:
def run_tests():
    r = BinaryTree('a')
    assert r.get_root_val() == 'a'
    assert r.get_left_child() == None
    
    r.insert_left('b')
    assert r.get_left_child().get_root_val() == 'b'
    
    r.insert_right('c')
    assert r.get_right_child().get_root_val() == 'c'
    
    r.get_right_child().set_root_val("hello")
    assert r.get_right_child().get_root_val() == "hello"

    print "All tests pass!"

run_tests()