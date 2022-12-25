from typing import Any


class Node:
    """
    Node for a linked list
    """
    def __init__(self, data: Any):
        self.data: Any = data
        self.next: Node | None = None


class SinglyLinkedList:
    """
    Singly Linked list class
    """

    # Function to initialise the linked list object
    def __init__(self):
        self.head: Node | None = None

    def size(self):
        """
        Returns the number of data elements in the list
        """
        size = 0
        current = self.head

        while current.next is not None:
            size += 1
            current = current.next

        return size

    def empty(self):
        """
        Returns true if list is empty
        """
        return self.head is None

    def value_at(self, index):
        """
        Returns the value of the nth item (starting from 0 for first)
        """
        i = 0
        current = self.head

        while i < index:
            current = current.head
            i += 1

        return current.data

    def push_front(self, value):
        """
        Adds item to the front of the list
        """
        new_node = Node(value)
        new_node.next = self.head

        self.head = new_node

    def push_end(self, value):
        """
        Adds element to the end of the list
        """
        new_node = Node(value)

        last_node = self._last()
        last_node.next = new_node

    def pop_back(self):
        """
        Removes end element and returns its value
        """
        previous = None
        current = self.head

        while current.next is not None:
            previous = current
            current = current.next

        previous.next = None

        return current

    def front(self):
        """
        Return the value from the first item in the list
        """
        return self.head.data

    def back(self):
        """
        Return the value from the last item in the list
        """
        return self._last().data

    def _last(self):
        """
        Returns last item
        """
        current = self.head
        while current.next is not None:
            current = current.next

        return current

    def insert(self, index, value):
        """
        Insert value at index, so the currentent item at that index is pointed to by the new item at the index
        """

        if index == 0:
            self.push_front(value)
            return

        new_node = Node(value)

        i = 0
        previous = None
        current = self.head
        while i is not index:
            previous = current
            current = current.next

            if current is None:
                raise IndexError("Index out of bounds")

            i += 1

        previous.next = new_node
        new_node.next = current

    def erase(self, index):
        """
        Removes node at given index
        """
        if index == 0:
            self.head = self.head.next
            return

        i = 0
        previous = None
        current = self.head

        while i is not index:
            previous = current
            current = current.next
            i += 1

        previous.next = current.next

    def value_n_from_end(self, n: int):
        """
        Returns value from of the node at the nth position from the end of the list
        """
        current = self.head

        i = 0
        while i < n:
            current = current.next
            i += 1

        node_n_from_end = self.head
        while current.next is not None:
            current = current.next
            node_n_from_end = node_n_from_end.next

        return node_n_from_end.data

    def reverse(self):
        """
        Reverse the linked list
        """
        previous = None
        current = self.head
        next = None

        while current.next is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous

    def remove_value(self, value):
        """
        Remove the first item in the list with the given value
        """
        previous = None
        current = self.head

        while current.next is not None:
            if current.data == value:
                break

            previous = current
            current = current.next

        if current.next is None:
            raise ValueError(f"Value {value} not in list")

        previous.next = current.next
