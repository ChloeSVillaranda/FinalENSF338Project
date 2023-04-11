from datastructures.Linear.SLL import SinglyLinkedList
from datastructures.nodes.SNode import SNode
from datastructures.Linear.DLL import DoublyLinkedList
from datastructures.nodes.DNode import DNode
from datastructures.Linear.CSLL import CircularSinglyLinkedList
from datastructures.Linear.CDLL import CircularDoublyLinkedList


def test_singly_linked_list():
    # Create an empty list
    sll = SinglyLinkedList()

    # Test that the list is empty
    assert sll.is_empty() == True
    assert sll.length() == 0

    # Test adding items to the list
    sll.add_first(1)
    sll.add_first(2)
    sll.add_last(3)
    assert sll.length() == 3

    # Test removing items from the list
    assert sll.remove_first() == 2
    assert sll.remove_last() == 3
    assert sll.length() == 1

    # Test iterating over the list
    items = [node.data for node in sll]
    assert items == [1]

    # Test searching for an item in the list
    assert sll.contains(1) == True
    assert sll.contains(2) == False

    # Test getting the data of the first and last nodes in the list
    assert sll.get_first() == 1
    assert sll.get_last() == 1

    # Test clearing the list
    sll.clear()
    assert sll.is_empty() == True
    assert sll.length() == 0

    # create some nodes to insert into the list
    node1 = DNode(1)
    node2 = DNode(2)
    node3 = DNode(3)
    node4 = DNode(4)

    # initialize an empty list
    dll = DoublyLinkedList()

    # test insert_head and print_info methods
    dll.insert_head(node2)
    dll.insert_head(node1)
    dll.print_info()  # should print List length: 2, Sorted status: unsorted, List content: 1 2, Reverse list content: 2 1

    # test insert_tail and print_info methods
    dll.insert_tail(node3)
    dll.print_info()  # should print List length: 3, Sorted status: unsorted, List content: 1 2 3, Reverse list content: 3 2 1

    # test insert method and print_info method
    dll.insert(node4, 2)
    dll.print_info()  # should print List length: 4, Sorted status: unsorted, List content: 1 2 4 3, Reverse list content: 3 4 2 1

    # test sorted_insert and print_info methods
    node0 = DNode(0)
    node5 = DNode(5)
    dll.sorted_insert(node0)
    dll.sorted_insert(node5)
    dll.print_info()  # should print List length: 6, Sorted status: sorted, List content: 0 1 2 3 4 5, Reverse list content: 5 4 3 2 1 0

    # test delete_head and print_info methods
    dll.delete_head()
    dll.print_info()  # should print List length: 5, Sorted status: sorted, List content: 1 2 3 4 5, Reverse list content: 5 4 3 2 1

    # test delete_tail and print_info methods
    dll.delete_tail()
    dll.print_info()  # should print List length: 4, Sorted status: sorted, List content: 1 2 3 4, Reverse list content: 4 3 2 1

    # test delete_node and print_info methods
    dll.delete_node(node2)
    dll.print_info()  # should print List length: 3, Sorted status: sorted, List content: 1 3 4, Reverse list content: 4 3 1

    # test search method
    print(dll.search(node3))  # should print DNode object at memory location ...
    print(dll.search(DNode(5)))  # should print None

    # test is_sorted method
    dll.sort()
    dll.print_info()  # should print List length: 3, Sorted status: sorted, List content: 1 3 4, Reverse list content: 4 3 1
    print(dll.is_sorted())  # should print True

    
    def test_circular_singly_linked_list():
        # Create an empty circular singly linked list
        cll = CircularSinglyLinkedList()

        # Test insert_head method
        cll.insert_head(SNode(3))
        assert cll.head.data == 3
        assert cll.tail.data == 3
        assert cll.size == 1

        cll.insert_head(SNode(2))
        assert cll.head.data == 2
        assert cll.tail.data == 3
        assert cll.size == 2

        cll.insert_head(SNode(1))
        assert cll.head.data == 1
        assert cll.tail.data == 3
        assert cll.size == 3

        # Test insert_tail method
        cll.insert_tail(SNode(4))
        assert cll.head.data == 1
        assert cll.tail.data == 4
        assert cll.size == 4

        cll.insert_tail(SNode(5))
        assert cll.head.data == 1
        assert cll.tail.data == 5
        assert cll.size == 5

        # Test insert method
        cll.insert(SNode(0), 0)
        assert cll.head.data == 0
        assert cll.tail.data == 5
        assert cll.size == 6

        cll.insert(SNode(6), 6)
        assert cll.head.data == 0
        assert cll.tail.data == 6
        assert cll.size == 7

        cll.insert(SNode(2.5), 3)
        assert cll.head.data == 0
        assert cll.tail.data == 6
        assert cll.size == 8

        # Test delete_head method
        cll.delete_head()
        assert cll.head.data == 1
        assert cll.tail.data == 6
        assert cll.size == 7

        cll.delete_head()
        assert cll.head.data == 2
        assert cll.tail.data == 6
        assert cll.size == 6

        # Test delete_tail method
        cll.delete_tail()
        assert cll.head.data == 2
        assert cll.tail.data == 5
        assert cll.size == 5

        cll.delete_tail()
        assert cll.head.data == 2
        assert cll.tail.data == 4
        assert cll.size == 4

        # Test delete_node method
        node_to_delete = cll.head.next
        cll.delete_node(node_to_delete)
        assert cll.head.data == 2
        assert cll.tail.data == 4
        assert cll.size == 3

        node_to_delete = cll.tail
        cll.delete_node(node_to_delete)
        assert cll.head.data == 2
        assert cll.tail.data == 3
        assert cll.size == 2

        # Test sort method
        cll.insert_tail(SNode(1))
        cll.insert_tail(SNode(5))
        cll.insert_tail(SNode(3))
        cll.sort()
        assert cll.head.data == 1
        assert cll.tail.data == 5
        assert cll.is_sorted()

        # Test is_sorted method
        cll = CircularSinglyLinkedList()
        cll.insert_tail(SNode(1))
        cll.insert_tail(SNode(2))
        cll.insert_tail(SNode(3))
        assert cll.is_sorted() == True

        cll = CircularSinglyLinkedList()
        cll.insert_tail(SNode(3))
        cll.insert_tail(SNode(2))
        cll.insert_tail(SNode(1))
        assert cll.is_sorted() == False

        cll = CircularSinglyLinkedList()
        cll.insert_tail(SNode(1))
        cll.insert_tail(SNode(3))
        cll.insert_tail(SNode(2))
        assert cll.is_sorted() == False

        cll = CircularSinglyLinkedList()
        cll.insert_tail(SNode(2))
        cll.insert_tail(SNode(1))
        assert cll.is_sorted() == False

        cll = CircularSinglyLinkedList()
        cll.insert_tail(SNode(1))
        assert cll.is_sorted() == True

        cll = CircularSinglyLinkedList()
        assert cll.is_sorted() == True





