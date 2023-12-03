import re
from pprint import pprint

class EngineTrouble():
    def __init__(self):
        self.symbols = {}
        self.numbers = []
        self.sum = 0

    def parse_line(self, line_number, line):
        number = {
            "value": "",
            "line": -1,
            "start": -1,
            "end": -1
        }

        for col in range(0, len(line)):
            # print(f"{col}: {line[col]}")

            if (re.match("[^\w.]", line[col])):
                # print("symbol found")
                if (number["value"] != ""):
                    number["end"] = col - 1
                    self.numbers.append(number)
                    number = {
                        "value": "",
                        "line": -1,
                        "start": -1,
                        "end": -1
                    }

                if line_number not in self.symbols:
                    self.symbols[line_number] = []

                self.symbols[line_number].append(col)

            if (line[col].isdigit()):
                # print(f"will add {line[col]}")
                number["value"] += line[col]

                number["line"] = line_number

                if number["start"] < 0:
                    number["start"] = col

            if (line[col] == "."):
                if (number["value"] != ""):
                    number["end"] = col - 1
                    self.numbers.append(number)
                    number = {
                        "value": "",
                        "line": -1,
                        "start": -1,
                        "end": -1
                    }

        # add stragglers
        if (number["value"] != ""):
            # print("in stragglers")
            number["end"] = col
            self.numbers.append(number)

    def get_front_adjacent(self):
        # print(self.symbols)
        # print(self.numbers)

        for numberob in self.numbers:
            # print(f"working on {numberob}")

            numline = numberob["line"]
            startcol = numberob["start"]
            endcol = numberob["end"]
            # print(f"numline {numline} | {startcol}:{endcol}")

            # check for front adjecent
            if startcol - 1 in self.symbols[numline]:
                # print("found")
                self.sum += int(numberob["value"])

        return self.sum

    def get_back_adjacent(self):
        return self.sum

    def is_symbol_adjecent(self, linenum, checkstart, checkend):
        if checkstart < 0:
            checkstart = 0

        # print(f"checking if symbol on {linenum} between {checkstart} and {checkend}")
        if not linenum in self.symbols:
            return False

        for element in self.symbols[linenum]:
            if element >= checkstart and element <= checkend:
                # print("found")
                return True
        return False

    def sum_adjacent(self):
        # pprint(self.symbols)
        # pprint(self.numbers)

        for numberob in self.numbers:
            # print(f"--------------------\nworking on {numberob}\ncurrent sum: {self.sum}")

            linenum = numberob["line"]
            startcol = numberob["start"]
            endcol = numberob["end"]
            # print(f"linenum {linenum} | {startcol}:{endcol}")

            # check above
            if linenum != 0:
                # print("will check above\n")
                checkline = linenum - 1
                checkstart = startcol - 1
                checkend = endcol + 1

                if self.is_symbol_adjecent(checkline, checkstart, checkend):
                    self.sum += int(numberob["value"])
                    continue

            # check same line
            if linenum != 0:
                # print("will check same line\n")
                checkline = linenum
                checkstart = startcol - 1
                checkend = endcol + 1

                if self.is_symbol_adjecent(checkline, checkstart, checkend):
                    self.sum += int(numberob["value"])
                    continue

            # check below
            if self.symbols and linenum < max(self.symbols, key=int):
                # print("will check below\n")
                checkline = linenum + 1
                checkstart = startcol - 1
                checkend = endcol + 1

                if self.is_symbol_adjecent(checkline, checkstart, checkend):
                    self.sum += int(numberob["value"])
                    continue

        # print(f"---------------- current sum {self.sum}")
        return self.sum

    def parse_engine_file(self, filename):
        linenum = 0
        with open(filename) as f:
            for line in f:
                self.parse_line(linenum, line.rstrip('\n'))
                linenum += 1
        return self.sum
