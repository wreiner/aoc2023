import unittest

from scratchcards_part2 import ScratchCards

class Testing(unittest.TestCase):
    def test_sum_of_cards_drawn_test_input(self):
        filename = "inputs/puzzle1-test-input"
        should_value = 30

        scratchcards = ScratchCards()
        is_value = scratchcards.parse_file(filename)

        self.assertEqual(should_value, is_value)

    def test_sum_of_cards_drawn_complete_input(self):
        filename = "inputs/puzzle1-complete-input"
        should_value = 13114317

        scratchcards = ScratchCards()
        is_value = scratchcards.parse_file(filename)

        self.assertEqual(should_value, is_value)

if __name__ == '__main__':
    unittest.main()
