import unittest

from scratchcards import ScratchCards

class Testing(unittest.TestCase):
    def test_single_card_with_winnings(self):
        line = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
        should_value = 8

        scratchcards = ScratchCards()
        is_value = scratchcards.parse_card(line)

        self.assertEqual(should_value, is_value)

    def test_sum_of_winnings_test_input(self):
        filename = "inputs/puzzle1-test-input"
        should_value = 13

        scratchcards = ScratchCards()
        is_value = scratchcards.sum_winnings(filename)

        self.assertEqual(should_value, is_value)

if __name__ == '__main__':
    unittest.main()
