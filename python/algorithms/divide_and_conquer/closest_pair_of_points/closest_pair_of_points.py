import math
from typing import List

from python.algorithms.divide_and_conquer.closest_pair_of_points.Point import Point


def _distance(point_1: Point, point_2: Point) -> float:
    """
    Finds the distance between two 2D points.

    @param point_1: First point
    @param point_2: Second point
    @return: minimum distance
    """
    return math.sqrt((point_1.x - point_2.x) ** 2 +
                     (point_1.y - point_2.y) ** 2)


def brute_force(points: List[Point]) -> float:
    """
    Brute force approach to finding the closest pair of points in an array of points.
    Just loop over the array and find the distance between each of the points and then find the minimum.

    @param points: List of points
    @param n: Length of points list
    @return: minimum distance
    """
    n = len(points)

    minimum_value = float("inf")
    for i in range(n):
        for j in range(i + 1, n):
            distance = _distance(points[i], points[j])
            if distance < minimum_value:
                minimum_value = distance

    return minimum_value


def closest_pair_of_points(points: List[Point]) -> float:
    """
    Finds the closest pair of points in the array

    @param points: Array of 2D points (x,y)
    @return: smallest distance between two points in the given array
    """

    n = len(points)
    points.sort(key=lambda point: point.x)

    return _closest_utility(points, n)


def _closest_in_strip(points: List[Point], minimum_value: float):
    n = len(points)
    points.sort(key=lambda point: point.y)

    for i in range(n):
        j = i + 1

        while j < n and (points[j].y - points[i].y < minimum_value):
            minimum_value = _distance(points[i], points[j])
            j += 1

    return minimum_value


def _closest_utility(points: List[Point], n: int):
    if n <= 3:
        return brute_force(points)

    midpoint_index = n // 2
    midpoint = points[midpoint_index]

    left_array = points[:midpoint_index]
    right_array = points[midpoint_index:]

    left_array_minimum_distance = _closest_utility(left_array, midpoint_index)
    right_array_minimum_distance = _closest_utility(right_array, n - midpoint_index)

    minimum_distance = min(left_array_minimum_distance, right_array_minimum_distance)

    strip = []
    for point in points:
        if abs(midpoint.x - point.x) < minimum_distance:
            strip.append(point)

    return min(minimum_distance, _closest_in_strip(strip, minimum_distance))
