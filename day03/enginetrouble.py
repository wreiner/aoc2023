import re
from pprint import pprint

class EngineTrouble():
    def __init__(self):
        self.symbols = {}
        self.numbers = []
        self.numbers_by_line = {}
        self.adj_numbers = []
        self.sum = 0
        self.sum_gear_ratios = 0

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

                    if line_number not in self.numbers_by_line:
                        self.numbers_by_line[line_number] = []

                    self.numbers_by_line[line_number].append(number)

                    number = {
                        "value": "",
                        "line": -1,
                        "start": -1,
                        "end": -1
                    }

                if line_number not in self.symbols:
                    self.symbols[line_number] = []

                self.symbols[line_number].append([col, line[col]])

            if (line[col].isdigit()):
                number["value"] += line[col]

                number["line"] = line_number

                if number["start"] < 0:
                    number["start"] = col

            if (line[col] == "."):
                if (number["value"] != ""):
                    number["end"] = col - 1
                    self.numbers.append(number)

                    if line_number not in self.numbers_by_line:
                        self.numbers_by_line[line_number] = []

                    self.numbers_by_line[line_number].append(number)

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
            if element[0] >= checkstart and element[0] <= checkend:
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

    # def is_number_adjecent(self, linenum, checkstart, checkend):
    #     print(f"--------------------\nchecking if a number is on {linenum} between {checkstart} and {checkend}")

    #     if not linenum in self.numbers_by_line:
    #         return False

    #     for numberob in self.numbers_by_line[linenum]:
    #         found = False
    #         # print(f"working on {numberob}\ncurrent sum: {self.sum}")

    #         # find numbers larger than the cutout we check
    #         if numberob["start"] < checkstart and numberob["end"] > checkend:
    #             found = True
    #         elif numberob["start"] >= checkstart and numberob["start"] <= checkend:
    #             found = True
    #         elif numberob["end"] >= checkstart and numberob["end"] <= checkend:
    #             found = True

    #         if found:
    #             print(f"number {numberob['value']} is added to adj numbers ..")
    #             self.adj_numbers.append(numberob)

    def is_number_adjecent(self, linenum, checkstart, checkend):
        for numberob in self.numbers:
            found = False
            if numberob["line"] != linenum:
                # print("not on check line")
                continue

            # find numbers larger than the cutout we check
            if numberob["start"] < checkstart and numberob["end"] > checkend:
                found = True
            elif numberob["start"] >= checkstart and numberob["start"] <= checkend:
                found = True
            elif numberob["end"] >= checkstart and numberob["end"] <= checkend:
                found = True

            if found:
                self.adj_numbers.append(numberob)

    def find_gear_ratio(self):
        pprint(self.symbols)
        pprint(self.numbers)
        pprint(self.numbers_by_line)

        if not self.numbers:
            print("no numbers found")
            return -1

        numbers_max_line = max(self.numbers, key=lambda x: x.get('line', float('-inf')))["line"]

        for linenum in self.symbols:
            for element in self.symbols[linenum]:
                self.adj_numbers = []

                if element[1] != "*":
                    # print(f"{element} is not *")
                    continue

                print(f"element {element} on {linenum} is *")
                checkstart = element[0] - 1
                checkend = element[0] + 1

                # check above
                if linenum != 0:
                    checklinenum = linenum - 1
                    self.is_number_adjecent(checklinenum, checkstart, checkend)

                # check below
                if linenum < numbers_max_line:
                    checklinenum = linenum + 1
                    self.is_number_adjecent(checklinenum, checkstart, checkend)

                # check same line
                checklinenum = linenum
                self.is_number_adjecent(checklinenum, checkstart, checkend)

                if len(self.adj_numbers) == 2:
                    print(f"only two adj numbers found {self.adj_numbers}, will multiply and add to sum")
                    self.sum_gear_ratios += (int(self.adj_numbers[0]["value"]) * int(self.adj_numbers[1]["value"]))
                    print(f"current sum: {self.sum_gear_ratios}")
                    continue

        return self.sum_gear_ratios

    def parse_engine_file(self, filename):
        linenum = 0
        with open(filename) as f:
            for line in f:
                self.parse_line(linenum, line.rstrip('\n'))
                linenum += 1
        return self.sum
