from unittest import TestCase

from set1.binary_search import binary_search


class Test_Binary_search(TestCase):

    def test_for_empty_array(self):
        data_list = []
        search_item = 10

        expected_result = False

        actual = binary_search(data_list=data_list, search_item=search_item)

        self.assertEqual(expected_result, actual)

    def test_for_binary_search_case1(self):
        data_list = [1, 2, 3, 4, 7, 11, 44, 89, 109, 111]
        search_item = 10

        expected_result = False

        actual = binary_search(data_list=data_list, search_item=search_item)

        self.assertEqual(expected_result, actual)

    def test_for_binary_for_first_item(self):
        data_list = [1, 2, 3, 4, 7, 11, 44, 89, 109, 121]
        search_item = 1

        expected_result = True

        actual = binary_search(data_list=data_list, search_item=search_item)

        self.assertEqual(expected_result, actual)

    def test_for_binary_for_last_item(self):
        data_list = [1, 2, 3, 4, 7, 11, 44, 89, 109, 121]
        search_item = 121

        expected_result = True

        actual = binary_search(data_list=data_list, search_item=search_item)

        self.assertEqual(expected_result, actual)
