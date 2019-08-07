from unittest import TestCase

from sorting.merge_sort import merge_sort


class Test_MergeSort(TestCase):

    def test_for_empty(self):
        expected = None
        output = merge_sort(None)
        self.assertEqual(output, expected)

    def test_for_single_input(self):
        expected = [1]
        merge_sort([1])
        self.assertEqual([1], expected)

    def test_for_odd_list_size_input(self):
        expected = [1, 2, 3, 4, 5]
        data_list = [4, 2, 5, 1, 3]
        merge_sort(data_list)
        self.assertEqual(data_list, expected)

    def test_for_event_list_size_input(self):
        expected = [1, 2, 3, 4, 5, 6]
        data_list = [4, 2, 5, 1, 6, 3]
        merge_sort(data_list)
        self.assertEqual(data_list, expected)

    def test_for_duplicate_values_in_input(self):
        expected = [1, 3, 3, 4, 5, 6]
        data_list = [4, 3, 5, 1, 6, 3]
        merge_sort(data_list)
        self.assertEqual(data_list, expected)
