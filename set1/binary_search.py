from math import floor


def binary_search(data_list, search_item):
    list_size = len(data_list)

    if list_size < 1:
        return False

    left = 0
    right = list_size - 1

    while left <= right:
        mid = int(floor(left + (right - left) / 2))
        if data_list[mid] == search_item:
            return True

        elif data_list[mid] < search_item:
            left = mid + 1
        else:
            right = mid - 1

    return False

