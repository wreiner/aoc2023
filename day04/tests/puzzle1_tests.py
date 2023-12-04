import unittest

from scratchcards import ScratchCards

class Testing(unittest.TestCase):
    def test_sum_of_winnings_test_input(self):
        filename = "inputs/puzzle1-test-input"
        should_value = 13

        scratchcards = ScratchCards()
        is_value = scratchcards.sum_winnings(filename)

        self.assertEqual(should_value, is_value)

    def test_sum_of_winnings_complete_input(self):
        filename = "inputs/puzzle1-complete-input"
        should_value = 24706

        scratchcards = ScratchCards()
        is_value = scratchcards.sum_winnings(filename)

        self.assertEqual(should_value, is_value)

if __name__ == '__main__':
    unittest.main()
