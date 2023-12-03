import unittest

from enginetrouble import EngineTrouble

class Testing(unittest.TestCase):
    def test_single_front_adjacent(self):
        line = "..#38.."
        should_value = 38

        enginetrouble = EngineTrouble()
        enginetrouble.parse_line(0, line)
        is_value = enginetrouble.get_front_adjacent()

        self.assertEqual(should_value, is_value)

    def test_single_back_adjacent(self):
        line = "..39#.."
        should_value = 39

        enginetrouble = EngineTrouble()
        enginetrouble.parse_line(0, line)
        is_value = enginetrouble.get_back_adjacent()

        self.assertEqual(should_value, is_value)

    def test_multi_front_adjacent(self):
        line = "..#38..#4"
        should_value = 42

        enginetrouble2 = EngineTrouble()
        enginetrouble2.parse_line(0, line)
        is_value = enginetrouble2.get_front_adjacent()

        self.assertEqual(should_value, is_value)

    def test_single_back_adjacent(self):
        line = "..39#...."
        should_value = 39

        enginetrouble = EngineTrouble()
        enginetrouble.parse_line(0, line)
        is_value =  enginetrouble.get_back_adjacent()

        self.assertEqual(should_value, is_value)

    def test_multi_back_adjacent(self):
        line = "..39#...4*"
        should_value = 43

        enginetrouble = EngineTrouble()
        enginetrouble.parse_line(0, line)
        is_value =  enginetrouble.get_back_adjacent()

        self.assertEqual(should_value, is_value)

if __name__ == '__main__':
    unittest.main()
