import re

class CubePossible():
    def get_game_id(self, line):
        content_array = re.match('^Game\s(\d+):', line)
        if content_array:
            return int(content_array.group(1))

        # not a valid line
        return None
