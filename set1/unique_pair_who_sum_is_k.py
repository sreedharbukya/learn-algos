"""

for given list of integers which integers, find the unique pair which has sum equal to k.


for an exmaple:

Input array = [1, 3,4,2,5,6], sum = 8

(5,3) and (3,5) are treated as unique pair.

unique pairs = [(5,3), (6,2)]


This is the problem, which appeared in my three interviews in last one year.

"""


def find_unique_pair_whose_sum(input_list, sum):
    if len(input_list) < 0:
        return

    if len(input_list) == 1:
        return
    unique_pairs = []

    input_list.sort()
    for index, value in enumerate(input_list):
        for index2, value2 in enumerate(input_list[index + 1:]):
            if (value + value2) == sum:
                unique_pairs.append([value, value2])

    return unique_pairs, len(unique_pairs)
