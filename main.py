# ##Tests for SLL
# # Create a new list
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

#######################################

from datastructures.nodes.TNode import TNode
from datastructures.Trees.BST import bst
from datastructures.Trees.AVL import avl

# Create a TNode
node1 = TNode(10)
node2 = TNode(20)
node3 = TNode(30)

# Test TNode getters
assert node1.get_data() == 10
assert node1.get_left() is None
assert node1.get_right() is None
assert node1.get_parent() is None
assert node1.get_balance() is None

# Test TNode setters
node1.set_data(5)
node1.set_left(node2)
node1.set_right(node3)
node1.set_parent(node2)
node1.set_balance(1)

assert node1.get_data() == 5
assert node1.get_left() == node2
assert node1.get_right() == node3
assert node1.get_parent() == node2
assert node1.get_balance() == 1

# Test BST insert and search
bst = bst()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

assert bst.search(5).get_data() == 5
assert bst.search(8).get_data() == 8
assert bst.search(1) is None

# Test AVL insert and search
avl = avl()
avl.insert(5)
avl.insert(3)
avl.insert(7)
avl.insert(2)
avl.insert(4)
avl.insert(6)
avl.insert(8)

assert avl.search(5).get_data() == 5
assert avl.search(8).get_data() == 8
assert avl.search(1) is None

# Test AVL delete
avl.delete(7)
assert avl.search(7) is None
assert avl.search(8).get_data() == 8
assert avl.search(6).get_data() == 6

# Test BST print in order and breadth-first
bst.print_inorder()  # should print 2 3 4 5 6 7 8
bst.print_bf()  # should print 5 \n 3 7 \n 2 4 6 8

# Test AVL print in order and breadth-first
avl.print_inorder()  # should print 2 3 4 5 6 8
avl.print_bf()  # should print 4 \n 3 6 \n 2 5 8
