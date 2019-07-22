from unittest import TestCase

from set1.unique_pair_who_sum_is_k import find_unique_pair_whose_sum


class TestFind_unique_pair_whose_sum(TestCase):
    def test_find_unique_pair_whose_sum(self):
        input_1 = [1, 2, 3, 4, 5, 6, 7, 1]
        sum = 10
        actual_result, count = find_unique_pair_whose_sum(input_1, sum)
        self.assertEqual(actual_result, [[3, 7], [4, 6]])
        self.assertEqual(count, 2)