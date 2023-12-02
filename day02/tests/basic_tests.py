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

    def test_extract_singe_set(self):
        line = "Game 1: 1 red, 2 green, 3 blue"
        should_value = ["1red,2green,3blue"]

        cubepossible = CubePossible()
        sets_array =  cubepossible.extract_sets(line)

        self.assertCountEqual(should_value, sets_array)
        self.assertListEqual(should_value, sets_array)

    def test_extract_multiple_sets(self):
        line = "Game 1: 1 red, 2 green, 3 blue; 4 green, 5 red, 6 blue"
        should_value = ["1red,2green,3blue","4green,5red,6blue"]

        cubepossible = CubePossible()
        sets_array =  cubepossible.extract_sets(line)

        self.assertCountEqual(should_value, sets_array)
        self.assertListEqual(should_value, sets_array)

if __name__ == '__main__':
    unittest.main()
