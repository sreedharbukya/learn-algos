from unittest import TestCase

from set1.unique_pair_who_sum_is_k import find_unique_pair_whose_sum


class Test_Find_unique_pair_whose_sum(TestCase):

    def test_find_unique_pair_whose_sum(self):
        input_1 = [1, 2, 3, 4, 5, 6, 7]
        sum = 10
        actual_result, count = find_unique_pair_whose_sum(input_1, sum)
        self.assertEqual([[3, 7], [4, 6]], actual_result)
        self.assertEqual(count, 2)

    def test_find_unique_for_duplicate_values(self):
        input_1 = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
        sum = 10
        actual_result, count = find_unique_pair_whose_sum(input_1, sum)

        self.assertEqual([[3, 7], [4, 6]], actual_result)
        self.assertEqual(count, 2)

    def test_to_find_empty_input(self):
        input_1 = []
        sum = 1
        actual_result, count = find_unique_pair_whose_sum(input_1, sum)

        self.assertEqual([], actual_result)
        self.assertEqual(count, 0)

    def test_to_find_negative_values_input(self):
        input_1 = [1, -2, 12, 3, 4, 4, 5, 6, 6, 7]
        sum = 10
        actual_result, count = find_unique_pair_whose_sum(input_1, sum)

        self.assertEqual([[-2, 12], [3, 7], [4, 6]], actual_result)
        self.assertEqual(count, 2)

