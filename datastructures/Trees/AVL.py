from datastructures.Trees.BST import BST
from datastructures.nodes.TNode import TNode


class AVL(BST):

    def __init__(self, obj=None):
        if obj is None:
            self.root = None
        elif isinstance(obj, int):
            self.root = TNode(obj)
        elif isinstance(obj, TNode):
            self.root = obj
            if obj.left is not None or obj.right is not None:
                self.root = self.balance(obj)
        else:
            raise ValueError("Invalid argument")
        
        # Overload constructor AVL(TNode obj) which takes a TNode as an
        # argument and use it as the root of the tree. If the TNode obj has children,
        # the constructor needs to create a balanced tree from passed tree by one
        # of the two following options:
        # • iteratively inserting nodes from the original tree and balancing the
        # new created AVL tree
        # • implementing a full tree balancing algorithm (Bonus)

    def set_root(self, node):
        # the setter function must check if the node has children. 

        # If children are found it must do the same as the overload constructor.
            # it is better to have a helper function (private function) that creates
            # an AVL tree and call it for the constructor and the setter
        self.root = node
        if node.left is not None or node.right is not None:
            self.root = self.balance(node)

    def get_root(self):
        return self.root
  

    def insert(self, val=None, node=None):
        if val is not None:
            # Insert(int val): creates a new node with data val to be inserted into the tree
            # ▪ Must maintain the tree balance. It can call the super.insert (insert
            # function from BST), but will need to also balance the tree after
            self.root = super().insert(self.root, val)
        elif node is not None:
            # o Insert(TNode node) : inserts the node passed as argument into the tree
            # ▪ Must maintain the tree balance. It can call the super.insert (insert
            # function from BST), but will need to also balance the tree after
            self.root = super().insert_node(self.root, node)
        else:
            raise ValueError("Either val or node must be provided.")
        self.root = self.balance(self.root)


    def delete(self, val):
        # Delete(int val): finds the node with val as data and deletes it, if not found prints
        # a statement that the value is not in the tree (Bonus)
        self.root = super().delete(self.root, val)
        self.root = self.balance(self.root)

    def search(self, val):
        # o TNode Search(int val): inherited from parent
        return super().search(self.root, val)
        
    def printInOrder(self):
        # printInOrder(): inherited from parent
        super().printInOrder()
    

    def printBF():
        # printBF(): inherited from parent
        super().printBF()
    
    def balance(self, node):
        if node is None:
            return None
        
        if self.get_height(node.left) - self.get_height(node.right) > 1:
            if self.get_height(node.left.left) >= self.get_height(node.left.right):
                node = self.rotate_right(node)
            else:
                node.left = self.rotate_left(node.left)
                node = self.rotate_right(node)
        elif self.get_height(node.right) - self.get_height(node.left) > 1:
            if self.get_height(node.right.right) >= self.get_height(node.right.left):
                node = self.rotate_left(node)
            else:
                node.right = self.rotate_right(node.right)
                node = self.rotate_left(node)
        
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        return node
    
    def get_height(self, node):
        if node is None:
            return -1
        else:
            return node.height
    
    def rotate_left(self, node):
        right_node = node.right
        node.right = right_node.left
        right_node.left = node
        
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        right_node.height = max(self.get_height(right_node.left), self.get_height(right_node.right)) + 1
        
        return right_node
    
    def rotate_right(self, node):
        left_node = node.left
        node.left = left_node.right
        left_node.right = node
        
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        left_node.height = max(self.get_height(left_node.left), self.get_height(left_node.right)) + 1
        
        return left_node




