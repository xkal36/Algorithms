"""
Functions for different ways of
traversing a parse tree.

In a preorder traversal, we visit the root node first, 
then recursively do a preorder traversal of the left subtree, 
followed by a recursive preorder traversal of the right subtree.

In an inorder traversal, we recursively 
do an inorder traversal on the left subtree, 
visit the root node, and finally do a recursive 
inorder traversal of the right subtree.

In a postorder traversal, we recursively do 
a postorder traversal of the left subtree 
and the right subtree followed by a visit to the root node.
"""


def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())


def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())


def inorder(tree):
  if tree != None:
      inorder(tree.getLeftChild())
      print(tree.getRootVal())
      inorder(tree.getRightChild())
