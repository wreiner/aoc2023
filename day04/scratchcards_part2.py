import re
from pprint import pprint

class ScratchCards():
    def __init__(self):
        self.initial_cards = {}
        self.won_cards = {}

    def parse_card(self, line):
        win = 0
        card_obj = {}

        line = re.sub("\s+", " ", line)

        card_parts_arr = re.match("Card\s+(\d+):\s([0-9\s]+)\s\|\s([0-9\s]+)$", line)
        if not card_parts_arr:
            print(f"line {line} not a valid card")
            return -1

        card_obj["card_id"] = card_parts_arr.group(1)
        self.won_cards[card_obj["card_id"]] = 1
        card_obj["winning_numbers"] = {}

        card_winning_numbers_arr = card_parts_arr.group(2).split(" ")
        for winning_number in card_winning_numbers_arr:
            if winning_number.isdigit():
                card_obj["winning_numbers"][winning_number] = 1

        card_drawn_numbers_arr = card_parts_arr.group(3).split(" ")
        for drawn_number in card_drawn_numbers_arr:
            if drawn_number.isdigit() and drawn_number in card_obj["winning_numbers"]:
                win += 1

        card_obj["number_to_draw"] = win
        return card_obj

    def draw_card(self, card_to_draw):
        # print(f"in draw_card for card {card_to_draw}")

        card_obj = self.initial_cards[card_to_draw]

        # print(f"card data: {card_obj}")
        # print(f"must draw {card_obj['number_to_draw']} cards")

        if card_obj["number_to_draw"] == 0:
            # print(f"----------- reached card {card_to_draw}, no more draws")
            return

        for i in range(int(card_to_draw) + 1, int(card_to_draw) + card_obj["number_to_draw"] + 1):
            # print(f"rec: will draw card {i}")
            self.won_cards[str(i)] += 1
            self.draw_card(str(i))

    def parse_file(self, filename):
        with open(filename) as f:
            for line in f:
                card_obj = self.parse_card(line)
                self.initial_cards[card_obj["card_id"]] = card_obj

        # pprint(self.initial_cards)
        # pprint(self.won_cards)

        for card in self.initial_cards:
            self.draw_card(str(card))

        # pprint(self.won_cards)

        return sum(self.won_cards.values())
