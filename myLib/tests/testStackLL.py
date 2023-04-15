from myLib.datastructures.Linear.SLL import SinglyLinkedList
from myLib.datastructures.nodes.SNode import SNode
from myLib.datastructures.Linear.DLL import DoublyLinkedList
from myLib.datastructures.nodes.DNode import DNode
from myLib.datastructures.Linear.CSLL import CircularSinglyLinkedList
from myLib.datastructures.Linear.CDLL import CircularDoublyLinkedList
from myLib.datastructures.Linear.StackLL import LLStack


def test_Stack():
    # from datastructures.Linear.QueueLL import QueueStack
    # Create an empty stack
    stack = LLStack()

    # Test pushing elements onto the stack
    stack.push(SNode(1))
    stack.push(SNode(2))
    stack.push(SNode(3))

    # Test peeking at the top element of the stack
    assert stack.peek().data == 3

    # Test popping elements off the stack
    assert stack.pop().data == 3
    assert stack.pop().data == 2

    # Test checking if the stack is empty
    assert stack.is_empty() == False

    # Test clearing the stack
    stack.Clear()
    assert stack.is_empty() == True

    # Test pushing and popping from an empty stack
    stack.push(SNode(10))
    assert stack.pop().data == 10

    # Test pushing and popping a single element
    stack.push(SNode(5))
    assert stack.pop().data == 5
    assert stack.is_empty() == True


if __name__ == "__main__":
    test_Stack

    