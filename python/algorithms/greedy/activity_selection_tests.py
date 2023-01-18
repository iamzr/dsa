import pytest

from python.algorithms.greedy.activity_selection_problem import activity_selection

tests = [([10, 12, 20], [20, 25, 30], [0, 2])]


@pytest.mark.parametrize("start, finish, expected_result", tests)
def test_activity_selection(start, finish, expected_result):
    result = activity_selection(start, finish)

    assert result == expected_result
