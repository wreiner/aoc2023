from collections import Counter
from pprint import pprint
import functools

class CamelCards():
    CARD_EXP_VALUES = {
        'A': 12,
        'K': 11,
        'Q': 10,
        'T': 9,
        '9': 8,
        '8': 7,
        '7': 6,
        '6': 5,
        '5': 4,
        '4': 3,
        '3': 2,
        '2': 1,
        'J': 0
    }

    GTYPES = {
        # Five of a kind, where all five cards have the same label: AAAAA
        '5OAK': 6,
        # Four of a kind, where four cards have the same label and one card has a different label: AA8AA
        '4OAK': 5,
        # Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
        'FH': 4,
        # Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
        '3OAK': 3,
        # Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
        'TP': 2,
        # One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
        'OP': 1,
        # High card, where all cards' labels are distinct: 23456
        'HC': 0
    }

    def classify_hand(self, hand):
        hand = sorted(hand)

        joker = False
        if 'J' in hand:
            joker = True

        new_list = hand
        if joker:
            mc = Counter(hand).most_common(2)
            if len(mc) == 1:
                new_list = hand
            else:
                replace = mc[0][0]
                if replace == "J":
                    replace = mc[1][0]
                new_list = sorted([replace if item == "J" else item for item in hand])

        # AAAAAA
        if new_list[0] == new_list[4]:
            return self.GTYPES["5OAK"]

        # AA8AA
        if new_list[0] == new_list[3] or new_list[1] == new_list[4]:
            return self.GTYPES["4OAK"]

        # 23332
        dist_groups = Counter(new_list)
        if len(dist_groups.values()) == 2:
            return self.GTYPES["FH"]

        # TTT98
        if len(dist_groups.values()) == 3 and dist_groups.most_common(1)[0][1] == 3:
            return self.GTYPES["3OAK"]

        # 23432
        if len(dist_groups.values()) == 3 and dist_groups.most_common(1)[0][1] == 2:
            return self.GTYPES["TP"]

        # A23A4
        if len(dist_groups.values()) == 4:
            return self.GTYPES["OP"]

        # 23456
        if len(dist_groups.values()) == 5:
            return self.GTYPES["HC"]

        return None

    def __init__(self):
        self.hands = []

    def parse_line(self, line):
        hand = {}

        la = line.rstrip('\n').split(' ')
        lhand = la[0]
        lbid = la[1]

        hand["handarr"] = lhand
        hand["bid"] = lbid

        hand["type"] = self.classify_hand(lhand)
        hand["num_handarr"] = [self.CARD_EXP_VALUES[x] for x in lhand]
        hand["numvalue"] = int("".join(str(x) for x in hand["num_handarr"]))

        self.hands.append(hand)

    def parse_file(self, filename):
        with open(filename) as f:
            for line in f:
                self.parse_line(line)

        sorted_hands = sorted(self.hands, key=lambda x: x["type"])
        overall_sorted = sorted(sorted_hands, key=functools.cmp_to_key(deep_compare))
        # pprint(overall_sorted)

        sum = 0
        for h in range(0, len(overall_sorted)):
            sum += int(overall_sorted[h]["bid"]) * (h+1)

        return sum

def deep_compare(a, b):
    if a["type"] != b["type"]:
        return 0

    for i in range(0, 5):
        if a["num_handarr"][i] > b["num_handarr"][i]:
            return 1
        if a["num_handarr"][i] < b["num_handarr"][i]:
            return -1