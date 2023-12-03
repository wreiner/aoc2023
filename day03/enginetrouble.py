class EngineTrouble:
    symbols = {}
    numbers = []

    sum = 0

    def parse_line(self, line_number, line):
        number = {
            "value": "",
            "line": -1,
            "start": -1,
            "end": -1
        }

        for col in range(0, len(line)):
            print(f"{col}: {line[col]}")

            if (re.match("[^\w.]", line[col])):
                print("symbol found")
                if (number["value"] != ""):
                    self.sum += int(number["value"])
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
                print(f"will add {line[col]}")
                number["value"] += line[col]

                number["line"] = line_number

                if number["start"] < 0:
                    number["start"] = col

            if (line[col] == "."):
                if (number["value"] != ""):
                    number["end"] = col
                    self.numbers.append(number)
                    number = {
                        "value": "",
                        "line": -1,
                        "start": -1,
                        "end": -1
                    }

    def get_front_adjacent(self):
        print(self.symbols)
        print(self.numbers)

        for numberob in self.numbers:
            print(f"working on {numberob}")

            numline = numberob["line"]
            startcol = numberob["start"]
            endcol = numberob["end"]
            print(f"numline {numline} | {startcol}:{endcol}")

            # check for front adjecent
            if startcol - 1 in self.symbols[numline]:
                print("found")
                self.sum += int(numberob["value"])

        return self.sum

    def get_back_adjecent(self):
        return self.sum

