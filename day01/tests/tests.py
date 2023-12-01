import unittest

from linecounter import LineCounter

class Testing(unittest.TestCase):
    def test_line_number(self):
        line = "1lala2"
        should_value = 12

        linecounter = LineCounter()
        is_value =  linecounter.number_of_line(line)

        self.assertEqual(should_value, is_value)

    def test_line_number_word(self):
        line = "1lala2"
        should_value = 12

        linecounter = LineCounter()
        is_value =  linecounter.parse_line_for_number_word(line)

        self.assertEqual(should_value, is_value)

    def test_line_number_words(self):
        line = "twone"
        should_value = 21

        linecounter = LineCounter()
        is_value =  linecounter.parse_line_for_number_word(line)

        self.assertEqual(should_value, is_value)

    def test_test_input_p1(self):
        filename = "inputs/puzzle1-test-input"
        should_numbers = [12, 38, 15, 77]

        linecounter = LineCounter()
        is_numbers = linecounter.get_numbers_from_file(filename)
        self.assertCountEqual(should_numbers, is_numbers)
        self.assertListEqual(should_numbers, is_numbers)

    def test_test_input_sum_p1(self):
        filename = "inputs/puzzle1-test-input"
        should_sum = 142

        linecounter = LineCounter()
        numbers = linecounter.get_numbers_from_file(filename)
        is_sum = linecounter.sum_of_numbers(numbers)
        self.assertEqual(should_sum, is_sum)

    def test_complete_input_p1(self):
        filename = "inputs/puzzle1-complete-input"
        should_sum = 53974

        linecounter = LineCounter()
        numbers = linecounter.get_numbers_from_file(filename)
        is_sum = linecounter.sum_of_numbers(numbers)
        self.assertEqual(should_sum, is_sum)

    def test_test_input_p2(self):
        filename = "inputs/puzzle2-test-input"
        should_numbers = [29, 83, 13, 24, 42, 14, 76]
        #. Adding these together produces 281.

        linecounter = LineCounter()
        is_numbers = linecounter.get_numbers_from_file_words(filename)
        self.assertCountEqual(should_numbers, is_numbers)
        self.assertListEqual(should_numbers, is_numbers)

    def test_test_input_sum_p2(self):
        filename = "inputs/puzzle2-test-input"
        should_sum = 281

        linecounter = LineCounter()
        numbers = linecounter.get_numbers_from_file_words(filename)
        is_sum = linecounter.sum_of_numbers(numbers)
        self.assertEqual(should_sum, is_sum)

    def test_complete_input_p2(self):
        filename = "inputs/puzzle2-complete-input"
        should_sum = 52840

        linecounter = LineCounter()
        numbers = linecounter.get_numbers_from_file_words(filename)
        is_sum = linecounter.sum_of_numbers(numbers)
        self.assertEqual(should_sum, is_sum)

if __name__ == '__main__':
    unittest.main()
