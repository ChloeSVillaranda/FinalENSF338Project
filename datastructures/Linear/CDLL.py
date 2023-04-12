from datastructures.Linear.DLL import DoublyLinkedList
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
        node.next = self.head
        node.prev = self.tail
        if self.head is not None:
            self.head.prev = node
        else:
            self.tail.next = node
        self.head = node
        self.tail.next = self.head
        self.size += 1

    def InsertTail(self, node):
        if self.tail is not None:
            node.prev = self.tail
            node.next = self.head
            self.tail.next = node
            self.head.prev = node
        else:
            self.head = node
            self.tail = node
            node.next = self.head
            node.prev = self.tail
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
        current = self.head
        prev = None
        while current is not self.head and current.data < node.data:
            prev = current
            current = current.next

        if prev is None:
            self.InsertHead(node)
        else:
            node.next = current
            node.prev = prev
            prev.next = node
            if current is not self.head:
                current.prev = node

        self.size += 1


    def Search(self, node):
        current = self.head
        while current is not self.head:
            if current.data == node.data:
                return current
            current = current.next
        return None

    def DeleteHead(self):
        if self.size > 0:
            if self.size == 2:
                self.tail = None
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head
            self.size -= 1

    def DeleteTail(self):
        if self.size > 0:
            if self.size == 2:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = self.head
                self.head.prev = self.tail
            self.size -= 1

    def Delete(self, node):
        if self.head == node:
            self.head = node.next
        if self.tail == node:
            self.tail = node.prev
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def Sort(self):
        if self.size <= 1:
            return

        current = self.head.next
        while current is not self.head:
            node_to_insert = current
            current = current.next
            self.delete_node(node_to_insert)

            prev = None
            insert_after = self.head.next
            while insert_after is not self.head and insert_after.data <= node_to_insert.data:
                prev = insert_after
                insert_after = insert_after.next

            if prev is None:
                node_to_insert.next = self.head.next
                node_to_insert.prev = self.head
                self.head.next.prev = node_to_insert
                self.head.next = node_to_insert
            else:
                node_to_insert.next = insert_after
                node_to_insert.prev = prev
                prev.next = node_to_insert
                if insert_after is not self.head:
                    insert_after.prev = node_to_insert
    

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
