class TNode:

# CONSTRUCTORS

    def __init__(self, data, L, R, P, balance):
        self.data = data 
        self.left = L
        self.right = R 
        self.parent = P 
        self.balance = balance

    def __init__(self):
        self.data = None 
        self.left = None
        self.right = None 
        self.parent = None 
        self.balance = None

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
    def print(self):
        print(f"Node Information:\n Data: {self.data} \n Left Child: {self.left} \n Right Child: {self.right} \n Parent: {self.parent} \n Balance: {self.balance}")

    def to_string(self):
        return str(self.data)


