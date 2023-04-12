from datastructures.Linear.SLL import SinglyLinkedList
from datastructures.nodes.SNode import SNode
from datastructures.Linear.DLL import DoublyLinkedList
from datastructures.nodes.DNode import DNode
from datastructures.Linear.CSLL import CircularSinglyLinkedList
from datastructures.Linear.CDLL import CircularDoublyLinkedList


def test_singly_linked_list():
    # Create a new linked list
    ll = SinglyLinkedList()

    # Test insert_head method
    ll.insert_head(SNode(1))
    assert ll.head.data == 1
    assert ll.tail.data == 1
    assert ll.size == 1

    # Test insert_tail method
    ll.insert_tail(SNode(2))
    assert ll.head.data == 1
    assert ll.tail.data == 2
    assert ll.size == 2

    # Test insert method
    ll.insert(SNode(3), 1)
    assert ll.head.data == 1
    assert ll.tail.data == 2
    assert ll.size == 3
    assert ll.head.next.data == 3
    assert ll.head.next.next.data == 2

    # Test sorted_insert method
    ll.sorted_insert(SNode(0))
    assert ll.head.data == 0
    assert ll.tail.data == 2
    assert ll.size == 4
    assert ll.head.next.data == 1
    assert ll.head.next.next.data == 3
    assert ll.head.next.next.next.data == 2

    # Test search method
    node = ll.search(SNode(3))
    assert node is not None
    assert node.data == 3

    # Test delete_head method
    ll.delete_head()
    assert ll.head.data == 1
    assert ll.tail.data == 2
    assert ll.size == 3

    # Test delete_tail method
    ll.delete_tail()
    assert ll.head.data == 1
    assert ll.tail.data == 3
    assert ll.size == 2

    # Test delete_node method
    node_to_delete = ll.search(SNode(3))
    ll.delete_node(node_to_delete)
    assert ll.head.data == 1
    assert ll.tail.data == 1
    assert ll.size == 1
    assert ll.head.next is None

    # Test sort method
    ll.insert_head(SNode(3))
    ll.insert_tail(SNode(2))
    ll.insert_head(SNode(5))
    ll.insert_tail(SNode(1))
    ll.sort()
    assert ll.head.data == 1
    assert ll.tail.data == 5
    assert ll.size == 5
    assert ll.head.next.data == 2
    assert ll.head.next.next.data == 3
    assert ll.head.next.next.next.data == 4
    assert ll.head.next.next.next.next.data == 5
    assert ll.head.next.next.next.next.next is None

    # Test print_info method
    captured_output = io.StringIO()
    sys.stdout = captured_output
    ll.print_info()
    sys.stdout = sys.__stdout__
    expected_output = "List length: 5\nSorted status: sorted\nList content:\n1\n2\n3\n4\n5\n"
    assert captured_output.getvalue() == expected_output

    # Test is_sorted method
    assert ll.is_sorted() is True
    ll.insert_tail(SNode(0))
    assert ll.is_sorted() is False


    
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

def test_circular_doubly_linked_list():
        # Test creation of an empty list
        cll = CircularDoublyLinkedList()
        assert cll.head is None
        assert cll.tail is None
        assert cll.size == 0

        # Test insertion at the head
        cll.insert_head(DoublyLinkedList.DNode(1))
        assert cll.head.data == 1
        assert cll.tail.data == 1
        assert cll.size == 1

        # Test insertion at the tail
        cll.insert_tail(DoublyLinkedList.DNode(2))
        assert cll.head.data == 1
        assert cll.tail.data == 2
        assert cll.size == 2

        # Test insertion at a specific position
        cll.insert(DoublyLinkedList.DNode(3), 1)
        assert cll.head.data == 1
        assert cll.tail.data == 2
        assert cll.head.next.data == 3
        assert cll.tail.prev.data == 3
        assert cll.size == 3

        # Test sorted insertion
        cll.sorted_insert(DoublyLinkedList.DNode(0))
        assert cll.head.data == 0
        assert cll.tail.data == 3
        assert cll.is_sorted()
        assert cll.size == 4

        # Test search
        assert cll.search(DoublyLinkedList.DNode(3)).data == 3
        assert cll.search(DoublyLinkedList.DNode(5)) is None

        # Test deletion from the head
        cll.delete_head()
        assert cll.head.data == 1
        assert cll.tail.data == 3
        assert cll.size == 3

        # Test deletion from the tail
        cll.delete_tail()
        assert cll.head.data == 1
        assert cll.tail.data == 2
        assert cll.size == 2

        # Test deletion of a specific node
        cll.delete_node(cll.search(DoublyLinkedList.DNode(3)))
        assert cll.head.data == 1
        assert cll.tail.data == 2
        assert cll.size == 1

        # Test sorting of unsorted list
        cll.insert_tail(DoublyLinkedList.DNode(0))
        cll.insert_tail(DoublyLinkedList.DNode(3))
        cll.sort()
        assert cll.head.data == 0
        assert cll.tail.data == 3
        assert cll.is_sorted()
        assert cll.size == 3

        # Test is_sorted method
        cll.insert_tail(DoublyLinkedList.DNode(2))
        assert cll.is_sorted() is False
        cll.sort()
        assert cll.is_sorted() is True

def main():
    test_singly_linked_list()
    # test_doubly_linked_list()
    # test_circular_singly_linked_list()
    # test_circular_doubly_linked_list()
    # test_ll_stack()

if __name__ == '__main__':
    main()






