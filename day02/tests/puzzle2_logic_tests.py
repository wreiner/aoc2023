import unittest

from cubepossible import CubePossible

class Testing(unittest.TestCase):
    def test_power_of_a_game(self):
        line = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
        should_value = 48

        cubepossible = CubePossible()
        is_value =  cubepossible.get_power_of_a_game(line)

        self.assertEqual(should_value, is_value)

    def test_powersum_of_test_game_file(self):
        filename = "inputs/puzzle2-test-input"
        should_value = 2286

        cubepossible = CubePossible()
        is_value = cubepossible.powersum_of_games_from_file(filename)

        self.assertEqual(should_value, is_value)

    def test_powersum_of_complete_game_file(self):
        filename = "inputs/puzzle2-complete-input"
        should_value = 63700

        cubepossible = CubePossible()
        is_value = cubepossible.powersum_of_games_from_file(filename)

        self.assertEqual(should_value, is_value)

if __name__ == '__main__':
    unittest.main()
