from datastructures.Trees.BST import bst
from datastructures.nodes.TNode import TNode




class avl(bst):
    """
    An AVL tree is a self-balancing binary search tree where the heights of the two child subtrees 
    of any node differ by at most one. This implementation extends the binary search tree (BST) class, 
    providing methods to insert, delete, and search for values in the tree while maintaining AVL balance. 
    The tree nodes are instances of the TNode class.

    """

    def __init__(self, root=None):
        if root is None:
            self.root = None
        elif isinstance(root, int):
            self.root = TNode(root)
        elif isinstance(root, TNode):
            self.root = root
        self.root = self.balance(self.root)


    def Insert(self, val):
        self.root = self._insert(self.root, val)

    def _insert(self, node, val):
        if node is None:
            return TNode(val)

        if val < node.data:
            node.left = self._insert(node.left, val)
        else:
            node.right = self._insert(node.right, val)

        # update height and balance factor
        #node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance_factor = self.get_balance_factor(node)

        # perform rotations if necessary
        if balance_factor > 1 and val < node.left.data:
            return self.right_rotation(node)
        if balance_factor < -1 and val > node.right.data:
            return self.left_rotation(node)
        if balance_factor > 1 and val > node.left.data:
            node.left = self.left_rotation(node.left)
            return self.right_rotation(node)
        if balance_factor < -1 and val < node.right.data:
            node.right = self.right_rotation(node.right)
            return self.left_rotation(node)

        return node

    def Delete(self, val):
        self.root = self._delete(self.root, val)

    def _delete(self, node, val):
        if node is None:
            return node

        if val < node.data:
            node.left = self._delete(node.left, val)
        elif val > node.data:
            node.right = self._delete(node.right, val)
        else:
            # found the node to delete
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                # node has two children, replace it with the successor
                successor = self._get_min_node(node.right)
                node.data = successor.data
                node.right = self._delete(node.right, successor.data)

        # rebalance the tree
        balance_factor = self.get_balance_factor(node)
        if balance_factor > 1:
            if self.get_balance_factor(node.left) >= 0:
                node = self.right_rotation(node)
            else:
                node = self.left_right_rotation(node)
        elif balance_factor < -1:
            if self.get_balance_factor(node.right) <= 0:
                node = self.left_rotation(node)
            else:
                node = self.right_left_rotation(node)

        return node

    def _get_min_node(self, node):
        while node.left is not None:
            node = node.left
        return node

    def balance(self, node):
        if node is None:
            return None
        
        # calculate balance factor
        balance_factor = self.get_balance_factor(node)
        
        if balance_factor > 1:
            # left subtree is heavier
            if self.get_balance_factor(node.left) >= 0:
                # left-left case
                node = self.right_rotation(node)
            else:
                # left-right case
                node.left = self.left_rotation(node.left)
                node = self.right_rotation(node)
        elif balance_factor < -1:
            # right subtree is heavier
            if self.get_balance_factor(node.right) <= 0:
                # right-right case
                node = self.left_rotation(node)
            else:
                # right-left case
                node.right = self.right_rotation(node.right)
                node = self.left_rotation(node)
        
        # update parent node's child reference
        if node.parent is not None:
            if node.parent.left == node:
                node.parent.left = node.parent
            else:
                node.parent.right = node.parent

        # recursively balance child nodes
        node.left = self.balance(node.left)
        node.right = self.balance(node.right)
        
        return node

    def left_rotation(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        return new_root

    def get_height(self, node):
        if node is None:
            return -1
        else:
            return max(self.get_height(node.left), self.get_height(node.right)) + 1

    def get_balance_factor(self, node):
        if node:
            return self.get_height(node.left) - self.get_height(node.right)
        else:
            return 0

    def right_rotation(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        return new_root

    def left_right_rotation(self, node):
        node.left = self.left_rotation(node.left)
        return self.right_rotation(node)

    def right_left_rotation(self, node):
        node.right = self.right_rotation(node.right)
        return self.left_rotation(node)

    def Search(self, val):
        return super().search(val)

    def printInOrder(self):
        super().printInOrder()

    def printBF(self):
        super().printBF()


