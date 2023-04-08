# - TNode:
# This class is a general tree node class that has requirements for both BST and AVL trees. In the
# node sub-library, add the implementation of the tree node
# Member variables of this class are:
# o Int data member
# o Tnode left
# o Tnode right
# o Tnode parent
# o Int balance
# The class must implement all needed:
# o Setters
# o Getters
# o print: prints the node information to console in a user friendly format
# o toString: returns the data member as a string (will be used for the tree prints)
# o constructors:
# ▪ TNode(): a default constructor without arguments that initializes
# members to default values.
# ▪ TNode(int data, int balance, TNode P, TNode L, TNode R): An overload
# constructor that takes an integer data, an integer balance to initialize the
# data and balance members. Initializes the parent using the P argument, L
# to initialize left child, and R to initialize right child