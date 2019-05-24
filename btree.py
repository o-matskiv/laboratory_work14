from bnode import *


class BTree:
    def __init__(self, root):
        self.key = BTNode(root)
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child == None:
            self.left_child = BTree(new_node)
        else:
            t = BTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child = BTree(new_node)
        else:
            t = BTree(new_node)
            t.right_child = self.right_child
            self.right_child = t
