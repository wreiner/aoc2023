import re

class ScratchCards():
    # def __init__(self):
    #     self.cards = {}
    #     self.winning_numbers = {}

    def parse_card(self, line):
        win = 0
        winning_numbers = {}

        card_parts_arr = re.match("Card\s+(\d+):\s([0-9\s]+)\s\|\s([0-9\s]+)$", line)
        if not card_parts_arr:
            print(f"line {line} not a valid card")
            return -1

        card_num = card_parts_arr.group(1)
        card_winning_numbers_arr = card_parts_arr.group(2).split(" ")
        for winning_number in card_winning_numbers_arr:
            if winning_number.isdigit():
                winning_numbers[winning_number] = 1

        card_drawn_numbers_arr = card_parts_arr.group(3).split(" ")
        for drawn_number in card_drawn_numbers_arr:
            if drawn_number.isdigit() and drawn_number in winning_numbers:
                # print(f"number {drawn_number} is a winning number")
                if win == 0:
                    win = 1
                else:
                    win *= 2

        # print(f"card {card_num} has win of {win}")
        return win

    def sum_winnings(self, filename):
        sum = 0
        with open(filename) as f:
            for line in f:
                sum += self.parse_card(line.rstrip('\n'))
        return sum
