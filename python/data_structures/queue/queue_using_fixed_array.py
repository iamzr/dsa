class Queue:
    def __init__(self, capacity):
        self._front = 0
        self._rear = -1
        self._size = 0
        self._queue = [None] * capacity
        self._capacity = capacity

    def dequeue(self):
        if self.is_empty():
            raise IndexError("The queue is empty")

        dequeued_element = self._queue[self._front]
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return dequeued_element

    def enqueue(self, item):
        if self.is_full():
            raise IndexError("The queue is full")

        self._rear = (self._rear + 1) % self._capacity
        self._queue[self._rear] = item
        self._size += 1

    def front(self):
        return self._queue[self._front]

    def rear(self):
        return self._queue[self._rear]

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._size == self._capacity
