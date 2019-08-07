"""
https://www.geeksforgeeks.org/find-minimum-number-of-coins-that-make-a-change/

Given a value V, if we want to make change for V cents, and we have infinite supply of
each of C = { C1, C2, .. , Cm} valued coins, what is the minimum number of coins to make the change?

"""


def find_minimum_number_of_coins(coins_list, sum):
    if len(coins_list) <= 0:
        return
    if sum <= 0:
        return
    sorted(coins_list)

    print(coins_list)
    count = 0

    return count