import re

class CubePossible():
    VALID_GAME_CRITERIA = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    def cleanup_line(self, line):
        # remove the game and its id
        line = re.sub('^Game\s(\d+):\s', '', line)
        # print(line)

        # remove all spaces
        line = re.sub('\s', '', line)
        # print(line)

        return line

    def extract_sets(self, line):
        line = self.cleanup_line(line)

        sets_array = re.split(';', line)
        # print(sets_array)

        return sets_array

    def get_game_id(self, line):
        content_array = re.match('^Game\s(\d+):', line)
        if content_array:
            return int(content_array.group(1))

        # not a valid line
        return None

    def is_game_valid(self, line):
        sets_array = self.extract_sets(line)

        for color, max_value in self.VALID_GAME_CRITERIA.items():
            # print(f"testing {color} for {max_value}")

            pattern = f"(\d+){color}"

            for set in sets_array:
                # print("")
                # print(f"checking set {set} for {pattern}")
                content_array = re.search(pattern, set)
                if content_array:
                    # print(f"found data {content_array.group(1)}")
                    if (int(content_array.group(1)) > max_value):
                        # print("game not valid")
                        return False

        return True

    def sum_of_games_from_file(self, filename):
        sum = 0
        with open(filename) as f:
            for line in f:
                game_id = self.get_game_id(line)
                if (self.is_game_valid(line)):
                    sum += game_id
        return sum

    def get_power_of_a_game(self, line):
        color_max = {"red": 0, "green": 0, "blue": 0}
        sets_array = self.extract_sets(line)
        for color in self.VALID_GAME_CRITERIA.keys():
            # print(f"looking for color {color}")

            pattern = f"(\d+){color}"

            for set in sets_array:
                # print("")
                # print(f"checking set {set} for {pattern}")
                content_array = re.search(pattern, set)
                if content_array:
                    if (int(content_array.group(1)) > color_max[color]):
                        color_max[color] = int(content_array.group(1))

        # print(color_max)
        return color_max["red"] * color_max["green"] * color_max["blue"]

    def powersum_of_games_from_file(self, filename):
        powersum = 0
        with open(filename) as f:
            for line in f:
                game_power = self.get_power_of_a_game(line)
                powersum += game_power

        return powersum
