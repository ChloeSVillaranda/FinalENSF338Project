from myLib.datastructures.Linear import *
from myLib.datastructures.Linear.DLL import DoublyLinkedList
from myLib.datastructures.nodes.SNode import SNode
from .DLL import DoublyLinkedList


class CircularDoublyLinkedList(DoublyLinkedList):
    def __init__(self, head=None):
        self.head = head
        self.tail = head
        self.size = 0
        if self.head is not None:
            self.head.prev = self.tail
            self.tail.next = self.head
            self.size += 1
            current = self.head.next
            while current is not self.head:
                current.prev = self.tail
                self.tail.next = current
                self.tail = current
                current = current.next
                self.size += 1

    def InsertHead(self, node):
        super().InsertHead(node)
        if self.size == 1:
            self.tail = node
            self.tail.prev = self.head
            self.head.next = self.tail
        else:
            self.head.prev = self.tail
            self.tail.next = self.head

    def InsertTail(self, node):
        super().InsertTail(node)
        if self.size == 1:
            self.head.next = node
        self.tail.next = self.head
        self.head.prev = node


    def Insert(self, node, position):
        if position == 0:
            self.InsertHead(node)
        elif position == self.size:
            self.InsertTail(node)
        elif position < self.size:
            current = self.head
            for i in range(position - 1):
                current = current.next
            node.next = current.next
            current.next.prev = node  # set the previous node of the next node to the new node
            current.next = node
            node.prev = current  # set the previous node of the new node to the current node
            self.size += 1

    def SortedInsert(self, node):
        if self.head is None:
            self.head = node
            node.next = node
            node.prev = node
            self.tail = node
            self.size += 1
            return

        current = self.head
        if current.data >= node.data:
            node.next = current
            node.prev = self.tail
            self.head = node
            current.prev = node
            self.tail.next = node
            self.size += 1
            return

        while current.next != self.head and current.next.data < node.data:
            current = current.next

        node.next = current.next
        node.prev = current
        current.next.prev = node
        current.next = node
        if current == self.tail:
            self.tail = node
            self.tail.next = self.head
            self.head.prev = self.tail

        self.size += 1


    def Search(self, node):
        # Create a temporary node pointing to the head
        temp = self.head
        # Create a variable to track the current index
        i = 0 
        # Loop through the list until the end or until the node is found
        while temp is not None:
            i += 1
            # If the current node matches the search node, return the current node
            if temp.data == node.data:
                return temp
            temp = temp.next
            # If we've looped back to the head, break the loop
            if temp == self.head:
                break
        # If the node is not found, return None
        return None


    def DeleteHead(self):
        if self.size > 0:
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.tail.next = self.head.next
                self.head = self.head.next
                self.head.prev = self.tail
            self.size -= 1

    def DeleteTail(self):
        if self.size > 0:
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = self.head
                self.head.prev = self.tail
            self.size -= 1

    def Delete(self, node):
        current = self.head
        prev = None
        while current is not None:
            if current == node:
                if prev is None:
                    self.head = current.next
                    self.tail.next = self.head
                    if self.size == 1:
                        self.tail = None
                    else:
                        self.head.prev = self.tail
                else:
                    prev.next = current.next
                    if current == self.tail:
                        self.tail = prev
                        self.head.prev = prev # update prev pointer
                    else:
                        current.next.prev = prev
                self.size -= 1
                return
            prev = current
            current = current.next

    def Sort(self):
        if self.size <= 1:
            return

        current = self.head
        while True:
            index = current.next
            while index != self.head:
                if current.data > index.data:
                    # Swap the data of the two nodes
                    temp = current.data
                    current.data = index.data
                    index.data = temp
                index = index.next
            current = current.next
            if current == self.head:
                break

        # Update tail pointer
        self.tail = self.head.prev

    def Print(self):
        print("List length:", self.size)

        if self.isSorted():
            print("Sorted status: sorted")
        else:
            print("Sorted status: unsorted")

        print("List content:")
        if self.head is not None:
            current = self.head
            print(current.data)
            current = current.next
            while current != self.head:
                print(current.data)
                current = current.next
                if current == self.head:
                    break

    def isSorted(self):
        if self.head is None:
            return True
        current = self.head
        while current.next != self.head:
            if current.data > current.next.data:
                return False
            current = current.next
            if current == self.head:
                break
        return True

