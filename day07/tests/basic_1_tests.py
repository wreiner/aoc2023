import unittest

from camelcards import CamelCards

class Testing(unittest.TestCase):
    def test_classification_1(self):
        line = "AAAAA"
        should_value = 6

        camelcards = CamelCards()
        is_value = camelcards.classify_hand([*line])

        self.assertEqual(should_value, is_value)

    def test_classification_2(self):
        line = "AA8AA"
        should_value = 5

        camelcards = CamelCards()
        is_value = camelcards.classify_hand([*line])

        self.assertEqual(should_value, is_value)

    def test_classification_3(self):
        line = "23332"
        should_value = 4

        camelcards = CamelCards()
        is_value = camelcards.classify_hand([*line])

        self.assertEqual(should_value, is_value)

    def test_test_input(self):
        filename = "inputs/complete-input"
        should_value = 250951660

        camelcards = CamelCards()
        is_value = camelcards.parse_file(filename)

        self.assertEqual(should_value, is_value)

if __name__ == '__main__':
    unittest.main()
