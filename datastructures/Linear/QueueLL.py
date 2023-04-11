from datastructures.Linear.SLL import SinglyLinkedList
from datastructures.nodes.SNode import SNode
class LLQueue(SinglyLinkedList):
    def __init__(self):
        super().__init__()
        self.tail = None

    def enque(self, value):
        node = SNode(value)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.length += 1

    def dequeue(self):
        return self.pop_front()

    def size(self):
        return self.length
