import re
from pprint import pprint

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
            seed_group["count"] = seeds_boundaries[i+1]
            self.seeds.append(seed_group)
        print(f"{self.seeds}")

    def parse_map_line(self, line):
        map_parts = line.split(" ")
        map_parts = list(map(int, map_parts))
        # print(map_parts)

        map_dict = {"input": {}, "output": {}}
        map_dict["output"]["start"] = map_parts[0]
        map_dict["output"]["end"] = map_parts[0] + map_parts[2]

        map_dict["input"]["start"] = map_parts[1]
        map_dict["input"]["end"] = map_parts[1] + map_parts[2]

        return map_dict

    def get_output_to_input(self, seed, map):
        # print(f"map: {map} for seed: {seed}")
        # print(f"checking map for seed: {seed}")
        for mapitem in map:
            # print(f"mapitem: {mapitem}")
            if mapitem["input"]["start"] <= seed and seed <= mapitem["input"]["end"]:
                lookup_difference = seed - mapitem["input"]["start"]
                # print(f"lookup_difference {lookup_difference}")
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

        min = -1
        for seedgrp in self.seeds:
            for seed in range(seedgrp["start"], seedgrp["start"] + seedgrp["count"]):
                input = seed
                for map in self.maps:
                    # print(f"will walk map for {input}")
                    input = self.get_output_to_input(input, map)

                if min < 0 or input < min:
                    min = input

            # print(input)

        return min
