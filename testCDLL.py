from datastructures.Linear.SLL import SinglyLinkedList
from datastructures.nodes.SNode import SNode
from datastructures.Linear.DLL import DoublyLinkedList
from datastructures.nodes.DNode import DNode
from datastructures.Linear.CSLL import CircularSinglyLinkedList
from datastructures.Linear.CDLL import CircularDoublyLinkedList

# # create an empty list
# cdll = CircularDoublyLinkedList()

# # test InsertHead()
# cdll.InsertHead(DNode(1))
# assert cdll.head.data == 1
# assert cdll.tail.data == 1
# assert cdll.size == 1

# cdll.InsertHead(DNode(2))
# assert cdll.head.data == 2
# assert cdll.tail.data == 1
# assert cdll.head.prev.data == 1
# assert cdll.tail.next.data == 2
# assert cdll.size == 2

# cdll.InsertHead(DNode(3))
# assert cdll.head.data == 3
# assert cdll.tail.data == 1
# assert cdll.head.prev.data == 1
# assert cdll.tail.next.data == 3
# assert cdll.size == 3

# # test InsertTail()
# cdll.InsertTail(DNode(4))
# assert cdll.head.data == 3
# assert cdll.tail.data == 4
# assert cdll.tail.next.data == 3
# assert cdll.head.prev.data == 4
# assert cdll.size == 4

# cdll.InsertTail(DNode(5))
# assert cdll.head.data == 3
# assert cdll.tail.data == 5
# assert cdll.tail.next.data == 3
# assert cdll.head.prev.data == 5
# assert cdll.size == 5

# # test Insert()
# cdll.Insert(DNode(6), 2)
# assert cdll.head.data == 3
# assert cdll.head.next.data == 2
# assert cdll.head.next.next.data == 6
# assert cdll.head.next.next.next.data == 1
# assert cdll.tail.prev.data == 4
# assert cdll.tail.data == 5
# assert cdll.size == 6

# cdll.Insert(DNode(7), 0)
# assert cdll.head.data == 7
# assert cdll.head.prev.data == 5
# assert cdll.head.next.data == 3
# assert cdll.tail.data == 5
# assert cdll.tail.next.data == 7
# assert cdll.size == 7

# cdll.Insert(DNode(8), 7)
# assert cdll.head.data == 7
# assert cdll.tail.data == 8
# assert cdll.tail.prev.data == 5
# assert cdll.tail.next.data == 7
# assert cdll.head.next.next.next.next.next.next.data == 5
# assert cdll.size == 8

# # test SortedInsert()
# cdll.SortedInsert(DNode(0))
# assert cdll.head.data == 0
# assert cdll.head.next.data == 7
# assert cdll.tail.prev.data == 5
# assert cdll.tail.data == 8
# assert cdll.size == 9

# cdll.SortedInsert(DNode(9))
# assert cdll.tail.data == 9
# assert cdll.tail.prev.data == 8
# assert cdll.size == 10

# # test Search()
# node = cdll.Search(DNode(3))
# assert node.data == 3

# node = cdll.Search(DNode(11))
# assert node is None


# # test DeleteHead()
# cdll.DeleteHead()
# assert cdll.head.data == 7
# assert cdll.head.prev.data == 9
# assert cdll.size == 9
# cdll.Print()

# # test DeleteTail()
# cdll.DeleteTail()
# cdll.Print()


def test_delete_node():
    # Initialize the linked list
    node1 = DNode(1)
    node2 = DNode(2)
    node3 = DNode(3)
    node4 = DNode(4)
    node5 = DNode(5)
    cll = CircularDoublyLinkedList()
    cll.InsertHead(node5)
    cll.InsertHead(node4)
    cll.InsertHead(node3)
    cll.InsertHead(node2)
    cll.InsertHead(node1)
    cll.Print()

    # Test deleting head node
    cll.Delete(node1)
    assert cll.head == node2
    assert cll.head.prev == cll.tail
    assert cll.tail.next == cll.head
    assert cll.size == 4

    # Test deleting tail node
    cll.Delete(node5)
    cll.Print()
    assert cll.tail == node4
    assert cll.tail.next == cll.head
    print("head prev is: ", cll.head.prev.data)
    print("tail is: ", cll.tail.data)
    assert cll.head.prev == cll.tail
    assert cll.size == 3

    # Test deleting middle node
    cll.Delete(node3)
    assert cll.head.next == node4
    assert cll.tail.prev == node2
    assert cll.size == 2
    cll.Print()
    print("all tests done")


def test_sort_list():
    # Initialize the linked list
    node1 = DNode(1)
    node2 = DNode(5)
    node3 = DNode(3)
    node4 = DNode(2)
    node5 = DNode(4)
    cll = CircularDoublyLinkedList()
    cll.InsertHead(node3)
    cll.InsertHead(node2)
    cll.InsertHead(node1)
    cll.InsertHead(node5)
    cll.InsertHead(node4)
    cll.Print()

    # Sort the list
    cll.Sort()

    # Check that the list is sorted
    cll.Clear()
    cll.Print()
    assert cll.head == None



def main():
    # test_delete_node()
    test_sort_list()

if __name__ == '__main__':
    main()

