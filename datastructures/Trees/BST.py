from datastructures.nodes.TNode import TNode

class BST:
    def __init__(self):
        self.root = None
        
    def insert(self, val):
        if not self.root:
            self.root = TNode(val, 0, None, None, None)
        else:
            self._insert(val, self.root)

    def _insert(self, val, node):
        if val < node.data:
            if not node.left:
                node.left = TNode(val, 0, node, None, None)
            else:
                self._insert(val, node.left)
        else:
            if not node.right:
                node.right = TNode(val, 0, node, None, None)
            else:
                self._insert(val, node.right)
    
    def delete(self, val):
        if self.root:
            return self._delete(val, self.root)
    
    def _delete(self, val, node):
        if not node:
            return node
        elif val < node.data:
            node.left = self._delete(val, node.left)
        elif val > node.data:
            node.right = self._delete(val, node.right)
        else:
            if not node.left and not node.right:
                del node
                return None
            elif not node.left:
                temp = node.right
                temp.parent = node.parent
                del node
                return temp
            elif not node.right:
                temp = node.left
                temp.parent = node.parent
                del node
                return temp
            else:
                temp = self._findMin(node.right)
                node.data = temp.data
                node.right = self._delete(temp.data, node.right)
        return node
        
    def search(self, val):
        if not self.root:
            return None
        else:
            return self._search(val, self.root)

    def _search(self, val, node):
        if not node:
            return None
        elif val == node.data:
            return node
        elif val < node.data:
            return self._search(val, node.left)
        else:
            return self._search(val, node.right)

    def printInOrder(self):
        self._printInOrder(self.root)

    def _printInOrder(self, node):
        if node:
            self._printInOrder(node.left)
            print(node.data)
            self._printInOrder(node.right)

    def printBF(self):
        if not self.root:
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
