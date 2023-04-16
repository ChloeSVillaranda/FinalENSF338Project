from myLib.datastructures.Linear import *

class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = head
        self.size = 0
        if self.head is not None:
            self.size += 1
            while self.tail.next is not None:
                self.tail = self.tail.next
                self.size += 1

    def InsertHead(self, node):
        node.next = self.head
        if self.head is not None:
            self.head.prev = node
        else:
            self.tail = node
        self.head = node
        self.size += 1

    def InsertTail(self, node):
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1

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
            node.prev = current
            current.next = node
            node.next.prev = node
            self.size += 1

    def SortedInsert(self, node):
        if self.size == 0:
            self.InsertHead(node)
            self.tail = node
            return
        current = self.head
        prev = None
        while current is not None and current.data < node.data:
            prev = current
            current = current.next
        if prev is None:
            self.InsertHead(node)
        else:
            node.next = current
            node.prev = prev
            prev.next = node
            if current is None:
                self.tail = node
            else:
                current.prev = node
            self.size += 1


    def Search(self, node):
        current = self.head
        while current is not None:
            if type(node) == int:
                if current.data == node:
                    return current
            elif type(node) == DNode:
                if current.data == node.data:
                    return current
            current = current.next
        return None


    def DeleteHead(self):
        if self.size > 0:
            if self.size == 1:
                self.tail = None
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            self.size -= 1

    def DeleteTail(self):
        if self.size > 0:
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
            self.size -= 1

    def Delete(self, node):
        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next
        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev
        self.size -= 1

    def Sort(self):
        if self.size <= 1:
            return

        sorted_list = DoublyLinkedList()
        current = self.head

        while current is not None:
            next_node = current.next
            sorted_list.SortedInsert(current)
            current = next_node

        self.head = sorted_list.head
        self.tail = sorted_list.tail
    
    def Clear(self):
        current = self.head
        while current is not None:
            temp = current.next
            current.prev = current.next = None
            current = temp
        self.head = self.tail = None
        self.size = 0

    def Print(self):
        print("List length:", self.size)

        if self.isSorted():
            print("Sorted status: sorted")
        else:
            print("Sorted status: unsorted")

        print("List content:")
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next


    def isSorted(self):
        current = self.head
        while current is not None and current.next is not None:
            if current.data > current.next.data:
                return False
            current = current.next
        return True





        




