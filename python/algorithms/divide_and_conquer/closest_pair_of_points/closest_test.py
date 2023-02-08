import pytest

from python.algorithms.divide_and_conquer.closest_pair_of_points.Point import Point
from python.algorithms.divide_and_conquer.closest_pair_of_points.closest_pair_of_points import brute_force, \
    closest_pair_of_points

P = [Point(2, 3), Point(12, 30),
     Point(40, 50), Point(5, 1),
     Point(12, 10), Point(3, 4)]
ans = 1.414214

test_cases = [(P, 1.414214)]


@pytest.mark.parametrize("points, answer", test_cases)
@pytest.mark.parametrize("algorithm", [brute_force, closest_pair_of_points])
def test_algorithm(algorithm, points, answer):
    result = algorithm(points)

    assert round(result, 6) == answer
