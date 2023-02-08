import pytest

from python.algorithms.divide_and_conquer.strassens_algorithm import multiply_naive

algorithms = [multiply_naive]

testcases = [([[2]], [[2]], [[4]]),
             ([[1, 2], [3, 4]], [[5, 6], [7, 8]], [[19, 22], [43, 50]])]


@pytest.mark.parametrize("A, B, C", testcases)
@pytest.mark.parametrize("algorithm", algorithms)
def test_multiply_algorithms(algorithm, A, B, C):
    answer = algorithm(A, B)

    assert answer == C
