from datastructures.Linear.SLL import SinglyLinkedList
from datastructures.nodes.SNode import SNode
from datastructures.Linear.DLL import DoublyLinkedList
from datastructures.nodes.DNode import DNode
from datastructures.Linear.CSLL import CircularSinglyLinkedList
from datastructures.Linear.CDLL import CircularDoublyLinkedList

def test_doubly_linked_list():
    # Test InsertHead
    dll = DoublyLinkedList()
    assert dll.head is None
    assert dll.tail is None
    assert dll.size == 0
    dll.InsertHead(DNode(1))
    assert dll.head.data == 1
    assert dll.tail.data == 1
    assert dll.size == 1

    dll.InsertHead(DNode(2))
    assert dll.head.data == 2
    assert dll.tail.data == 1
    assert dll.head.next.data == 1
    assert dll.tail.prev.data == 2
    assert dll.size == 2

    dll.InsertHead(DNode(3))
    assert dll.head.data == 3
    assert dll.tail.data == 1
    assert dll.head.next.data == 2
    assert dll.tail.prev.data == 2
    assert dll.size == 3

    # Test InsertTail
    dll = DoublyLinkedList()
    dll.InsertTail(DNode(1))
    assert dll.head.data == 1
    assert dll.tail.data == 1
    assert dll.size == 1

    dll.InsertTail(DNode(2))
    assert dll.head.data == 1
    assert dll.tail.data == 2
    assert dll.head.next.data == 2
    assert dll.tail.prev.data == 1
    assert dll.size == 2

    dll.InsertTail(DNode(3))
    assert dll.head.data == 1
    assert dll.tail.data == 3
    assert dll.head.next.next.data == 3
    assert dll.tail.prev.data == 2
    assert dll.size == 3

    # Test Insert
    dll = DoublyLinkedList()
    dll.Insert(DNode(1), 0)
    assert dll.head.data == 1
    assert dll.tail.data == 1
    assert dll.size == 1

    dll.Insert(DNode(2), 0)
    assert dll.head.data == 2
    assert dll.tail.data == 1
    assert dll.head.next.data == 1
    assert dll.tail.prev.data == 2
    assert dll.size == 2

    dll.Insert(DNode(3), 1)
    assert dll.head.data == 2
    assert dll.tail.data == 1
    assert dll.head.next.data == 3
    assert dll.tail.prev.data == 3
    assert dll.size == 3

    dll.Insert(DNode(4), 2)
    assert dll.head.data == 2
    assert dll.tail.data == 1
    assert dll.head.next.next.data == 4
    assert dll.tail.prev.data == 4
    assert dll.size == 4

    # Test SortedInsert
    dll = DoublyLinkedList()
    dll.SortedInsert(DNode(2))
    assert dll.head.data == 2
    assert dll.tail.data == 2
    assert dll.size == 1

    dll.SortedInsert(DNode(1))
    assert dll.head.data == 1
    assert dll.tail.data == 2
    assert dll.head.next.data == 2
    assert dll.tail.prev.data == 1
    assert dll.size == 2

    dll.SortedInsert(DNode(3))
    assert dll.head.data == 1
    assert dll.tail.data == 3
    assert dll.head.next.next.data == 3
    assert dll.tail.prev.data == 2
    assert dll.size == 3

    # Test Search
    dll = DoublyLinkedList()
    n1 = DNode(1)
    n2 = DNode(2)
    n3 = DNode(3)
    dll.InsertHead(n1)
    dll.InsertTail(n2)
    dll.Insert(n3, 1)
    assert dll.Search(1) == n1
    assert dll.Search(2) == n2
    assert dll.Search(3) == n3
    assert dll.Search(4) is None

    # Test DeleteHead
    dll = DoublyLinkedList()
    n1 = DNode(1)
    n2 = DNode(2)
    dll.InsertHead(n1)
    dll.InsertTail(n2)
    assert dll.size == 2
    dll.DeleteHead()
    assert dll.head == n2
    assert dll.tail == n2
    assert dll.size == 1
    dll.DeleteHead()
    assert dll.head is None
    assert dll.tail is None
    assert dll.size == 0

    # Test DeleteTail
    dll = DoublyLinkedList()
    n1 = DNode(1)
    n2 = DNode(2)
    dll.InsertHead(n1)
    dll.InsertTail(n2)
    assert dll.size == 2
    dll.DeleteTail()
    assert dll.head == n1
    assert dll.tail == n1
    assert dll.size == 1
    dll.DeleteTail()
    assert dll.head is None
    assert dll.tail is None
    assert dll.size == 0

    # Test Delete
    dll = DoublyLinkedList()
    n1 = DNode(1)
    n2 = DNode(2)
    n3 = DNode(3)
    dll.InsertHead(n1)
    dll.InsertTail(n2)
    dll.Insert(n3, 1)
    assert dll.size == 3
    dll.Delete(n1)
    assert dll.head == n3
    assert dll.size == 2
    dll.Delete(n2)
    assert dll.tail == n3
    assert dll.size == 1
    dll.Delete(n3)
    assert dll.head is None
    assert dll.tail is None
    assert dll.size == 0

    # Test Sort
    dll = DoublyLinkedList()
    n1 = DNode(1)
    n2 = DNode(2)
    n3 = DNode(3)
    dll.InsertHead(n1)
    dll.InsertTail(n2)
    dll.Insert(n3, 1)
    dll.Print()
    dll.Sort()
    dll.Print()
    
    # Test Clear
    dll = DoublyLinkedList()
    n1 = DNode(1)
    n2 = DNode(2)
    dll.InsertHead(n1)
    dll.InsertTail(n2)
    assert dll.head == n1
    assert dll.tail == n2
    assert dll.size == 2
    dll.Clear()
    assert dll.head is None
    assert dll.tail is None
    assert dll.size == 0



def main():
    test_doubly_linked_list()

if __name__ == '__main__':
    main()


