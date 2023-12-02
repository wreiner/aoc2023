import unittest

from cubepossible import CubePossible

class Testing(unittest.TestCase):
    def test_parse_single_digit_gameid_number(self):
        line = "Game 1: 1 red, 2 green, 3 blue"
        should_value = 1

        cubepossible = CubePossible()
        is_value =  cubepossible.get_game_id(line)

        self.assertEqual(should_value, is_value)

    def test_parse_double_digit_gameid_number(self):
        line = "Game 12: 1 red, 2 green, 3 blue"
        should_value = 12

        cubepossible = CubePossible()
        is_value =  cubepossible.get_game_id(line)

        self.assertEqual(should_value, is_value)

if __name__ == '__main__':
    unittest.main()
