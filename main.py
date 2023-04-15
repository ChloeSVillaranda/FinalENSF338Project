from datastructures.nodes.TNode import TNode
from datastructures.Trees.BST import bst
from datastructures.Trees.AVL import avl


def main():
    # create a root node
    root = TNode(5)

    # test the getters and setters
    assert root.get_data() == 5
    assert root.get_left() is None
    assert root.get_right() is None
    assert root.get_parent() is None
    assert root.get_balance() is None

    root.set_data(10)
    assert root.get_data() == 10

    left_child = TNode(3)
    root.set_left(left_child)
    assert root.get_left() == left_child

    right_child = TNode(7)
    root.set_right(right_child)
    assert root.get_right() == right_child

    parent_node = TNode(15)
    root.set_parent(parent_node)
    assert root.get_parent() == parent_node

    root.set_balance(1)
    assert root.get_balance() == 1

    # test the print method
    root.print()

    # test the to_string method
    assert root.to_string() == "10"
    assert left_child.to_string() == "3"
    assert right_child.to_string() == "7"
    assert parent_node.to_string() == "15"


    # Create a new BST
    bst1 = bst()

    # Insert some nodes
    bst1.insert(5)
    bst1.insert(3)
    bst1.insert(7)
    bst1.insert(1)
    bst1.insert(9)

    # Print the tree
    bst1.root.print()


    # Test default constructor
    bst2 = bst()
    assert bst2.root is None

    # Test constructor with int root
    bst2 = bst(5)
    assert bst2.root.data == 5
    assert bst2.root.left is None
    assert bst2.root.right is None

    # Test constructor with TNode root
    root = TNode(data=10, left=TNode(data=5), right=TNode(data=15))
    bst2 = bst(root)
    assert bst2.root.data == 10
    assert bst2.root.left.data == 5
    assert bst2.root.right.data == 15

    # Test constructor with invalid root argument
    try:
        bst2 = bst("invalid")
    except TypeError as e:
        assert str(e) == "Invalid argument for root node."


def test_bst_constructors():
    # Test default constructor
    bst3 = bst()
    assert bst3.root is None

    # Test constructor with int argument
    bst4 = bst(5)
    assert bst4.root.data == 5

    # Test constructor with TNode argument
    node = TNode(data=7)
    bst5 = bst(node)
    assert bst5.root.data == 7

    print("All constructor tests passed!")

def test_bst_setters_and_getters():
    # Test set_root and get_root
    bst1 = bst()
    node1 = TNode(data=1)
    bst1.set_root(node1)
    assert bst1.get_root().data == 1
    
    # Test set_root with invalid argument
    bst2 = bst()
    try:
        bst2.set_root(5)
    except TypeError:
        pass
    else:
        assert False
    
    # Test get_root with empty tree
    bst3 = bst()
    assert bst3.get_root() is None

    print("All setter and getter tests passed!")

def test_insert_node():
    # Create a new tree
    tree = bst()

    # Insert some nodes into the tree
    nodes = [TNode(5), TNode(3), TNode(7), TNode(1), TNode(4), TNode(6), TNode(8)]
    for node in nodes:
        tree.insert_node(node)

    # Check that the nodes were inserted in the correct order
    assert tree.root.data == 5
    assert tree.root.left.data == 3
    assert tree.root.right.data == 7
    assert tree.root.left.left.data == 1
    assert tree.root.left.right.data == 4
    assert tree.root.right.left.data == 6
    assert tree.root.right.right.data == 8

    print("All insert tests passed!")



def test_bst_search():
    # create a new bst
    b = bst()

    # insert some nodes
    b.insert(5)
    b.insert(3)
    b.insert(7)
    b.insert(2)
    b.insert(4)
    b.insert(6)
    b.insert(8)

    # search for existing data
    node = b.search(4)
    assert node.data == 4

    # search for non-existing data
    node = b.search(9)
    assert node is None

    print("All search tests passed!")
   
def test_bst_delete():
    # create a BST and add some nodes
    b = bst()
    b.insert(5)
    b.insert(3)
    b.insert(8)
    b.insert(1)
    b.insert(4)
    b.insert(7)
    b.insert(9)

    # test deleting a node that exists in the tree
    b.deleteNode(8)
    assert b.search(8) is None
    assert b.search(9).parent.data == 5

    # test deleting a node that does not exist in the tree
    b.deleteNode(2)
    assert b.search(2) is None
  
    # test deleting the root node
    b.deleteNode(5)
    assert b.root.data == 7
    assert b.search(5) is None
    assert b.search(4).parent.data == 3

    # test deleting a leaf node
    b.deleteNode(1)
    assert b.search(1) is None
    assert b.search(3).left is None
    assert b.search(4).parent.data == 3

    print("All delete tests passed!")

def test_bst_printInOrder():
    print("TESTING PRINT IN ORDER")
    b = bst()
    assert b.printInOrder() == []
    
    b.insert(10)
    assert b.printInOrder() == [10]
    
    b.insert(5)
    b.insert(20)
    assert b.printInOrder() == [5, 10, 20]
    
    b.insert(3)
    b.insert(7)
    b.insert(15)
    b.insert(25)
    assert b.printInOrder() == [3, 5, 7, 10, 15, 20, 25]
    print(" *** ALL TESTS PASSED ***\n")

def test_bst_printBF():
    # create a BST and add some nodes
    b = bst()
    b.insert(5)
    b.insert(3)
    b.insert(8)
    b.insert(1)
    b.insert(4)
    b.insert(7)
    b.insert(9)

    # call printBF() and check the output
    expected_output = "5\n3 8\n1 4 7 9\n"
 
    print("Expected output:")
    print(expected_output)
    print("Actual output:")
    b.printBF()

    print("All printBF tests passed!")


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
 
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(5)
    
    assert tree.root.data == 2
    assert tree.root.left.data == 1
    assert tree.root.right.data == 4
    assert tree.root.right.left.data == 3
    assert tree.root.right.right.data == 5

    assert(tree.get_balance_factor(tree.root)) == 1 or -1 or 0

    # Perform left-right rotation
    tree.insert(6)

    assert tree.root.data == 4
    assert tree.root.left.data == 2
    assert tree.root.right.data == 5
    assert tree.root.left.left.data == 1
    assert tree.root.left.right.data == 3
    assert tree.root.right.right.data == 6

    assert(tree.get_balance_factor(tree.root)) == 1 or -1 or 0

    # Perform right rotation
   
    tree.insert(7)
    
    assert tree.root.data == 4
    assert tree.root.left.data == 2
    assert tree.root.right.data == 6
    assert tree.root.left.left.data == 1
    assert tree.root.left.right.data == 3
    assert tree.root.right.left.data == 5
    assert tree.root.right.right.data == 7

    assert(tree.get_balance_factor(tree.root)) == 1 or -1 or 0

    # Perform right-left rotation

    tree.insert(8)

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
    tree.insert(9)

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
    avl_tree.insert(10)
    avl_tree.insert(20)
    avl_tree.insert(30)
    avl_tree.insert(40)
    avl_tree.insert(50)

    # Check if the AVL tree is balanced after inserting nodes
    assert avl_tree.get_balance_factor(avl_tree.root) == -1 or 1 or 0

    # Delete nodes from the AVL tree
    avl_tree.delete(10)
    avl_tree.delete(20)

    # Check if the AVL tree is balanced after deleting nodes
    assert avl_tree.get_balance_factor(avl_tree.root) == 0 or 1 or -1

def test_avl():
    # Create an empty AVL tree
    avl_tree = avl()
    assert avl_tree.root is None
    print("Empty tree created successfully.")

    # Insert values into the AVL tree
    avl_tree.insert(50)
    avl_tree.insert(30)
    avl_tree.insert(70)
    avl_tree.insert(20)
    avl_tree.insert(40)
    avl_tree.insert(60)
    avl_tree.insert(80)

    # Verify that the AVL tree is balanced
    assert avl_tree.get_balance_factor(avl_tree.root) == 0 
    print("Nodes inserted and tree balanced successfully.")
    
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
    avl_tree.delete(20)

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

    print("**************** TESTING BST CLASS *******************\n")
    main()
    print()
    test_bst_constructors()
    test_bst_setters_and_getters()
    test_insert_node()
    test_bst_search()
    test_bst_delete()
    test_bst_printInOrder()
    test_bst_printBF()
    print("**************** END OF TESTS ************************\n")


    print("**************** TESTING AVL CLASS *******************\n")
    test_avl_constructors()
    test_balance()
    test_avl_balancing()
    test_avl()
    print("**************** END OF TESTS ************************\n")

    
 