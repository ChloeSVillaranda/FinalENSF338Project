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

# Test Sort method
csl = CircularSinglyLinkedList()
csl.InsertHead(SNode(2))
csl.InsertHead(SNode(3))
csl.InsertHead(SNode(1))
print("The next after head is: ", csl.head.next.data)
csl.Print()
csl.Sort()
csl.Print()
assert csl.head.data == 1
assert csl.head.next.data == 2
assert csl.tail.data == 3
assert csl.head.next.next.next.data == 1
assert csl.size == 3
