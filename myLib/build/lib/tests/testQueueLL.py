from myLib.datastructures.Linear.SLL import SinglyLinkedList
from myLib.datastructures.nodes.SNode import SNode
from myLib.datastructures.Linear.DLL import DoublyLinkedList
from myLib.datastructures.nodes.DNode import DNode
from myLib.datastructures.Linear.CSLL import CircularSinglyLinkedList
from myLib.datastructures.Linear.CDLL import CircularDoublyLinkedList
from myLib.datastructures.Linear.QueueLL import LLQueue
import unittest

class TestQueueLL(unittest.TestCase):
    def test_enqueue_and_dequeue(self):
        queue = LLQueue()
        node1 = SNode(1)
        node2 = SNode(2)
        node3 = SNode(3)
        queue.enqueue(node1)
        queue.enqueue(node2)
        queue.enqueue(node3)
        self.assertEqual(queue.dequeue(), node1)
        self.assertEqual(queue.dequeue(), node2)
        self.assertEqual(queue.dequeue(), node3)
        self.assertIsNone(queue.dequeue())

    def test_delete(self):
        queue = LLQueue()
        node1 = SNode(1)
        node2 = SNode(2)
        node3 = SNode(3)
        queue.enqueue(node1)
        queue.enqueue(node2)
        queue.enqueue(node3)
        queue.Delete(node2)
        self.assertEqual(queue.dequeue(), node1)
        self.assertEqual(queue.dequeue(), node3)
        self.assertIsNone(queue.dequeue())

if __name__ == '__main__':
    unittest.main()
