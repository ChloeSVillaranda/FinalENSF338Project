from datastructures.Linear.SLL import SinglyLinkedList
from datastructures.nodes.SNode import SNode
class CircularSinglyLinkedList(SinglyLinkedList):
    def __init__(self, head=None):
        super().__init__(head)
        if self.head is not None:
            self.tail.next = self.head

    def InsertHead(self, node):
        super().InsertHead(node)
        if self.size == 1:
            self.tail = node
            self.tail.next = self.head
        else:
            self.tail.next = self.head


    def InsertTail(self, node):
        super().InsertTail(node)
        self.tail.next = self.head

    def Insert(self, node, position):
        if position == 0:
            self.InsertHead(node)
        elif position == self.size:
            self.InsertTail(node)
            self.tail = node
        elif position < self.size:
            current = self.head
            for i in range(position - 1):
                current = current.next
            node.next = current.next
            current.next = node
            self.size += 1

    def SortedInsert(self, node):
        if self.head is None:
            self.head = node
            node.next = node
            self.tail = node
            self.size += 1
            return

        current = self.head
        if current.data >= node.data:
            node.next = current
            self.head = node
            self.tail.next = node
            self.size += 1
            return

        while current.next != self.head and current.next.data < node.data:
            current = current.next

        node.next = current.next
        current.next = node
        if current == self.tail:
            self.tail = node
            self.tail.next = self.head

        self.size += 1



    def DeleteHead(self):
        if self.size > 0:
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.tail.next = self.head.next
                self.head = self.head.next
            self.size -= 1

    def DeleteTail(self):
        if self.size > 0:
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                current = self.head
                while current.next != self.tail:
                    current = current.next
                current.next = self.head
                self.tail = current
            self.size -= 1

    def Delete(self, node):
        current = self.head
        prev = None
        while current is not None:
            if current == node:
                if prev is None:
                    self.head = current.next
                    self.tail.next = self.head
                else:
                    prev.next = current.next
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
            if current.next == self.head:
                break

        # Update head and tail pointers
        self.tail = self.head
        while self.tail.next != self.head:
            self.tail = self.tail.next
        self.tail.next = self.head
    
    def Search(self, node):
        # Create a temporary node pointing to the head
        temp = self.head
        # Create a variable to track the current index
        i = 0 
        # Loop through the list until the end or until the node is found
        while temp != None:
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
        return True


