from datastructures.Trees.BST import bst
from datastructures.nodes.TNode import TNode

class avl(bst):

    def __init__(self, obj=None):
        if obj is None:
            self.root = None
        elif isinstance(obj, int):
            self.root = TNode(obj)
        elif isinstance(obj, TNode):
            self.root = obj
            if obj.left is not None or obj.right is not None:
                self.balance()
        else:
            raise ValueError("Invalid argument")

    def set_root(self, node):
        self.root = node
        if node.left is not None or node.right is not None:
            self.balance()

    def insert(self, val=None):
        if val is None:
            raise ValueError("val must be provided.")
        super().insert(val)
        self.balance()

    def delete(self, val):
        super().delete(val)
        self.balance()
        
    def search(self, val):
        node = super().search(val)
        return node if node is not None else None

    def balance(self):
        if self.root is None:
            return
        
        while True:
            if self.get_balance_factor(self.root) > 1:
                if self.get_balance_factor(self.root.left) >= 0:
                    self.root = self.rotate_right(self.root)
                else:
                    self.root.left = self.rotate_left(self.root.left)
                    self.root = self.rotate_right(self.root)
            elif self.get_balance_factor(self.root) < -1:
                if self.get_balance_factor(self.root.right) <= 0:
                    self.root = self.rotate_left(self.root)
                else:
                    self.root.right = self.rotate_right(self.root.right)
                    self.root = self.rotate_left(self.root)
            else:
                break
    
    def get_balance_factor(self, node):
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
    
    def get_height(self, node):
        if node is None:
            return 0
        return max(self.get_height(node.left), self.get_height(node.right)) + 1
    
    def rotate_left(self, node):
        right_node = node.right
        node.right = right_node.left
        right_node.left = node
        return right_node
    
    def rotate_right(self, node):
        left_node = node.left
        node.left = left_node.right
        left_node.right = node
        return left_node



