
class TNode(object):

 # CONSTRUCTOR
    def __init__(self, data=None, left=None, right=None, parent=None, balance =None):
            self.data = data
            self.left = left
            self.right = right
            self.parent = parent
            self.balance = balance

  # GETTERS
    def get_data(self):
        return self.data
    
    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right
    
    def get_parent(self):
        return self.parent
    
    def get_balance(self):
        return self.balance

  # SETTERS
    def set_data(self, value):
        self.data = value
    
    def set_left(self, value):
        self.left = value
    
    def set_right(self, value):
        self.right = value
    
    def set_parent(self, value):
        self.parent = value
    
    def set_balance(self, value):
        self.balance = value

# METHODS 
    # def print(self):
    #     print(f"Node Information:\n Data: {self.data} \n Left Child: {self.left} \n Right Child: {self.right} \n Parent: {self.parent} \n Balance: {self.balance}")

    def print(self):
        left_str = self.left.toString() if self.left is not None else "None"
        right_str = self.right.toString() if self.right is not None else "None"
        parent_str = self.parent.toString() if self.parent is not None else "None"
        print(f"Node Information:\n Data: {self.data} \n Left Child: {left_str} \n Right Child: {right_str} \n Parent: {parent_str} \n Balance: {self.balance}")

    def toString(self):
        return str(self.data)
    

    def __lt__(self, other):
        return self.data < other.data

