##Tests for SLL
# Create a new list
# from datastructures.Linear.DLL import DoublyLinkedList
# from datastructures.Linear.SLL import SinglyLinkedList
from contextlib import redirect_stdout
import io
from datastructures.nodes.TNode import TNode
from datastructures.Trees.BST import bst
from datastructures.Trees.AVL import avl



# my_list = SinglyLinkedList()

# # Test insert_head method
# my_list.insert_head(Node(1))
# assert my_list.head.data == 1
# assert my_list.tail.data == 1
# assert my_list.size == 1

# # Test insert_tail method
# my_list.insert_tail(Node(2))
# assert my_list.head.data == 1
# assert my_list.tail.data == 2
# assert my_list.size == 2

# # Test insert method
# my_list.insert(Node(3), 1)
# assert my_list.head.data == 1
# assert my_list.head.next.data == 3
# assert my_list.tail.data == 2
# assert my_list.size == 3

# # Test sorted_insert method
# my_list.sorted_insert(Node(0))
# assert my_list.head.data == 0
# assert my_list.head.next.data == 1
# assert my_list.head.next.next.data == 3
# assert my_list.tail.data == 2
# assert my_list.size == 4

# # Test search method
# node = my_list.search(Node(3))
# assert node.data == 3

# # Test delete_head method
# my_list.delete_head()
# assert my_list.head.data == 1
# assert my_list.head.next.data == 3
# assert my_list.tail.data == 2
# assert my_list.size == 3

# # Test delete_tail method
# my_list.delete_tail()
# assert my_list.head.data == 1
# assert my_list.head.next.data == 3
# assert my_list.tail.data == 3
# assert my_list.size == 2

# # Test delete_node method
# my_list.delete_node(Node(3))
# assert my_list.head.data == 1
# assert my_list.tail.data == 1
# assert my_list.size == 1

# # Test sort method
# my_list.insert_tail(Node(0))
# my_list.insert_tail(Node(2))
# my_list.sort()
# assert my_list.head.data == 0
# assert my_list.head.next.data == 1
# assert my_list.head.next.next.data == 2
# assert my_list.tail.data == 2
# assert my_list.size == 3

# # Test print_info method
# my_list.print_info()
# # Expected output:
# # List length: 3
# # Sorted status: sorted
# # List content:
# # 0
# # 1
# # 2

# # Test is_sorted method
# assert my_list.is_sorted() == True

# # Test is_sorted method on unsorted list
# my_list.insert_tail(Node(-1))
# assert my_list.is_sorted() == False
# linked_list = SinglyLinkedList()
# node1 = Node(4)
# node2 = Node(2)
# node3 = Node(7)
# node4 = Node(1)
# linked_list.insert_head(node1)
# linked_list.insert_tail(node2)
# linked_list.insert_tail(node3)
# linked_list.insert_tail(node4)

# # assert that the linked list is unsorted
# assert not linked_list.is_sorted()

# ##Tests for DLL
# # create an empty list
# my_list = DoublyLinkedList()

# # test insert_head and insert_tail methods
# my_list.insert_head(Node(1))
# my_list.insert_tail(Node(3))
# my_list.insert_head(Node(2))
# my_list.insert_tail(Node(4))
# assert my_list.size == 4
# assert my_list.head.data == 2
# assert my_list.tail.data == 4
# assert my_list.head.next.data == 1
# assert my_list.tail.prev.data == 3

# # test insert method
# my_list.insert(Node(5), 4)
# my_list.insert(Node(0), 0)
# my_list.insert(Node(2.5), 3)
# assert my_list.size == 7
# assert my_list.head.data == 0
# assert my_list.tail.data == 5
# assert my_list.head.next.next.data == 1
# assert my_list.tail.prev.prev.data == 3
# assert my_list.head.next.next.next.data == 2.5

# # test sorted_insert method
# my_list.sorted_insert(Node(1.5))
# my_list.sorted_insert(Node(4.5))
# assert my_list.size == 9
# assert my_list.head.data == 0
# assert my_list.tail.data == 5
# assert my_list.head.next.next.data == 1
# assert my_list.tail.prev.prev.data == 4
# assert my_list.head.next.next.next.data == 1.5
# assert my_list.tail.prev.prev.prev.data == 4.5

# # test search method
# node = my_list.search(Node(1.5))
# assert node is not None
# assert node.data == 1.5
# node = my_list.search(Node(10))
# assert node is None

# # test delete_head method
# my_list.delete_head()
# assert my_list.size == 8
# assert my_list.head.data == 1
# assert my_list.head.prev is None
# assert my_list.head.next.data == 1.5

# # test delete_tail method
# my_list.delete_tail()
# assert my_list.size == 7
# assert my_list.tail.data == 4
# assert my_list.tail.next is None
# assert my_list.tail.prev.data == 3

# # test delete_node method
# node = my_list.search(Node(3))
# my_list.delete_node(node)
# assert my_list.size == 6
# assert my_list.head.next.next.data == 1.5
# assert my_list.tail.prev.data == 4.5

# # test sort method
# my_list.sort()
# assert my_list.head.data == 0
# assert my_list.tail.data == 5
# assert my_list.head.next.next.data == 1
# assert my_list.tail.prev.prev.data == 4
# assert my_list.head.next.next.next.data == 1.5
# assert my_list.tail.prev.prev.prev.data == 4.5

# # test print_info method
# my_list.print_info()

######################################

from datastructures.nodes.TNode import TNode

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

    print("All tests passed!")



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

    # search for existing value
    node = b.search(4)
    assert node.data == 4

    # search for non-existing value
    node = b.search(9)
    assert node is None
   
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
    print("Value 2 not found in tree")

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

    # create an AVL tree using the overload constructor with a value of 5
    avl2 = avl(5)

    # check that the root has a value of 5 and both the left and right child are None
    assert avl2.root.data == 5
    assert avl2.root.left is None
    assert avl2.root.right is None

    # create an AVL tree using the overload constructor with a TNode object


    tnode1 = TNode(5)
    tnode2 = TNode(10)
    tnode3 = TNode(15)
    tnode4 = TNode(20)
    tnode5 = TNode(25)

    tnode1.left = tnode2
    tnode1.right = tnode3
    tnode2.left = tnode4
    tnode3.right = tnode5

    avl1 = avl(tnode1)

    # check that the AVL tree is created correctly from the TNode object
    assert avl1.root.data == 10
    assert avl1.root.left.data == 5
    assert avl1.root.left.left is None
    assert avl1.root.left.right is None
    assert avl1.root.right.data == 20
    assert avl1.root.right.left.data == 15
    assert avl1.root.right.right.data == 25
    assert avl1.root.right.left.left is None
    assert avl1.root.right.left.right is None
    assert avl1.root.right.right.left is None
    assert avl1.root.right.right.right is None


if __name__ == "__main__":
    main()
    test_bst_constructors()
    test_bst_setters_and_getters()
    test_insert_node()
    test_bst_search()
    test_bst_delete()
    test_bst_printInOrder()

    test_bst_printBF()
    test_avl_constructors()


