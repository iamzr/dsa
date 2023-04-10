from abc import ABC, abstractmethod
from math import inf
from typing import List


class BinaryTreeArrayBasedAbstractClass(ABC):

    @abstractmethod
    def __init__(self):
        self.size: int = 0
        self._arr: List[int] = []

    @staticmethod
    def _parent_index(index):
        return (index - 1) // 2

    @staticmethod
    def left_child_index(index):
        return 2 * index + 1

    @staticmethod
    def right_child_index(index):
        return 2 * index - 1

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0


class BinaryHeapAbstractClass(BinaryTreeArrayBasedAbstractClass, ABC):
    @abstractmethod
    def __init__(self, max_size: int):
        super().__init__()
        self.max_size = max_size
        self._arr = [None] * max_size

    def insert(self, value: int) -> None:
        raise NotImplementedError

    def get_max(self):
        return self._arr[0]

    def extract_max(self):
        raise NotImplementedError

    def remove(self, index: int) -> int:
        raise NotImplementedError

    def heapify(self):
        raise NotImplementedError

    def heap_sort(self):
        raise NotImplementedError


class MaxHeap(BinaryHeapAbstractClass):
    def __init__(self, max_size):
        super().__init__(max_size)

    def insert(self, value):
        if self.size == self.max_size:
            raise OverflowError

        self.size += 1
        index = self.size - 1
        self._arr[index] = value

        self._rearrange_tree_from_index(index)

    def extract_max(self):
        if self.size <= 0:
            return None

        if self.size == 1:
            self.size -= 1
            return self._arr[0]

        root = self._arr[0]
        self._arr[0] = self._arr[self.size - 1]
        self.size -= 1

        self.heapify(0)

        return root

    def remove(self, index):
        self._arr[index] = inf
        self._rearrange_tree_from_index(index)
        self.extract_max()

    def heapify(self, index):
        l = self.left_child_index(index)
        r = self.right_child_index(index)

        largest_value_index = index
        if l < self.size and self._arr[l] > self._arr[index]:
            largest_value_index = l
        if r < self.size and self._arr[r] > self._arr[largest_value_index]:
            largest_value_index = r

        if largest_value_index != index:
            temp = self._arr[index]
            self._arr[index] = self._arr[largest_value_index]
            self._arr[index] = temp
            self.heapify(largest_value_index)

    def _rearrange_tree_from_index(self, index):
        """
        Given an index, works from that index up thorugh its parent and re_arranges them until it's in the correct
        place i.e. it's parent is no longer bigger than it. @param index:
        """
        while index != 0 and self._arr[self._parent_index(index)] < self._arr[index]:
            temp = self._arr[index]
            self._arr[index] = self._arr[self._parent_index(index)]
            self._arr[self._parent_index(index)] = temp
            index = self._parent_index(index)
