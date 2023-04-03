from abc import ABC, abstractmethod


class HashTableBase(ABC):
    def hash_function(self, **kwargs):
        raise NotImplementedError

    def add(self, value):
        raise NotImplementedError

    def exists(self, value):
        raise NotImplementedError

    def get(self, value):
        raise NotImplementedError

    def remove(self, value):
        raise NotImplementedError

    def __init__(self, size):
        self._table = [None] * size
        self._size = size

class HashTableWithTrivialMapping(HashTableBase):

    @staticmethod
    def hash_function(value):
        return value

    def exists(self, value):
        return self._table[self.hash_function(value)] == value

    def get(self, value):
        return self._table[self.hash_function(value)]

    def remove(self, value):
        self._table[self.hash_function(value)] = None

    def add(self, value):
        self._table[self.hash_function(value)] = value


class HashTableWithModuloMapping(HashTableWithTrivialMapping):
    def hash_function(self, value):
        return value % self._size


class HashTableWithModuloMappingLinearProbing(HashTableBase):

    def hash_function(self, value, offset):
        return (value + offset) % self._size

    def add(self, value):
        offset = 0
        while self._table[self.hash_function(value, offset)] is not None and offset < self._size:
            offset += 1

        self._table[self.hash_function(value, offset)] = value

    def _get(self, value):
        offset = 0
        while self._table[self.hash_function(value, offset)] != value and offset < self._size:
            offset += 1
        return value, offset

    def get(self, value):
        return self._get(value)[0]

    def remove(self, value):
        offset = self._get(value)[1]
        self._table[self.hash_function(value, offset)] = None

    def exists(self, value):
        index = value
        offset = 0
        while self._table[self.hash_function(index, offset)] != value and offset < self._size:
            offset += 1

        if offset >= self._size:
            return False

        return self._table[self.hash_function(index, offset)] == value
