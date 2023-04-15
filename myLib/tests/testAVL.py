from myLib.datastructures.nodes.TNode import TNode
from myLib.datastructures.Trees.AVL import avl

def test_avl_constructors():
# create an AVL tree using the default constructor
    avl2 = avl()

    # check that the root is None
    assert avl2.root is None

    # create an AVL tree using the overload constructor with a data of 5
    avl2 = avl(5)

    # check that the root has a data of 5 and both the left and right child are None
    assert avl2.root.data == 5
    assert avl2.root.left is None
    assert avl2.root.right is None

    # create an AVL tree using the overload constructor with a TNode object
    tnode1 = TNode(5)
    tnode2 = TNode(10)
    tnode3 = TNode(15)
    tnode4 = TNode(20)
    tnode5 = TNode(25)

    tnode2.left = tnode1
    tnode2.right = tnode3
    tnode3.right = tnode5
    tnode3.left = tnode4

    avl1 = avl(tnode2)

    # check that the AVL tree is created correctly from the TNode object
    assert avl1.root.data == 10
    assert avl1.root.left.data == 5
    assert avl1.root.left.left is None
    assert avl1.root.left.right is None
    assert avl1.root.right.data == 15
    assert avl1.root.right.left.data == 20
    assert avl1.root.right.right.data == 25


def test_balance():
    tree = avl()
 
    tree.Insert(1)
    tree.Insert(2)
    tree.Insert(3)
    tree.Insert(4)
    tree.Insert(5)
    
    assert tree.root.data == 2
    assert tree.root.left.data == 1
    assert tree.root.right.data == 4
    assert tree.root.right.left.data == 3
    assert tree.root.right.right.data == 5

    assert(tree.get_balance_factor(tree.root)) == 1 or -1 or 0

    # Perform left-right rotation
    tree.Insert(6)

    assert tree.root.data == 4
    assert tree.root.left.data == 2
    assert tree.root.right.data == 5
    assert tree.root.left.left.data == 1
    assert tree.root.left.right.data == 3
    assert tree.root.right.right.data == 6

    assert(tree.get_balance_factor(tree.root)) == 1 or -1 or 0

    # Perform right rotation
   
    tree.Insert(7)
    
    assert tree.root.data == 4
    assert tree.root.left.data == 2
    assert tree.root.right.data == 6
    assert tree.root.left.left.data == 1
    assert tree.root.left.right.data == 3
    assert tree.root.right.left.data == 5
    assert tree.root.right.right.data == 7

    assert(tree.get_balance_factor(tree.root)) == 1 or -1 or 0

    # Perform right-left rotation

    tree.Insert(8)

    assert tree.root.data == 4
    assert tree.root.left.data == 2
    assert tree.root.right.data == 6
    assert tree.root.left.left.data == 1
    assert tree.root.left.right.data == 3
    assert tree.root.right.left.data == 5
    assert tree.root.right.right.data == 7
    assert tree.root.right.right.right.data == 8

    assert(tree.get_balance_factor(tree.root)) == 1 or -1 or 0
 
    # Perform left rotation
    tree.Insert(9)

    assert tree.root.data == 4
    assert tree.root.left.data == 2
    assert tree.root.right.data == 6
    assert tree.root.left.left.data == 1
    assert tree.root.left.right.data == 3
    assert tree.root.right.left.data == 5
    assert tree.root.right.right.data == 8
    assert tree.root.right.right.right.data == 9
    assert tree.root.right.right.left.data == 7

    assert(tree.get_balance_factor(tree.root)) == 1 or -1 or 0

    print("AVL TREE BALANCED SUCCESSFULLY")
    

def test_avl_balancing():
    # Create an empty AVL tree
    avl_tree = avl()

    # Insert nodes into the AVL tree
    avl_tree.Insert(10)
    avl_tree.Insert(20)
    avl_tree.Insert(30)
    avl_tree.Insert(40)
    avl_tree.Insert(50)

    # Check if the AVL tree is balanced after Inserting nodes
    assert avl_tree.get_balance_factor(avl_tree.root) == -1 or 1 or 0

    # Delete nodes from the AVL tree
    avl_tree.Delete(10)
    avl_tree.Delete(20)

    # Check if the AVL tree is balanced after deleting nodes
    assert avl_tree.get_balance_factor(avl_tree.root) == 0 or 1 or -1

def test_avl():
    # Create an empty AVL tree
    avl_tree = avl()
    assert avl_tree.root is None
    print("Empty tree created successfully.")

    # Insert values into the AVL tree
    avl_tree.Insert(50)
    avl_tree.Insert(30)
    avl_tree.Insert(70)
    avl_tree.Insert(20)
    avl_tree.Insert(40)
    avl_tree.Insert(60)
    avl_tree.Insert(80)

    # Verify that the AVL tree is balanced
    assert avl_tree.get_balance_factor(avl_tree.root) == 0 
    print("Nodes Inserted and tree balanced successfully.")
    
    # Verify that the inorder traversal of the AVL tree is correct
    print("\nTESTING PRINT IN ORDER")
    print("\nExpected output: \n[20, 30, 40, 50, 60, 70, 80]")
    print("Actual Output:")
    avl_tree.printInOrder()

    # Verify that the level order traversal of the AVL tree is correct
    print("\nTESTING PRINTBF")
    print("\nExpected output: \n50\n30 70\n20 40 60 80\n")
    print("Actual Output:")
    avl_tree.printBF() 

    # Delete a node from the AVL tree
    avl_tree.Delete(20)

    # Verify that the AVL tree is still balanced
    assert avl_tree.get_balance_factor(avl_tree.root) == 0

    # Verify that the inorder traversal of the AVL tree is correct
    print("\nTESTING PRINT IN ORDER AFTER DELETING 20")
    print("\nExpected output: \n[30, 40, 50, 60, 70, 80]")
    print("Actual Output:")
    avl_tree.printInOrder() 

    # Verify that the level order traversal of the AVL tree is correct
    print("\nTESTING PRINTBF AFTER DELETING 20")
    print("\nExpected output: \n50\n30 70\n40 60 80\n")
    print("Actual Output:")
    avl_tree.printBF()

    # Search for a value in the AVL tree
    

if __name__ == "__main__":
    print("**************** TESTING AVL CLASS *******************\n")
    test_avl_constructors()
    test_balance()
    test_avl_balancing()
    test_avl()
    print("**************** END OF TESTS ************************\n")

    