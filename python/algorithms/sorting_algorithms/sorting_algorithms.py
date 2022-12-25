from typing import List


def merge_sort(data: List[int]) -> List[int] | None:
    """
    Merge sort

    Average case: n log(n)
    Best case: n log(n)
    Worst case: n log(n)
    Memory: n
    Stable: Yes

    @param data: list to be sorted
    @return: sorted list
    """
    length_of_data = len(data)
    if length_of_data <= 1:
        return

    middle_position = length_of_data // 2

    left_list = data[:middle_position]
    right_list = data[middle_position:]

    # Sort the first half
    merge_sort(left_list)

    # Sort the second half
    merge_sort(right_list)

    # This code gets executed once the array has been sliced into length 1 lists
    i = j = k = 0

    # Copy data to temp array
    while i < len(left_list) and j < len(right_list):
        if left_list[i] <= right_list[j]:
            data[k] = left_list[i]
            i += 1
        else:
            data[k] = right_list[j]
            j += 1
        k += 1

    # If you've run out of right elements, add left list elements to the end
    while i < len(left_list):
        data[k] = left_list[i]
        i += 1
        k += 1

    # If you've run out of left elements, add right elements to the end
    while j < len(right_list):
        data[k] = right_list[j]
        j += 1
        k += 1


def _partition(list, low, high):
    # pivot - element to be place into the correct position
    pivot = list[high]

    # index of smaller element and indicates the correct position of the pivot found so far
    i = low - 1

    for j in range(low, high):
        if list[j] <= pivot:
            i += 1
            list[i], list[j] = list[j], list[i]

    list[i + 1], list[high] = list[high], list[i + 1]

    return i + 1


def _quick_sort_recursive(list, low, high):
    if low < high:
        partition = _partition(list, low, high)

        _quick_sort_recursive(list, low, partition - 1)
        _quick_sort_recursive(list, partition + 1, high)


def quick_sort(data: List[int]) -> List[int]:
    """
    Quick sort

    Best case: n log(n)
    Average case: n log(n)
    Worst case: n^2
    Memory: log(n)
    Stable: No

    @param data: list to be sorted
    @return: sorted list
    """

    low = 0
    high = len(data) - 1

    _quick_sort_recursive(data, low, high)
