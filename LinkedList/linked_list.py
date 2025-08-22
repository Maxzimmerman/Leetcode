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

    def reverse(self):
        # loop through and change the direction of the pointer
        curr = self.head
        prev = None
        while curr:
            # me save the next cause by swapping we would lose the connection and end up in a loop
            temp = curr.next
            # swap pointer
            curr.next = prev
            # now we kind of jump over the change and carry on
            prev = curr
            curr = temp
        self.head = prev

    def transform_to_cicle(self):
        new_node = Node()
        new_node.next = self.head
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def is_cicle(self):
        fast = self.head.next
        slow = self.head
        while fast and fast.next:
            if fast == slow:
                return True
            fast = fast.next.next
            slow = slow.next
        return False

    def middle(self):
        slow, fast = self.head, self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        print(f"middle {slow.val}")

    def merge(self, list1):
        dummy = node = Node()
        temp = self.head
        while list1 and temp:
            if list1.val < temp.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = temp
                temp = temp.next
            node = node.next
        node.next = temp if temp else list1
        self.head = dummy.next

    def print(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next