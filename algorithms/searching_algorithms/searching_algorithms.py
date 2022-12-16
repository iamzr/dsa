def linear_search(array, item):
    """
    Uses linear search to find the item in the array

    Time complexity: O(n)
    Auxillary space: O(1)

    array: unsorted array
    item: item you're searching for
    """
    if array == []:
        raise ValueError("Array is empty")

    for k, v in enumerate(array):
        if v == item:
            return k

    raise ValueError(f"{item} not found in array")


def binary_search(sorted_array, item):
    """
    Applies the bineary search algorithm
    """
    i = 0
    n = len(sorted_array)
    while i < n:
        element = sorted_array[i]

        if element == item:
            return i
        elif element < item:
            sorted_array = sorted_array[0:i]
        elif element > item:
            sorted_array = sorted_array[i + 1:-1]

        i += 1


def binary_search_iterative(sorted_array, item):
    """
    Applied binary search to find item in a sorted array

    Time complexity: O(log(n))
    Auxiliary space: O(log(n))
    """
    if not sorted_array:
        raise ValueError("Array is empty")

    n = len(sorted_array)

    low = 0
    high = n

    while low != high:
        current_middle_index = (low + high) // 2

        current_middle_value = sorted_array[current_middle_index]

        if current_middle_value == item:
            return current_middle_index
        elif item > current_middle_value:
            low = current_middle_index + 1
        else:
            high = current_middle_index - 1

    raise ValueError(f"{item} not found in array.")


def interpolation_search(array, item):
    """
    Applies interpolation search to find item in array

    Time complexity: O(log_2 (log_2 (n)))
    Auxillary space: O(1)

    array: uniformly distributed array
    item: item you're searching for
    """
    if not array:
        raise ValueError("Array is empty")
    n = len(array)

    low = 0
    high = n

    while low <= high and array[low] <= item <= array[high]:
        current_position = low + (item - array[low]) * (high - low) / (array[high] - array[low])
        current_value = array[current_position]

        if current_value == item:
            return current_position
        elif item < current_value:
            low = current_position + 1
        else:
            high = current_position - 1

    raise ValueError(f"{item} not found in array.")
