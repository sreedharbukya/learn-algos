from math import floor


def binary_search(data_list, search_item):
    list_size = len(data_list)

    if list_size < 1:
        return False

    pointer1 = 0
    pointer2 = list_size - 1

    while pointer1 <= pointer2:
        mid = int(floor(pointer1 + (pointer2 - pointer1) / 2))
        if data_list[mid] == search_item:
            return True

        elif data_list[mid] < search_item:
            pointer1 = mid + 1
        else:
            pointer2 = mid - 1

    return False

