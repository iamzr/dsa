from abc import ABC


class HashTableBase(ABC):

    def add(self, key):
        raise NotImplementedError

    def exists(self, key):
        raise NotImplementedError

    def get(self, key):
        raise NotImplementedError

    def remove(self, key):
        raise NotImplementedError


class HashTableWithTrivialMapping(HashTableBase):

    @staticmethod
    def hash_function(key):
        return key

    def exists(self, key):
        return self._table[self.hash_function(key)] == key

    def get(self, key):
        return self._table[self.hash_function(key)]

    def remove(self, key):
        self._table[self.hash_function(key)] = None

    def add(self, key):
        self._table[self.hash_function(key)] = key

    def __init__(self, size):
        self._table = [None] * size
        self._size = size


class HashTableWithModuloMapping(HashTableWithTrivialMapping):
    def hash_function(self, key):
        return key % self._size


class HashTableWithModuloMappingLinearProbing(HashTableWithModuloMapping):

    def add(self, key):
        counter = 0
        index = key
        while self._table[self.hash_function(index)] and counter < self._size:
            index = index + 1 % self._size
            counter += 1

        self._table[self.hash_function(index)] = key

    def _get(self, key):
        counter = 0
        index = key
        while self._table[self.hash_function(index)] != key and counter < self._size:
            index = index + 1 % self._size
            counter += 1
        return key, index

    def get(self, key):
        return self._get(key)[0]

    def remove(self, key):
        index = self._get(key)[1]
        self._table[self.hash_function(index)] = None

    def exists(self, key):
        index = key
        counter = 0
        while self._table[self.hash_function(index)] and counter < self._size:
            index = index + 1 % self._size
            counter += 1
        return self._table[self.hash_function(key)] == key
