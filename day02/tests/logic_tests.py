import unittest

from cubepossible import CubePossible

class Testing(unittest.TestCase):
    def test_valid_game(self):
        line = "Game 1: 1 red, 2 green, 3 blue"
        should_value = True

        cubepossible = CubePossible()
        is_value =  cubepossible.is_game_valid(line)

        self.assertEqual(should_value, is_value)

    def test_invalid_game(self):
        line = "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"
        should_value = False

        cubepossible = CubePossible()
        is_value = cubepossible.is_game_valid(line)

        self.assertEqual(should_value, is_value)

    def test_sum_of_valid_games(self):
        filename = "inputs/puzzle1-test-input"
        should_value = 8

        cubepossible = CubePossible()
        is_value = cubepossible.sum_of_games_from_file(filename)

        self.assertEqual(should_value, is_value)

if __name__ == '__main__':
    unittest.main()
