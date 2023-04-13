from datastructures.Linear.CSLL import CircularSinglyLinkedList
from datastructures.Linear.CDLL import CircularDoublyLinkedList
from datastructures.nodes.SNode import SNode
from datastructures.nodes.DNode import DNode

def test_clear_csll():
    c = CircularSinglyLinkedList()
    assert c.is_empty() == True
    c.add_head(SNode(1))
    c.add_head(SNode(2))
    c.add_head(SNode(3))
    assert c.is_empty() == False
    c.clear()
    assert c.is_empty() == True
    assert c.get_head() == None
    print("All CircularSinglyLinkedList clear tests pass")

def test_clear_cdll():
    c = CircularDoublyLinkedList()
    assert c.is_empty() == True
    c.add_head(DNode(1))
    c.add_head(DNode(2))
    c.add_head(DNode(3))
    assert c.is_empty() == False
    c.clear()
    assert c.is_empty() == True
    assert c.get_head() == None
    assert c.get_tail() == None
    print("All CircularDoublyLinkedList clear tests pass")
    
test_clear_csll()
test_clear_cdll()
