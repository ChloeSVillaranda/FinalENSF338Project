from datastructures.Linear.SLL import SinglyLinkedList
from datastructures.nodes.SNode import SNode
from datastructures.Linear.DLL import DoublyLinkedList
from datastructures.nodes.DNode import DNode
from datastructures.Linear.CSLL import CircularSinglyLinkedList
from datastructures.Linear.CDLL import CircularDoublyLinkedList
from datastructures.Linear.QueueLL import LLQueue


def test_llqueue():
    q = LLQueue()

    # Test enqueue
    q.enqueue(SNode("A"))
    q.enqueue(SNode("B"))
    q.enqueue(SNode("C"))
    assert q.__str__() == "A -> B -> C -> None"

    # Test dequeue
    assert q.dequeue() == "A"
    assert q.dequeue() == "B"
    assert q.dequeue() == "C"
    assert q.dequeue() is None
    assert q.__str__() == "None"

    # Test is_empty
    assert q.is_empty() == True

    # Test insert_head
    q.insert_head("A")
    assert q.__str__() == "A -> None"

    # Test insert
    q.insert("B", 1)
    assert q.__str__() == "A -> B -> None"

    # Test sorted_insert
    q.sorted_insert("C")
    q.sorted_insert("D")
    assert q.__str__() == "A -> B -> C -> D -> None"

    # Test delete_head
    q.delete_head()
    assert q.__str__() == "B -> C -> D -> None"

    # Test delete_tail
    q.delete_tail()
    assert q.__str__() == "B -> C -> None"

    # Test delete
    node_c = q.get_head().get_next()
    q.delete(node_c)
    assert q.__str__() == "B -> None"

    # Test get_head
    assert q.get_head().get_data() == "B"

    # Test get_tail
    assert q.get_tail().get_data() == "B"

    print("All LLQueue tests pass")


test_llqueue()
