from datastructures.Linear.SLL import SinglyLinkedList
from datastructures.nodes.SNode import SNode
from datastructures.Linear.DLL import DoublyLinkedList
from datastructures.nodes.DNode import DNode
from datastructures.Linear.CSLL import CircularSinglyLinkedList
from datastructures.Linear.CDLL import CircularDoublyLinkedList


# # Test Insert method
# csl = CircularSinglyLinkedList()
# csl.InsertHead(SNode(1))
# csl.InsertHead(SNode(2))
# csl.InsertTail(SNode(4))
# csl.Insert(SNode(3), 2)
# print("testing insert method")
# csl.Print()


# # Test InsertHead and InsertTail methods
# csl = CircularSinglyLinkedList()
# csl.InsertHead(SNode(1))
# assert csl.head.data == 1
# assert csl.head.next.data == 1
# csl.InsertHead(SNode(2))
# assert csl.head.data == 2
# assert csl.head.next.data == 1
# csl.InsertTail(SNode(3))
# assert csl.head.data == 2
# assert csl.head.next.data == 1
# assert csl.head.next.next.data == 3
# assert csl.head.next.next.next.data == 2
# print("testing insert head/tail")
# csl.Print()

# # Test Insert method
# csl = CircularSinglyLinkedList()
# csl.InsertHead(SNode(1))
# csl.InsertHead(SNode(2))
# csl.InsertTail(SNode(4))
# csl.Insert(SNode(3), 2)
# assert csl.head.data == 2
# assert csl.head.next.data == 1
# assert csl.head.next.next.data == 3
# assert csl.head.next.next.next.data == 4
# assert csl.head.next.next.next.next.data == 2
# print("testing insert")
# csl.Print()

# # Test DeleteHead and DeleteTail methods
# csl = CircularSinglyLinkedList()
# csl.InsertHead(SNode(1))
# csl.InsertHead(SNode(2))
# csl.InsertTail(SNode(3))
# csl.DeleteHead()
# assert csl.head.data == 1
# csl.DeleteTail()
# csl.Print()
# assert csl.head.data == 1
# assert csl.head.next.data == 1
# print("testing delete head/tail")
# csl.Print()

# Test Delete method
# csl = CircularSinglyLinkedList()
# csl.InsertHead(SNode(1))
# csl.InsertHead(SNode(2))
# csl.InsertTail(SNode(3))
# csl.Delete(csl.head.next)
# assert csl.head.data == 2
# assert csl.head.next.data == 3
# assert csl.head.next.next.data == 2
# print("testing delete")
# csl.Print()

# Test Delete method
# csl = CircularSinglyLinkedList()
# csl.InsertHead(SNode(1))
# csl.InsertHead(SNode(2))
# csl.InsertTail(SNode(3))
# csl.Delete(csl.head.next)
# csl.Print()
# assert csl.head.data == 2
# assert csl.head.next.data == 3
# assert csl.tail.data == 3
# assert csl.size == 2

# # Test Sort method
# csl = CircularSinglyLinkedList()
# csl.InsertHead(SNode(2))
# csl.InsertHead(SNode(3))
# csl.InsertHead(SNode(1))
# print("The next after head is: ", csl.head.next.data)
# csl.Print()
# csl.Sort()
# csl.Print()
# assert csl.head.data == 1
# assert csl.head.next.data == 2
# assert csl.tail.data == 3
# assert csl.head.next.next.next.data == 1
# assert csl.size == 3

# # Create a new linked list
# my_list = CircularSinglyLinkedList()

# # Add some nodes to the list
# my_list.InsertHead(SNode(1))
# my_list.InsertTail(SNode(2))
# my_list.InsertTail(SNode(3))
# my_list.InsertTail(SNode(4))
# my_list.InsertTail(SNode(5))

# list = CircularSinglyLinkedList()
# node1 = SNode(1)
# node2 = SNode(2)
# list.InsertHead(node1)
# list.InsertHead(node2)

# # Test case 1: Search for existing node
# assert list.Search(node1) == node1

# # Test case 2: Search for non-existing node
# assert list.Search(SNode(3)) is None

# Create a new circular singly linked list
c_list = CircularSinglyLinkedList()

# Test SortedInsert() with an empty list
node1 = SNode(5)
c_list.SortedInsert(node1)
assert c_list.size == 1
assert c_list.head == node1
assert c_list.tail == node1
assert c_list.head.next == c_list.head

# Test SortedInsert() with a larger list
node2 = SNode(3)
node3 = SNode(8)
node4 = SNode(1)
c_list.SortedInsert(node2)
c_list.SortedInsert(node3)
c_list.SortedInsert(node4)
assert c_list.size == 4
assert c_list.head == node4
assert c_list.tail == node3
assert c_list.head.next == node2
assert c_list.head.next.next == node1
assert c_list.tail.next == c_list.head


# Test SortedInsert() with a duplicate value
node5 = SNode(3)
c_list.SortedInsert(node5)
assert c_list.size == 5
assert c_list.head == node4
assert c_list.tail == node3
assert c_list.head.next == node5
assert c_list.head.next.next == node2
assert c_list.tail.next == c_list.head

# Test SortedInsert() with a value larger than the largest value in the list
node6 = SNode(10)
c_list.SortedInsert(node6)
assert c_list.size == 6
assert c_list.head == node4
assert c_list.tail == node6
assert c_list.head.next == node5
assert c_list.head.next.next == node2
assert c_list.tail.next == c_list.head

# Test SortedInsert() with a value smaller than the smallest value in the list
node7 = SNode(0)
c_list.SortedInsert(node7)
assert c_list.size == 7
assert c_list.head == node7
assert c_list.tail == node6
assert c_list.head.next == node4
assert c_list.head.next.next == node5
assert c_list.tail.next == c_list.head
c_list.Print()


