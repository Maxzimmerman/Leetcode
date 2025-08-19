from LinkedList.node import Node

class LinkedList:
    def __init__(self):
        self.head = Node()

    def prepand(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def append(self, val):
        new_node = Node(val)
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_first(self):
        new_head = self.head.next
        self.head = new_head

    def delete_last(self):
        prev = None
        current = self.head
        while current.next:
            prev = current
            current = current.next
        prev.next = None

    def print(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next