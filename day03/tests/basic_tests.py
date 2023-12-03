import unittest

from enginetrouble import EngineTrouble

class Testing(unittest.TestCase):

    def test_single_front_adjacent(self):
        line = "..#38.."
        should_value = 38

        enginetrouble = EngineTrouble()
        enginetrouble.parse_line(0, line)
        is_value =  enginetrouble.get_front_adjacent()

        self.assertEqual(should_value, is_value)

if __name__ == '__main__':
    unittest.main()
