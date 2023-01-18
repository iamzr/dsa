from typing import List

from numpy import inf


def activity_selection(start: List[int], finish: List[int]):
    """
    Finds the maximum number of activities, given that the acitivies in arrays are sorted by finish time
    @param start: list of start times
    @param finish: sorted list of finish times
    @return: list of selected activities
    """
    n = len(finish)
    jobs = []

    i = 0
    jobs.append(i)

    for j in range(1, n):
        if start[j] >= finish[i]:
            jobs.append(j)
            i = j

    return jobs