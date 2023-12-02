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
        line = "Game 1: 15 red, 2 green, 3 blue"
        should_value = False

        cubepossible = CubePossible()
        is_value =  cubepossible.is_game_valid(line)

        self.assertEqual(should_value, is_value)


if __name__ == '__main__':
    unittest.main()
