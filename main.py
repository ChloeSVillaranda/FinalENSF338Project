from datastructures.Linear.SLL import SinglyLinkedList
from datastructures.nodes.SNode import SNode
from datastructures.Linear.DLL import DoublyLinkedList
from datastructures.nodes.DNode import DNode
from datastructures.Linear.CSLL import CircularSinglyLinkedList
from datastructures.Linear.CDLL import CircularDoublyLinkedList



def test_SinglyLinkedList():
    # Test SinglyLinkedList.InsertHead() method
    list = SinglyLinkedList()
    list.InsertHead(SNode(1))
    assert list.head.data == 1
    assert list.tail.data == 1
    assert list.size == 1

    list.InsertHead(SNode(2))
    assert list.head.data == 2
    assert list.tail.data == 1
    assert list.size == 2

    # Test SinglyLinkedList.InsertTail() method
    list = SinglyLinkedList()
    list.InsertTail(SNode(1))
    assert list.head.data == 1
    assert list.tail.data == 1
    assert list.size == 1

    list.InsertTail(SNode(2))
    assert list.head.data == 1
    assert list.tail.data == 2
    assert list.size == 2

    # Test SinglyLinkedList.Insert() method
    list = SinglyLinkedList()
    list.Insert(SNode(1), 0)
    assert list.head.data == 1
    assert list.tail.data == 1
    assert list.size == 1

    list.Insert(SNode(3), 1)
    assert list.head.data == 1
    assert list.tail.data == 3
    assert list.size == 2

    list.Insert(SNode(2), 1)
    assert list.head.data == 1
    assert list.tail.data == 3
    assert list.size == 3

    # Test SinglyLinkedList.SortedInsert() method
    list = SinglyLinkedList()
    list.SortedInsert(SNode(2))
    assert list.head.data == 2
    assert list.tail.data == 2
    assert list.size == 1

    list.SortedInsert(SNode(1))
    assert list.head.data == 1
    assert list.tail.data == 2
    assert list.size == 2

    list.SortedInsert(SNode(3))
    assert list.head.data == 1
    assert list.tail.data == 3
    assert list.size == 3

    # Test SinglyLinkedList.Search() method
    list = SinglyLinkedList()
    node1 = SNode(1)
    node2 = SNode(2)
    list.InsertHead(node1)
    list.InsertHead(node2)

    assert list.Search(node1) == node1
    assert list.Search(SNode(3)) is None

    # Test SinglyLinkedList.DeleteHead() method
    list = SinglyLinkedList()
    list.InsertHead(SNode(1))
    list.InsertHead(SNode(2))
    list.DeleteHead()
    assert list.head.data == 1
    assert list.tail.data == 1
    assert list.size == 1

    list.DeleteHead()
    assert list.head is None
    assert list.tail is None
    assert list.size == 0

    # Test SinglyLinkedList.DeleteTail() method
    list = SinglyLinkedList()
    list.InsertHead(SNode(1))
    list.InsertHead(SNode(2))
    list.DeleteTail()
    assert list.head.data == 2
    assert list.tail.data == 2
    assert list.size == 1

    list.DeleteTail()
    assert list.head is None
    assert list.tail is None
    assert list.size == 0

    # # Test SinglyLinkedList.Delete() method
    # list = SinglyLinkedList()
    # node1 = SNode(1)
    # node2 = SNode(2)
    # node3 = SNode(3)
    # list.InsertHead(node1)


def main():
    test_SinglyLinkedList
    test_delete
    test_sort
    test_clear
    test_print
    

    

if __name__ == '__main__':
    main()






