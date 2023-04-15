from myLib.datastructures.Trees import * 
from myLib.datastructures.nodes.TNode import TNode
from queue import Queue

class bst:
    """
    Binary Search Tree implementation.
    
    """
    def __init__(self, root=None):
        if root is None:
            self._root = None
        elif isinstance(root, int):
            self._root = TNode(data=root)
        elif isinstance(root, TNode):
            self._root = root
        else:
            raise TypeError("Invalid argument for root node.")

    def get_root(self):
        return self._root

    def set_root(self, node):
        if node is None:
            self._root = None
        elif isinstance(node, TNode):
            self._root = node
        else:
            raise TypeError("Invalid argument for root node.")

    root = property(get_root, set_root)

    def Inserewrt(self, value):
        # Check if the tree is empty
        if self._root is None:
            self._root = TNode(value)
        else:
            # Traverse the tree to find the correct position for the new node
            current = self._root
            while True:
                if value < current.data:
                    if current.left is None:
                        current.left = TNode(value)
                        current.left.parent = current
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = TNode(value)
                        current.right.parent = current
                        break
                    else:
                        current = current.right

    def insert_nodrwree(self, node):
        # Check if the tree is empty
        if self._root is None:
            self._root = node
        else:
            # Traverse the tree to find the correct position for the new node
            current = self._root
            while True:
                if node.data < current.data:
                    if current.left is None:
                        current.left = node
                        current.left.parent = current
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = node
                        current.right.parent = current
                        break
                    else:
                        current = current.right

    def Insert(self, value_or_node):
        if isinstance(value_or_node, TNode):
            node = value_or_node
            value = node.data
        else:
            value = value_or_node
            node = TNode(value)

        # Check if the tree is empty
        if self._root is None:
            self._root = node
        else:
            # Traverse the tree to find the correct position for the new node
            current = self._root
            while True:
                if value < current.data:
                    if current.left is None:
                        current.left = node
                        current.left.parent = current
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = node
                        current.right.parent = current
                        break
                    else:
                        current = current.right



    def search(self, val):
        """
        Searches for the node with val as data and returns it, or returns None if not found.
        """
        node = self._root
        while node is not None:
            if val == node.data:
                return node
            elif val < node.data:
                node = node.left
            else:
                node = node.right
        return None

    def printInOrder(self):
        nodes = []
        self._printInOrderHelper(self.root, nodes)
        print(nodes)
        return nodes

    def _printInOrderHelper(self, node, nodes):
        if node is None:
            return
        self._printInOrderHelper(node.left, nodes)
        nodes.append(node.data)
        self._printInOrderHelper(node.right, nodes)

    
    def deleteNode(self, key):
        self.root = self._delete(self.root, key)


    def _delete(self, node, key):
        if node is None:
            return None

        if key < node.data:
            node.left = self._delete(node.left, key)
        elif key > node.data:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None and node.right is None:
                node = None
            elif node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            else:
                # find the smallest node in the right subtree
                temp = node.right
                while temp.left is not None:
                    temp = temp.left
                
                # replace the node we want to delete with the smallest node
                node.data = temp.data
                
                # delete the smallest node from the right subtree
                node.right = self._delete(node.right, temp.data)

        return node

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def printBF(self):
        # check if the tree is empty
        if self.root is None:
            print("Tree is empty")
            return

        # create a queue and put the root node in it
        queue = Queue()
        queue.put(self.root)

        # loop through the queue until it is empty
        while not queue.empty():
            # get the number of nodes in the current level of the tree
            level_size = queue.qsize()

            # loop through the nodes in the current level
            for i in range(level_size):
                # get the next node from the queue and print its data
                node = queue.get()
                print(node.data, end=' ')

                # put the left and right child nodes in the queue if they exist
                if node.left is not None:
                    queue.put(node.left)
                if node.right is not None:
                    queue.put(node.right)

            # print a newline character to move to the next line of the tree
            print()





