from myLib.datastructures.Linear.SLL import SinglyLinkedList
from myLib.datastructures.nodes.SNode import SNode
from myLib.datastructures.Linear.DLL import DoublyLinkedList
from myLib.datastructures.nodes.DNode import DNode
from myLib.datastructures.Linear.CSLL import CircularSinglyLinkedList
from myLib.datastructures.Linear.CDLL import CircularDoublyLinkedList




def test_SinglyLinkedList():
    # Test SinglyLinkedList.InsertHead() method
    list = SinglyLinkedList()
    assert list.head is None
    assert list.tail is None
    assert list.size == 0
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

    # Test SinglyLinkedList.Delete() method
    list = SinglyLinkedList()
    node1 = SNode(1)
    node2 = SNode(2)
    node3 = SNode(3)
    list.InsertHead(node1)

# Tests for Delete()
def test_delete():
    # Create a linked list with some nodes
    linked_list = SinglyLinkedList()
    linked_list.InsertTail(SNode(1))
    linked_list.InsertTail(SNode(2))
    linked_list.InsertTail(SNode(3))
    
    # Delete the first node
    linked_list.Delete(SNode(1))
    assert linked_list.Search(SNode(1)) is None
    assert linked_list.size == 2
    assert linked_list.head.data == 2
    
    # Delete the last node
    linked_list.Delete(SNode(3))
    assert linked_list.Search(SNode(3)) is None
    assert linked_list.size == 1
    assert linked_list.head.data == 2
    
    # Delete a node in the middle
    linked_list.InsertTail(SNode(3))
    linked_list.InsertTail(SNode(4))
    linked_list.Delete(SNode(2))

    assert linked_list.Search(SNode(2)) is None
    print("The linked size here is: ", linked_list.size)
    assert linked_list.size == 2
    assert linked_list.head.data == 3
    assert linked_list.tail.data == 4


# Tests for Sort()
def test_sort():
    # Create an unsorted linked list
    linked_list = SinglyLinkedList()
    linked_list.InsertTail(SNode(3))
    linked_list.InsertTail(SNode(1))
    linked_list.InsertTail(SNode(4))
    linked_list.InsertTail(SNode(2))
    linked_list.Print()


    # Sort the linked list
    linked_list.Sort()
    linked_list.Print()
    assert linked_list.size == 4
    assert linked_list.head.data == 1
    print("the data of the head is: ", linked_list.head.data)
    print("the data of the tail is: ", linked_list.tail.data)
    assert linked_list.tail.data == 4

    # Create an already sorted linked list
    linked_list = SinglyLinkedList()
    linked_list.InsertTail(SNode(1))
    linked_list.InsertTail(SNode(2))
    linked_list.InsertTail(SNode(3))
    linked_list.InsertTail(SNode(4))

    # Sort the linked list (should not change anything)
    linked_list.Sort()
    assert linked_list.size == 4
    assert linked_list.head.data == 1
    assert linked_list.tail.data == 4


# Tests for Clear()
def test_clear():
    # Create a linked list with some nodes
    linked_list = SinglyLinkedList()
    linked_list.InsertTail(SNode(1))
    linked_list.InsertTail(SNode(2))
    linked_list.InsertTail(SNode(3))
    
    # Clear the linked list
    linked_list.Clear()
    assert linked_list.size == 0
    assert linked_list.head is None
    assert linked_list.tail is None


# Tests for Print()
def test_print():
    # Create a linked list with some nodes
    linked_list = SinglyLinkedList()
    linked_list.InsertTail(SNode(1))
    linked_list.InsertTail(SNode(2))
    linked_list.InsertTail(SNode(3))

    # Print the linked list
    linked_list.Print()

    # Expected output:
    # List length: 3
    # Sorted status: sorted
    # List content:
    # 1
    # 2
    # 3


def main():
    test_SinglyLinkedList()
    test_delete()
    test_sort()
    test_clear()
    test_print()
    

    

if __name__ == '__main__':
    main()






