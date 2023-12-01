import re

class LineCounter():
    WORDS2NUMS = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    def complete_number_of_line(self, line):
        return int(re.sub("[^0-9.]", "", line))

    def check_if_number_word_in_word(self, word):
        for numword in self.WORDS2NUMS:
            if (numword in word):
                return self.WORDS2NUMS[numword]
        return -1

    def parse_line_for_number_word(self, line):
        numbers = []
        word = ""
        for char in line:
            if (char.isnumeric()):
                numbers.append(char)
                word = ""
                continue

            word += char

            valid_num_word = self.check_if_number_word_in_word(word)
            if (valid_num_word > 0):
                numbers.append(valid_num_word)
                word = word[-1]

        s = f"{numbers[0]}{numbers[-1]}"
        return int(''.join(s))

    def number_of_line(self, line):
        numbers = re.sub("[^0-9.]", "", line)
        return int(f"{numbers[0]}{numbers[-1]}")

    def get_numbers_from_file(self, filename):
        numbers = []
        with open(filename) as f:
            for line in f:
                numbers.append(self.number_of_line(line))
        return numbers

    def get_numbers_from_file_words(self, filename):
        numbers = []
        with open(filename) as f:
            for line in f:
                numbers.append(self.parse_line_for_number_word(line))
        return numbers

    def sum_of_numbers(self, numbers):
        return sum(numbers)
