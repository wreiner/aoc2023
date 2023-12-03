import unittest

from enginetrouble import EngineTrouble

class Testing(unittest.TestCase):
    def test_with_testinput(self):
        filename = "inputs/part1-test-input"
        should_value = 4361

        enginetrouble = EngineTrouble()
        enginetrouble.parse_engine_file(filename)
        is_value = enginetrouble.sum_adjacent()

        self.assertEqual(should_value, is_value)

    def test_with_complete_input(self):
        filename = "inputs/part1-complete-input"
        should_value = 527364

        enginetrouble = EngineTrouble()
        enginetrouble.parse_engine_file(filename)
        is_value = enginetrouble.sum_adjacent()

        self.assertEqual(should_value, is_value)

if __name__ == '__main__':
    unittest.main()
