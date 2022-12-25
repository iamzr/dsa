import pytest

from algorithms.searching_algorithms.searching_algorithms import binary_search_iterative, linear_search, \
    interpolation_search

search_algorithms = [linear_search, binary_search_iterative, interpolation_search]

@pytest.mark.parametrize("algorithm", search_algorithms)
def test_searching_algorithm_given_valid_input_returns_correct_value(algorithm):
    array = [1, 3, 4, 5, 6]
    element = 4
    expected_result = 2

    result = algorithm(array, element)

    assert result == expected_result


@pytest.mark.parametrize("algorithm", search_algorithms)
def test_searching_algorithm_given_empty_array_raises_value_error(algorithm):
    array = []
    element = 1

    with pytest.raises(ValueError) as e:
        algorithm(array, element)

    assert "Array is empty" in e.exconly()

@pytest.mark.parametrize("algorithm", search_algorithms)
def test_searching_algorithm_given_item_not_in_array_returns_value_error(algorithm):
    array = [1,2,3,4,5,6,7,8]
    element = 9

    with pytest.raises(ValueError) as e:
        algorithm(array, element)

    assert f"{element} not found in array" in e.exconly()

