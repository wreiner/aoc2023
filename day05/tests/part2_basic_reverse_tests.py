import unittest

from growit3 import GrowIt

class Testing(unittest.TestCase):
    # def test_get_location_with_test(self):
    #     map = [{'input': {'start': 56, 'end': 93}, 'output': {'start': 60, 'end': 97}}]
    #     seed = 57
    #     should_value = 61

    #     growit = GrowIt()
    #     is_value = growit.get_output_to_input(seed, map)
    #     self.assertEqual(should_value, is_value)

    # def test_get_location_with_testrev(self):
    #     map = [{'input': {'start': 56, 'end': 93}, 'output': {'start': 60, 'end': 97}}]
    #     seed = 61
    #     should_value = 57

    #     growit = GrowIt()
    #     is_value = growit.get_output_to_input_reverse(seed, map)
    #     self.assertEqual(should_value, is_value)

    # def test_get_location_with_test(self):
    #     filename = "inputs/part1-new-ci"
    #     should_value = 46

    #     growit = GrowIt()
    #     is_value = growit.parse_file(filename)

    #     self.assertEqual(should_value, is_value)

    def test_get_location_with_test(self):
        filename = "inputs/part1-new-ci"
        should_value = 52510809

        growit = GrowIt()
        is_value = growit.parse_file(filename)

        self.assertEqual(should_value, is_value)


if __name__ == '__main__':
    unittest.main()
