import pytest

from algorithms.sorting_algorithms.sorting_algorithms import merge_sort, quick_sort

sorting_algorithms = [
    merge_sort,
    quick_sort
]


simple_list_with_no_repeats = [63, 46, 83, 43, 76, 50, 36, 62, 96, 33, 24, 35, 10, 15, 40, 57, 67, 78, 94, 84, 53, 48, 8, 58, 45, 2, 88, 93, 79, 73, 90, 28, 92, 91, 80, 5, 38, 12, 81, 61, 20, 74, 17, 34, 75, 27, 77, 6, 95, 71, 64, 59, 7, 86, 97, 41, 69, 9, 29, 66, 16, 4, 49, 98]

simple_list_with_repeats = [2, 3, 4, 5, 3, 4, 6, 5, 4, 3, 2, 5, 6, 7, 5, 4, 5, 6, 7, 6]

empty_list = []

list_with_one_item = [1]


@pytest.mark.parametrize("list",
                         [simple_list_with_no_repeats, simple_list_with_repeats, empty_list, list_with_one_item])
@pytest.mark.parametrize("algorithm", sorting_algorithms)
def test_sort_simple_list_returns_correct_list(algorithm, list):
    algorithm(list)

    assert list == sorted(list)
