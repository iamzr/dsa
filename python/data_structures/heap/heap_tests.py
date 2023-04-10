from data_structures.heap.heap import MaxHeap


def test():
    values = [3, 10, 12, 8, 2, 14]
    h = MaxHeap(15)

    for value in values:
        h.insert(value)

    assert h.size == 6
    assert h.get_max() == 14

    h.remove(2)

    assert h.size == 5

    h.insert(15)
    h.insert(5)

    assert h.size == 7
    assert h.get_max() == 15
