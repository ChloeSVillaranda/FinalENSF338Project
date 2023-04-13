from datastructures.Linear.SLL import SinglyLinkedList
from datastructures.nodes.SNode import SNode
from datastructures.Linear.DLL import DoublyLinkedList
from datastructures.nodes.DNode import DNode
from datastructures.Linear.CSLL import CircularSinglyLinkedList
from datastructures.Linear.CDLL import CircularDoublyLinkedList
from datastructures.Linear.StackLL import SLLStack
# from datastructures.Linear.QueueLL import QueueStack
# Create an empty stack
stack = SLLStack()

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