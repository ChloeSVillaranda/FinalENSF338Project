from datastructures.Linear.SLL import SinglyLinkedList

class LLQueue(SinglyLinkedList):
    def __init__(self):
        super().__init__()

    def enqueue(self, node):
        """
        Add a node to the end of the queue.
        """
        self.InsertTail(node)

    def dequeue(self):
        """
        Remove and return the node at the front of the queue.
        """
        node = self.get_head()
        if node is not None:
            self.Delete(node)
        return node

    def is_empty(self):
        """
        Return True if the queue is empty, else False.
        """
        return super().is_empty()

    # Override all the methods in LinkedList that don't apply to queues
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
        super().delete(node)
