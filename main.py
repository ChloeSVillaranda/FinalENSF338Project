class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

if __name__ == '__main__':
    # Create a new linked list
    linked_list = SinglyLinkedList()

    # Insert nodes at the head and tail of the list
    linked_list.insert_head(Node(1))
    linked_list.insert_tail(Node(3))
    linked_list.insert_head(Node(2))
    linked_list.insert_tail(Node(4))

    # Print the list
    current_node = linked_list.head
    while current_node is not None:
        print(current_node.data)
        current_node = current_node.next

    # Search for a node in the list
    node_to_search = Node(3)
    found_node = linked_list.search(node_to_search)
    if found_node is not None:
        print(f"Found node with data {found_node.data}")
    else:
        print("Node not found")

    # Delete the head and tail nodes of the list
    linked_list.delete_head()
    linked_list.delete_tail()

    # Print the list
    current_node = linked_list.head
    while current_node is not None:
        print(current_node.data)
        current_node = current_node.next

    # Insert a node at a specific position in the list
    linked_list.insert(Node(5), 1)

    # Print the list
    current_node = linked_list.head
    while current_node is not None:
        print(current_node.data)
        current_node = current_node.next

    # Sort the list and print it
    linked_list.sort()
    current_node = linked_list.head
    while current_node is not None:
        print(current_node.data)
        current_node = current_node.next

    # Insert a node in a sorted order
    linked_list.sorted_insert(Node(0))
    linked_list.sorted_insert(Node(6))

    # Print the list
    current_node = linked_list.head
    while current_node is not None:
        print(current_node.data)
        current_node = current_node.next

    # Delete a specific node from the list
    node_to_delete = Node(3)
    linked_list.delete_node(node_to_delete)

    # Print the list
    current_node = linked_list.head
    while current_node is not None:
        print(current_node.data)
        current_node = current_node.next
    
