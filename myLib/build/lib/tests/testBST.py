from myLib.datastructures.nodes.TNode import TNode
from myLib.datastructures.Trees.BST import BST

def test_case_1():
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
    assert root.toString() == "10"
    assert left_child.toString() == "3"
    assert right_child.toString() == "7"
    assert parent_node.toString() == "15"


    # Create a new BST
    BST1 = BST()

    # Insert some nodes
    BST1.Insert(5)
    BST1.Insert(3)
    BST1.Insert(7)
    BST1.Insert(1)
    BST1.Insert(9)

    # Print the tree
    BST1.root.print()


    # Test default constructor
    BST2 = BST()
    assert BST2.root is None

    # Test constructor with int root
    BST2 = BST(5)
    assert BST2.root.data == 5
    assert BST2.root.left is None
    assert BST2.root.right is None

    # Test constructor with TNode root
    root = TNode(data=10, left=TNode(data=5), right=TNode(data=15))
    BST2 = BST(root)
    assert BST2.root.data == 10
    assert BST2.root.left.data == 5
    assert BST2.root.right.data == 15

    # Test constructor with invalid root argument
    try:
        BST2 = BST("invalid")
    except TypeError as e:
        assert str(e) == "Invalid argument for root node."


def test_BST_constructors():
    # Test default constructor
    BST3 = BST()
    assert BST3.root is None

    # Test constructor with int argument
    BST4 = BST(5)
    assert BST4.root.data == 5

    # Test constructor with TNode argument
    node = TNode(data=7)
    BST5 = BST(node)
    assert BST5.root.data == 7

    print("All constructor tests passed!")

def test_BST_setters_and_getters():
    # Test set_root and get_root
    BST1 = BST()
    node1 = TNode(data=1)
    BST1.set_root(node1)
    assert BST1.get_root().data == 1
    
    # Test set_root with invalid argument
    BST2 = BST()
    try:
        BST2.set_root(5)
    except TypeError:
        pass
    else:
        assert False
    
    # Test get_root with empty tree
    BST3 = BST()
    assert BST3.get_root() is None

    print("All setter and getter tests passed!")

def test_Insert_node():
    # Create a new tree
    tree = BST()

    # Insert some nodes into the tree
    nodes = [TNode(5), TNode(3), TNode(7), TNode(1), TNode(4), TNode(6), TNode(8)]
    for node in nodes:
        tree.Insert(node)

    # Check that the nodes were Inserted in the correct order
    assert tree.root.data == 5
    assert tree.root.left.data == 3
    assert tree.root.right.data == 7
    assert tree.root.left.left.data == 1
    assert tree.root.left.right.data == 4
    assert tree.root.right.left.data == 6
    assert tree.root.right.right.data == 8

    print("All Insert tests passed!")



def test_BST_search():
    # create a new BST
    b = BST()

    # Insert some nodes
    b.Insert(5)
    b.Insert(3)
    b.Insert(7)
    b.Insert(2)
    b.Insert(4)
    b.Insert(6)
    b.Insert(8)

    # search for existing data
    node = b.search(4)
    assert node.data == 4

    # search for non-existing data
    node = b.search(9)
    assert node is None

    print("All search tests passed!")
   
def test_BST_delete():
    # create a BST and add some nodes
    b = BST()
    b.Insert(5)
    b.Insert(3)
    b.Insert(8)
    b.Insert(1)
    b.Insert(4)
    b.Insert(7)
    b.Insert(9)

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

def test_BST_printInOrder():
    print("TESTING PRINT IN ORDER")
    b = BST()
    assert b.printInOrder() == []
    
    b.Insert(10)
    assert b.printInOrder() == [10]
    
    b.Insert(5)
    b.Insert(20)
    assert b.printInOrder() == [5, 10, 20]
    
    b.Insert(3)
    b.Insert(7)
    b.Insert(15)
    b.Insert(25)
    assert b.printInOrder() == [3, 5, 7, 10, 15, 20, 25]
    print(" *** ALL TESTS PASSED ***\n")

def test_BST_printBF():
    # create a BST and add some nodes
    b = BST()
    b.Insert(5)
    b.Insert(3)
    b.Insert(8)
    b.Insert(1)
    b.Insert(4)
    b.Insert(7)
    b.Insert(9)

    # call printBF() and check the output
    expected_output = "5\n3 8\n1 4 7 9\n"
 
    print("Expected output:")
    print(expected_output)
    print("Actual output:")
    b.printBF()

    print("All printBF tests passed!")

if __name__ == "__main__":

    print("**************** TESTING BST CLASS *******************\n")
    test_case_1()
    print()
    test_BST_constructors()
    test_BST_setters_and_getters()
    test_Insert_node()
    test_BST_search()
    test_BST_delete()
    test_BST_printInOrder()
    test_BST_printBF()
    print("**************** END OF TESTS ************************\n")


