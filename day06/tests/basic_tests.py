import unittest

from moveit import MoveIt

class Testing(unittest.TestCase):
    def test_single_race_01(self):
        max_time = 7
        distance_to_beat = 9
        number_of_possible_moves = 4

        moveit = MoveIt()
        is_value = moveit.get_possible_moves_for_game(max_time, distance_to_beat)

        self.assertEqual(number_of_possible_moves, is_value)

    def test_single_race_02(self):
        max_time = 15
        distance_to_beat = 40
        number_of_possible_moves = 8

        moveit = MoveIt()
        is_value = moveit.get_possible_moves_for_game(max_time, distance_to_beat)

        self.assertEqual(number_of_possible_moves, is_value)

    def test_single_race_03(self):
        max_time = 30
        distance_to_beat = 200
        number_of_possible_moves = 9

        moveit = MoveIt()
        is_value = moveit.get_possible_moves_for_game(max_time, distance_to_beat)

        self.assertEqual(number_of_possible_moves, is_value)

if __name__ == '__main__':
    unittest.main()
