import ctypes


class Vector:
    """
    Class that implements a vector i.e. a mutable array with automatic resizing.
    """

    def __init__(self):
        self._n = 0
        self._capacity = 16
        self._A = self._make_array(self._capacity)

    def _make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def size(self):
        """
        Size of the Vector.
        """
        return self._n

    def capacity(self):
        """
        Capacity of the Vector.
        """
        return self._capacity

    def is_empty(self):
        """
        Returns boolean depending on is the Vector is empty.
        """
        if self._n == 0:
            return True
        return False

    def at(self, index):
        """
        Returns item at given index raises error if index is out of bounds.
        """
        if index > self._n:
            raise IndexError(
                f"Index out of bounds. You called index {index}, but the size of the Vector is {self._n}")

        if index < 0:
            raise IndexError(
                f"Index out bounds. Please enter a non-negative intger")

        return self._A[index]

    def push(self, item):
        """
        Adds item to the end of the Vector.
        """
        if self._n == self._capacity:
            # Double capacity if not enough room
            self.resize(2 * self._capacity)

        self._A[self._n] = item
        self._n += 1

    def insert(self, index, item):
        """
        Inserts item at given index and shifts that index's value and trailing elements to the right.
        """
        if index < 0 or index > self._capacity:
            raise IndexError("Index out of bounds")

        if self._n == self._capacity:
            self.resize()

        for i in range(self._n-1, index-1, -1):
            self._A[i+1] = self._A[i]

        self._A[index] = item
        self._n += 1

    def prepend(self, item):
        """
        Inserts elements to the front of the Vector.
        """
        self.insert(0, item)

    def pop(self):
        """
        Removes element from the end of the array and returns it.
        """
        last_element = self._A[-1]
        self._A[-1] = None
        self._n -= 1

        return last_element

    def delete(self, index):
        """
        Deletes an element at a given index
        """
        if index < 0 or index > self._capacity:
            raise IndexError("Index out of bounds")

        for i in range(index, self._n-1):
            self._A[i] = self._A[i+1]

        self._n -= 1

    def remove(self, item):
        """
        Looks for a value and removes the first occurence
        """
        for k, v in enumerate(self._n):
            if v == item:
                self.delete(k)
                self._n -= 1
                return

        raise ValueError(f"Value {item} not in list")

    def find(self, item):
        """
        Looks for an value and returns first index with that value
        """
        raise NotImplementedError

    def resize(self, new_capacity=None):
        if new_capacity == None:
            new_capacity = self._capacity * 2

        B = self._make_array(new_capacity)

        for i in range(self._n):
            B[i] = self._A[i]

        self._A = B
        self._capacity = new_capacity
