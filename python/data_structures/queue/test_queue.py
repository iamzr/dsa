import pytest

from python.data_structures.queue.queue_using_fixed_array import Queue


def test_dequeue_when_queue_empty():
    queue = Queue(10)

    with pytest.raises(IndexError) as e:
        queue.dequeue()

    assert "The queue is empty" in e.exconly()


def test_dequeue_give_non_empty_queue_removes_rear_element():
    queue = Queue(3)
    queue.enqueue(1)
    queue.enqueue(5)

    queue.dequeue()


def test_enqueue_when_queue_full():
    queue = Queue(1)
    queue._size = 1

    with pytest.raises(IndexError) as e:
        queue.enqueue(3)

    assert "The queue is full" in e.exconly()


def test_queue_pointers_are_correct():
    queue = Queue(30)

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    queue.dequeue()

    assert queue.front() == 20
    assert queue.rear() == 40


# TODO: split this test into several proper unit tests
def test_queue_pointers_are_cyclic():
    queue = Queue(3)

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.dequeue()

    assert queue.front() == 20
    assert queue.rear() == 30

    queue.enqueue(40)
    queue.dequeue()

    assert queue.front() == 30
    assert queue.rear() == 40

    queue.enqueue(50)
    queue.dequeue()
    queue.dequeue()

    assert queue.front() == 50
    assert queue.rear() == 50
