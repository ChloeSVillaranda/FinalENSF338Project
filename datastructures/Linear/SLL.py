class SinglyLinkedList:
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
        self.head = node
        if self.size == 0:
            self.tail = node
        self.size += 1

    def insert_tail(self, node):
        if self.size == 0:
            self.head = node
        else:
            self.tail.next = node
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
            current.next = node
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
                prev.next = node
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
            self.size -= 1

    def delete_tail(self):
        if self.size > 0:
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                current = self.head
                while current.next != self.tail:
                    current = current.next
                current.next = None
                self.tail = current
            self.size -= 1

    def delete_node(self, node):
        current = self.head
        prev = None
        while current is not None:
            if current.data == node.data:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                if current.next is None:
                    self.tail = prev
                self.size -= 1
                return
            prev = current
            current = current.next

    def sort(self):
        if self.size <= 1:
            return

        current = self.head.next
        while current is not None:
            node_to_insert = current
            current = current.next
            self.delete_node(node_to_insert)

            prev = None
            insert_after = self.head
            while insert_after is not None and insert_after.data <= node_to_insert.data:
                prev = insert_after
                insert_after = insert_after.next

            if prev is None:
                self.insert_head(node_to_insert)
            else:
                node_to_insert.next = insert_after
                prev.next = node_to_insert
    

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

    #Adding an is_sorted method
    def is_sorted(self):
        if self.size <= 1:
            return True
        current = self.head
        while current.next is not None:
            if current.data > current.next.data:
                return False
            current = current.next
        return True

