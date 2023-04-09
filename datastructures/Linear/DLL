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

    def insert_head(self, node):
        node.next = self.head
        if self.head is not None:
            self.head.prev = node
        else:
            self.tail = node
        self.head = node
        self.size += 1

    def insert_tail(self, node):
        if self.tail is not None:
            self.tail.next = node
            node.prev = self.tail
        else:
            self.head = node
        self.tail = node
        self.size += 1

    def insert(self, node, position):
        if position == 0:
            self.insert_head(node)
        elif position == self.size:
            self.insert_tail(node)
        elif position < self.size:
            current = self.head
            for i in range(position - 1):
                current = current.next
            node.next = current.next
            node.prev = current
            current.next = node
            node.next.prev = node
            self.size += 1

    def sorted_insert(self, node):
        if self.is_sorted():
            current = self.head
            prev = None
            while current is not None and current.data < node.data:
                prev = current
                current = current.next
            if prev is None:
                self.insert_head(node)
            else:
                node.next = current
                node.prev = prev
                prev.next = node
                current.prev = node
            self.size += 1
        else:
            self.sort()
            self.sorted_insert(node)

    def search(self, node):
        current = self.head
        while current is not None:
            if current.data == node.data:
                return current
            current = current.next
        return None

    def delete_head(self):
        if self.size > 0:
            if self.size == 1:
                self.tail = None
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            self.size -= 1

    def delete_tail(self):
        if self.size > 0:
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
            self.size -= 1

    def delete_node(self, node):
        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next
        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev
        self.size -= 1

    def sort(self):
        if self.size <= 1:
            return

        current = self.head.next
        while current is not None:
            node_to_insert = current
            current = current.next
            self.delete_node(node_to_insert)

            prev = None
            insert_after = self.head.next
            while insert_after is not None and insert_after.data <= node_to_insert.data:
                prev = insert_after
                insert_after = insert_after.next

            if prev is None:
                node_to_insert.next = self.head.next
                node_to_insert.prev = self.head
                self.head.next = node_to_insert
                if node_to_insert.next is not None:
                    node_to_insert.next.prev = node_to_insert
            else:
                node_to_insert.next = insert_after
                node_to_insert.prev = prev
                prev.next = node_to_insert
                if insert_after is not None:
                    insert_after.prev = node_to_insert

        

    def print_info(self):
        print("List length:", self.size)
        if self.is_sorted():
            print("Sorted status: sorted")
        else:
            print("Sorted status: unsorted")
        print("List content:")
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

        print("Reverse list content:")
        current = self.tail
        while current is not None:
            print(current.data)
            current = current.prev


    #Adding an is_sorted method
    def is_sorted(self):
        if self.size <= 1:
            return True
        current = self.head
        while current.next is not None:
            if current.data > current.next.data:
                return False
            current = current.next
        while current.prev is not None:
            if current.data < current.prev.data:
                return False
            current = current.prev
        return True


