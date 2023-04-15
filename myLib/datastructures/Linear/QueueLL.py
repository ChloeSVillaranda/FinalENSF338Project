from myLib.datastructures.Linear import *
from myLib.datastructures.Linear.SLL import SinglyLinkedList
from myLib.datastructures.nodes.SNode import SNode
from .SLL import SinglyLinkedList

class LLQueue(SinglyLinkedList):
    def __init__(self):
        super().__init__()

    def enqueue(self, node):
        self.InsertTail(node)

    def dequeue(self):
        if self.head is None:
            return None

        node = self.head
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        return node

    def InsertHead(self, node):
        pass

    def Insert(self, node, position):
        pass

    def SortedInsert(self, node):
        pass

    def DeleteHead(self):
        pass

    def DeleteTail(self):
        pass

    def Delete(self, node):
        super().Delete(node)
