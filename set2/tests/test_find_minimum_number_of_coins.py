from unittest import TestCase

from set2.miniumum_coins_required import find_minimum_number_of_coins


class TestFind_minimum_number_of_coins(TestCase):
    def test_find_minimum_number_of_coins(self):
        coins_list = [25, 10, 5]
        sum = 30
        expected_output = 2
        actual_output = find_minimum_number_of_coins(coins_list=coins_list, sum=sum)


        self.assertEqual(actual_output, expected_output)
