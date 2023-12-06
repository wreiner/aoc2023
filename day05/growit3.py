import re
from pprint import pprint
import itertools

class GrowIt():
    def __init__(self):
        self.seeds = []
        self.maps = []
        return

    def get_seeds_array(self, line):
        seeds_boundaries = line.split(": ")[1].split(" ")
        seeds_boundaries = list(map(int, seeds_boundaries))
        for i in range(0, len(seeds_boundaries), 2):
            seed_group = {}
            seed_group["start"] = seeds_boundaries[i]
            seed_group["end"] = seeds_boundaries[i] + seeds_boundaries[i+1]
            self.seeds.append(seed_group)
        print(f"{self.seeds}")

    def parse_map_line(self, line):
        map_parts = line.split(" ")
        map_parts = list(map(int, map_parts))
        # print(map_parts)

        map_dict = {"input": {}, "output": {}}
        map_dict["input"]["start"] = map_parts[0]
        map_dict["input"]["end"] = map_parts[0] + map_parts[2]

        map_dict["output"]["start"] = map_parts[1]
        map_dict["output"]["end"] = map_parts[1] + map_parts[2]

        return map_dict

    def get_output_to_input(self, seed, map):
        # print(f"map: {map} for seed: {seed}")
        # print(f"checking map for seed: {seed}")
        for mapitem in map:
            print(f"mapitem: {mapitem}")
            print(f'{mapitem["input"]["start"]} <= {seed} AND {seed} <= {mapitem["input"]["end"]}')
            if mapitem["input"]["start"] <= seed and seed <= mapitem["input"]["end"]:
                lookup_difference = seed - mapitem["input"]["start"]
                print(f"lookup_difference {lookup_difference}")
                return mapitem["output"]["start"] + lookup_difference

        return seed




    def parse_file(self, filename):
        map = ""
        i = -1
        with open(filename) as f:
            for line in f:
                line = line.rstrip("\n")

                if re.match("^seeds:", line):
                    self.get_seeds_array(line)
                    continue

                maparr = re.match("^(.*?)\smap:", line)
                if maparr:
                    i += 1
                    map = maparr.group(1)
                    self.maps.append([])
                    # self.maps[map] = []
                    continue

                if re.match("^$", line):
                    continue

                # self.maps[map].append(self.parse_map_line(line))
                self.maps[i].append(self.parse_map_line(line))

        # pprint(self.maps)

        i = 0
        for i in itertools.count(start=52510809):
            input = i
            # print(f"will check for soil {i}")

            if i % 10000 == 0:
                print(f"we are on {i}")

            k = 0
            for map in reversed(self.maps):
                input = self.get_output_to_input_reverse(input, map)
                # print(f"----- {k} {input}")
                # if k == 6:
                #     break
                # k += 1

            if i >= 52510810:
                print("---------- ERROR ---------------")

            # print(f"--- final input to check {input}")
            if self.check_if_in_seeds_array(input):
                return i

    def check_if_in_seeds_array(self, input):
        for seeditem in self.seeds:
            # print(f"seeditem: {seeditem}")
            if seeditem["start"] <= input and input <= seeditem["end"]:
                print(f"found")
                return True

    def get_output_to_input_reverse(self, seed, map):
        # print(f"map: {map}")
        # print(f"checking map for seed: {seed}")
        for mapitem in map:
            # print(f"mapitem: {mapitem}")
            # print(f'{mapitem["input"]["start"]} <= {seed} AND {seed} <= {mapitem["input"]["end"]}')
            if mapitem["input"]["start"] <= seed and seed <= mapitem["input"]["end"]:
                lookup_difference = seed - mapitem["input"]["start"]
                # print(f"lookup_difference {lookup_difference}")
                return mapitem["output"]["start"] + lookup_difference

        return seed
