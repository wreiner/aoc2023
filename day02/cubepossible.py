import re

class CubePossible():
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
