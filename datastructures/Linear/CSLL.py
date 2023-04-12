from datastructures.Linear.SLL import SinglyLinkedList
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


    def DeleteHead(self):
        if self.size > 0:
            if self.size == 1:
                self.tail = None
            self.head = self.head.next
            self.tail.next = self.head
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

        current = self.head.next
        while current is not None:
            node_to_insert = current
            current = current.next
            self.Delete(node_to_insert)

            prev = None
            insert_after = self.head
            while insert_after is not None and insert_after.data <= node_to_insert.data:
                prev = insert_after
                insert_after = insert_after.next
                if insert_after == self.head:
                    break

            if prev is None:
                self.InsertHead(node_to_insert)
            else:
                node_to_insert.next = insert_after
                prev.next = node_to_insert
                
    def Print(self):
        print("List length:", self.size)
        
        sorted_status = True
        prev_node = self.head.next
        current_node = prev_node.next
        while current_node is not None:
            if current_node.data < prev_node.data:
                sorted_status = False
                break
            prev_node = current_node
            current_node = current_node.next

        if sorted_status:
            print("Sorted status: sorted")
        else:
            print("Sorted status: unsorted")

        print("List content:")
        current = self.head.next
        while current is not None:
            print(current.data)
            current = current.next

