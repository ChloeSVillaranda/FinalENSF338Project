from datastructures.Trees.BST import bst
from datastructures.nodes.TNode import TNode

class avl(bst):
    
    def __init__(self, val=None, obj=None):
        if val is None and obj is None:
            self.root = None
        elif val is not None and obj is None:
            self.root = TNode(val)
        elif val is None and obj is not None:
            self.root = self.__balance(obj)
    
    def __balance(self, node):
        # Implement AVL balancing logic here
        pass

    

