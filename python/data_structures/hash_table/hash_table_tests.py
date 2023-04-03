import pytest

from data_structures.hash_table.hash_table import HashTableWithTrivialMapping, HashTableWithModuloMapping, \
    HashTableWithModuloMappingLinearProbing


def test_hash_table_with_trivial_mapping():
    values = [2, 3, 4, 13, 15, 12, 16]
    n = 17

    hash_table = HashTableWithTrivialMapping(n)

    for value in values:
        hash_table.add(value)

    for value in values:
        assert hash_table.get(value) == value
        assert hash_table.exists(value) == True

    hash_table.remove(13)

    assert hash_table.exists(13) == False

def test_hash_table_with_modulo_mapping():
    values = [2, 3, 4, 13, 15, 12, 16]
    n = 17

    hash_table = HashTableWithModuloMapping(n)

    for value in values:
        hash_table.add(value)

    for value in values:
        assert hash_table.get(value) == value
        assert hash_table.exists(value) == True

    print(hash_table._table)

    hash_table.remove(13)

    assert hash_table.exists(13) == False

def test_hash_table_with_modulo_mapping_with_big_numbers():
    values = [2, 3, 4, 13, 15, 12, 16, 34, 55]
    n = 10

    hash_table = HashTableWithModuloMapping(n)

    for value in values:
        hash_table.add(value)

    with pytest.raises(AssertionError):
        assert hash_table.exists(2)

    print(hash_table._table)

def test_hash_table_with_modulo_mapping_linear_probing():
    values = [2, 3, 4, 13, 15, 12, 16]
    n = 10

    hash_table = HashTableWithModuloMappingLinearProbing(n)

    for value in values:
        hash_table.add(value)

    print(hash_table._table)

    for value in values:
        assert hash_table.get(value) == value
        assert hash_table.exists(value) == True

    print(hash_table._table)

    hash_table.remove(13)

    assert hash_table.exists(13) == False
