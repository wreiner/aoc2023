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
            print(f"testing {color} for {max_value}")

            pattern = f"(\d+){color}"

            for set in sets_array:
                print(f"checking set {set}")
                content_array = re.match(pattern, set)
                if content_array:
                    print(f"found data {content_array.group(1)}")
                    if (int(content_array.group(1)) > self.VALID_GAME_CRITERIA[color]):
                        print("game not valid")
                        return False
        return True
