import re

class MoveIt():
    def __init__(self):
        self.part_two_races = []
        pass

    def get_possible_moves_for_game(self, max_time, distance_to_beat):
        for h_hold in range(1, max_time):
            s_speed = h_hold
            mt_max_move_time = max_time - h_hold
            t_traveled_distance = s_speed * mt_max_move_time
            if (t_traveled_distance > distance_to_beat):
                break

        print(f"max reached h: {h_hold}")
        # add first and last as there is no movement, but first is 0
        num_poss_moves = max_time - 2*h_hold + 1
        print(f"poss_moves: {num_poss_moves}")
        return num_poss_moves

    def part_one_get_product_of_possible_moves(self, filename):
        product = 1
        with open(filename) as f:
            i = 0
            for line in f:
                a = line.rstrip('\n').split(":")[1].lstrip(" ")
                a = re.sub("\s+", "", a)

                print(f"{a}")

                if i == 0:
                    self.part_two_races.append({"max_hold_time": int(a)})
                else:
                    self.part_two_races[0]["distance_to_beat"] = int(a)

                i += 1

        for race in self.part_two_races:
            product *= self.get_possible_moves_for_game(race["max_hold_time"], race["distance_to_beat"])

        return product