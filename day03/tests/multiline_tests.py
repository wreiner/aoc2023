import unittest

from enginetrouble import EngineTrouble

class Testing(unittest.TestCase):
    def test_single_touching_above_adjacent(self):
        line1 = "..#..."
        line2 = "..38.."
        should_value = 38

        enginetrouble = EngineTrouble()
        enginetrouble.parse_line(0, line1)
        enginetrouble.parse_line(1, line2)
        is_value = enginetrouble.get_vertical_adjacent()

        self.assertEqual(should_value, is_value)

    def test_single_touching_below_adjacent(self):
        line1 = "..39.."
        line2 = "...#.."
        should_value = 39

        enginetrouble = EngineTrouble()
        enginetrouble.parse_line(0, line1)
        enginetrouble.parse_line(1, line2)
        is_value = enginetrouble.get_vertical_adjacent()

        self.assertEqual(should_value, is_value)

    def test_single_touching_vertical_below_adjacent(self):
        line1 = "..40.."
        line2 = ".*...."
        should_value = 40

        enginetrouble = EngineTrouble()
        enginetrouble.parse_line(0, line1)
        enginetrouble.parse_line(1, line2)
        is_value = enginetrouble.get_vertical_adjacent()

        self.assertEqual(should_value, is_value)

    def test_single_touching_vertical_above_adjacent(self):
        line2 = "....*."
        line1 = "..43.."
        should_value = 43

        enginetrouble = EngineTrouble()
        enginetrouble.parse_line(0, line1)
        enginetrouble.parse_line(1, line2)
        is_value = enginetrouble.get_vertical_adjacent()

        self.assertEqual(should_value, is_value)

if __name__ == '__main__':
    unittest.main()
