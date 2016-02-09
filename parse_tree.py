"""
Functions to first build a parse tree from
a fully parenthesised mathematical expression, 
and then to evaluate this parse tree, 
returning the result of the expression.

We first split the expression into
a list of tokens. The parse tree is then
built by going through these tokens 
and applying the following rules:

1. If the current token is a '(', add a new 
node as the left child of the current node, 
and descend to the left child.

2. If the current token is in the list ['+','-','/','*'], 
set the root value of the current node to the operator 
represented by the current token. Add a new node as the right child of the current node and descend to the right child.

3. If the current token is a number, set the root 
value of the current node to the number 
and return to the parent.

4.  If the current token is a ')', 
go to the parent of the current node.
"""

import operator
from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree


def build_parse_tree(fp_exp):
	operators = ['+', '-', '*', '/']
	fp_list = fp_exp.split()
	p_stack = Stack()
	e_tree = BinaryTree('')
	p_stack.push(e_tree)
	current_tree = e_tree

	for token in fp_list:
		if token == '(':
			current_tree.insertLeft('')
			p_stack.push(current_tree)
			current_tree = current_tree.getLeftChild()
		elif token not in (operators + ['(']):
			current_tree.setRootVasl(int(token))
			parent = p_stack.pop()
			current_tree = parent
		elif token in operators:
			current_tree.set_root_val(token)
            current_tree.insert_right('')
            p_stack.push(current_tree)
            current_tree = current_tree.getRightChild()
        elif token == ')':
            current_tree = p_stack.pop()
        else:
            raise ValueError
    return e_tree


# Function that evaluates a parse tree
# built from a parenthesised expression:
def evaluate(parse_tree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

    left_c = parse_tree.getLeftChild()
    right_c = parse_tree.getRightChild()

    if left_c and right_c:
        fn = opers[parse_tree.getRootVal()]
        return fn(evaluate(left_c), evaluate(right_c))
    else:
        return parse_tree.getRootVal()


# Evaluation function could also be:
def postorder_eval(tree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
    res1 = None
    res2 = None
    if tree:
        res1 = postorder_eval(tree.getLeftChild())
        res2 = postorder_eval(tree.getRightChild())
        if res1 and res2:
            return opers[tree.getRootVal()](res1,res2)
        else:
            return tree.getRootVal()
