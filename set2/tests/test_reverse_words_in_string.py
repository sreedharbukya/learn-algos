from unittest import TestCase

from set2.reverse_words_in_sentense import reverse_words_in_string


class Test_Reverse_Words_in_String(TestCase):

    def test_empty_input(self):
        expected = None
        output = reverse_words_in_string(None)

        self.assertEqual(output, expected)

    def test_for_single_character_input(self):
        expected = "a"
        output = reverse_words_in_string("a")

        self.assertEqual(output, expected)

    def test_for_two_character_with_spaces(self):
        expected = "a b"
        output = "a b"

        self.assertEqual(output, expected)

    def test_with_multiple_words_in_string(self):
        expected = "cba gfe"
        output = reverse_words_in_string("abc efg")

        self.assertEqual(output, expected)

    def test_with_multiple_words_with_special_characters(self):
        expected = "a_bc e_gf"
        output = reverse_words_in_string("cb_a fg_e")

        self.assertEqual(output, expected)


