import unittest

from growit import GrowIt

class Testing(unittest.TestCase):
    def test_get_location_with_test(self):
        filename = "inputs/part1-test-input"
        should_value = 35

        growit = GrowIt()
        is_value = growit.parse_file(filename)

        self.assertEqual(should_value, is_value)

    def test_get_location_with_winnings(self):
        filename = "inputs/part1-complete-input"
        should_value = 662197086

        growit = GrowIt()
        is_value = growit.parse_file(filename)

        self.assertEqual(should_value, is_value)

if __name__ == '__main__':
    unittest.main()
