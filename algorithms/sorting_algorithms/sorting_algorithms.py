from typing import List


def merge_sort(data: List[int]) -> List[int] | None:
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

    while i < len(left_list):
        data[k] = left_list[i]
        i += 1
        k += 1

    while j < len(right_list):
        data[k] = right_list[j]
        j += 1
        k += 1
