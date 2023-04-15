from datastructures.Linear.SLL import SinglyLinkedList
class LLStack(SinglyLinkedList):
    def __init__(self):
        super().__init__()

    def push(self, node):
        self.InsertHead(node)

    def pop(self):
        node = self.head
        self.DeleteHead()
        return node

    def peek(self):
        return self.head

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def Clear(self):
        super().Clear()

    def InsertTail(self, node):
        pass

    def Insert(self, node, position):
        pass

    def SortedInsert(self, node):
        pass

    def DeleteTail(self):
        pass

    def isSorted(self):
        pass
