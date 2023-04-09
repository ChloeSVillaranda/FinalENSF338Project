from datastructures.nodes.TNode import TNode

class BST:
    def __init__(self, root=None):
        self.root = root

    def get_root(self):
        return self.root

    def set_root(self, root):
        self.root = root

    def insert(self, val):
        node = TNode(val)
        if self.root is None:
            self.root = node
        else:
            curr = self.root
            while True:
                if val < curr.val:
                    if curr.left is None:
                        curr.left = node
                        break
                    else:
                        curr = curr.left
                elif val > curr.val:
                    if curr.right is None:
                        curr.right = node
                        break
                    else:
                        curr = curr.right

    def insert_node(self, node):
        if self.root is None:
            self.root = node
        else:
            curr = self.root
            while True:
                if node.val < curr.val:
                    if curr.left is None:
                        curr.left = node
                        break
                    else:
                        curr = curr.left
                elif node.val > curr.val:
                    if curr.right is None:
                        curr.right = node
                        break
                    else:
                        curr = curr.right

    def search(self, val):
        curr = self.root
        while curr is not None:
            if curr.val == val:
                return curr
            elif val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return None

    def delete(self, val):
        parent = None
        curr = self.root

        # Find the node to be deleted and its parent
        while curr is not None and curr.val != val:
            parent = curr
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right

        # If the node is not found, print an error message and return
        if curr is None:
            print("Value not found in tree")
            return

        # If the node has two children, find the successor and replace the node
        if curr.left is not None and curr.right is not None:
            successor = curr.right
            while successor.left is not None:
                successor = successor.left
            curr.val = successor.val
            curr = successor

        # At this point, curr has zero or one child
        if curr.left is not None:
            child = curr.left
        else:
            child = curr.right

        # If the node to be deleted is the root, set the child as the new root
        if parent is None:
            self.root = child
        elif curr == parent.left:
            parent.left = child
        else:
            parent.right = child

    def print_inorder(self, node=None):
        if node is None:
            node = self.root
        if node is not None:
            self.print_inorder(node.left)
            print(node.val, end=' ')
            self.print_inorder(node.right)

    def print_bf(self):
        if self.root is None:
            return

        queue = [self.root]

        while queue:
            curr_level_nodes = len(queue)
            for i in range(curr_level_nodes):
                node = queue.pop(0)
                print(node.val, end=' ')

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            print()

    