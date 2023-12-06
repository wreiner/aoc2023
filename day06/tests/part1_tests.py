import unittest

from moveit import MoveIt

class Testing(unittest.TestCase):
    def test_test_input(self):
        filename = "inputs/test-input"
        number_of_possible_moves = 288

        moveit = MoveIt()
        is_value = moveit.part_one_get_product_of_possible_moves(filename)

        self.assertEqual(number_of_possible_moves, is_value)

    def test_complete_input(self):
        filename = "inputs/complete-input"
        number_of_possible_moves = 2612736

        moveit = MoveIt()
        is_value = moveit.part_one_get_product_of_possible_moves(filename)

        self.assertEqual(number_of_possible_moves, is_value)

if __name__ == '__main__':
    unittest.main()
