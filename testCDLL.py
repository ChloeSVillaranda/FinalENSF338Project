from datastructures.Linear.SLL import SinglyLinkedList
from datastructures.nodes.SNode import SNode
from datastructures.Linear.DLL import DoublyLinkedList
from datastructures.nodes.DNode import DNode
from datastructures.Linear.CSLL import CircularSinglyLinkedList
from datastructures.Linear.CDLL import CircularDoublyLinkedList

# create an empty list
cdll = CircularDoublyLinkedList()

# test InsertHead()
cdll.InsertHead(DNode(1))
assert cdll.head.data == 1
assert cdll.tail.data == 1
assert cdll.size == 1

cdll.InsertHead(DNode(2))
assert cdll.head.data == 2
assert cdll.tail.data == 1
assert cdll.head.prev.data == 1
assert cdll.tail.next.data == 2
assert cdll.size == 2

cdll.InsertHead(DNode(3))
assert cdll.head.data == 3
assert cdll.tail.data == 1
assert cdll.head.prev.data == 1
assert cdll.tail.next.data == 3
assert cdll.size == 3

# test InsertTail()
cdll.InsertTail(DNode(4))
assert cdll.head.data == 3
assert cdll.tail.data == 4
assert cdll.tail.next.data == 3
assert cdll.head.prev.data == 4
assert cdll.size == 4

cdll.InsertTail(DNode(5))
assert cdll.head.data == 3
assert cdll.tail.data == 5
assert cdll.tail.next.data == 3
assert cdll.head.prev.data == 5
assert cdll.size == 5

# test Insert()
cdll.Insert(DNode(6), 2)
assert cdll.head.data == 3
assert cdll.head.next.data == 2
assert cdll.head.next.next.data == 6
assert cdll.head.next.next.next.data == 1
assert cdll.tail.prev.data == 4
assert cdll.tail.data == 5
assert cdll.size == 6

cdll.Insert(DNode(7), 0)
assert cdll.head.data == 7
assert cdll.head.prev.data == 5
assert cdll.head.next.data == 3
assert cdll.tail.data == 5
assert cdll.tail.next.data == 7
assert cdll.size == 7

cdll.Insert(DNode(8), 7)
assert cdll.head.data == 7
assert cdll.tail.data == 8
assert cdll.tail.prev.data == 5
assert cdll.tail.next.data == 7
assert cdll.head.next.next.next.next.next.next.data == 5
assert cdll.size == 8

# test SortedInsert()
cdll.SortedInsert(DNode(0))
print("stuck at 1")
assert cdll.head.data == 0
assert cdll.head.next.data == 7
assert cdll.tail.prev.data == 5
assert cdll.tail.data == 8
assert cdll.size == 9
print("prints all the tests at 1")

cdll.SortedInsert(DNode(9))
print("stuck at 2")
assert cdll.tail.data == 9
assert cdll.tail.prev.data == 8
assert cdll.tail.prev.prev.data == 7
assert cdll.size == 10

# test Search()
node = cdll.Search(DNode(3))
assert node.data == 3

node = cdll.Search(DNode(11))
assert node is None

# test DeleteHead()
cdll.DeleteHead()
assert cdll.head.data == 1
assert cdll.head.prev.data == 9
assert cdll.tail.next.data == 1
assert cdll.size == 9

# test DeleteTail()
cdll.DeleteTail()
assert cdll.tail.data == 8
assert cdll.tail.next.data == 0
