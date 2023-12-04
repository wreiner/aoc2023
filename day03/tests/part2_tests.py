import unittest

from enginetrouble import EngineTrouble

class Testing(unittest.TestCase):
    def test_two_star_adjecent_vertical(self):
        line1 = "467..114.."
        line2 = "...*......"
        line3 = "..35..633."
        should_value = 16345

        enginetrouble = EngineTrouble()
        enginetrouble.parse_line(0, line1)
        enginetrouble.parse_line(1, line2)
        enginetrouble.parse_line(2, line3)
        is_value = enginetrouble.find_gear_ratio()

        self.assertEqual(should_value, is_value)

    def test_two_star_adjecent_vertical_2(self):
        line1 = "......755."
        line2 = "...$.*...."
        line3 = ".664.598.."
        should_value = 451490

        enginetrouble = EngineTrouble()
        enginetrouble.parse_line(0, line1)
        enginetrouble.parse_line(1, line2)
        enginetrouble.parse_line(2, line3)
        is_value = enginetrouble.find_gear_ratio()

        self.assertEqual(should_value, is_value)

    def test_two_star_adjecent_horizontal(self):
        line1 = ".....114.."
        line2 = "467*35...."
        line3 = "......633."
        should_value = 16345

        enginetrouble = EngineTrouble()
        enginetrouble.parse_line(0, line1)
        enginetrouble.parse_line(1, line2)
        enginetrouble.parse_line(2, line3)
        is_value = enginetrouble.find_gear_ratio()

        self.assertEqual(should_value, is_value)

    def test_with_testinput(self):
        filename = "inputs/part1-test-input"
        should_value = 467835

        enginetrouble = EngineTrouble()
        enginetrouble.parse_engine_file(filename)
        is_value = enginetrouble.find_gear_ratio()

        self.assertEqual(should_value, is_value)

    def test_two_star_adjecent_complpart01(self):
        line1 = "...................15....904...........850.................329...................13....................................871....816....697...."
        line2 = "...........53.497........................%....906...610.......*.............735#..&...*......558...68...............68..*......&....*......."
        line3 = "..........*....$....................132.........*..........844....875................350............*...............*..336.364...649........"
        should_value = 1022685

        enginetrouble = EngineTrouble()
        enginetrouble.parse_line(0, line1)
        enginetrouble.parse_line(1, line2)
        enginetrouble.parse_line(2, line3)
        is_value = enginetrouble.find_gear_ratio()

        self.assertEqual(should_value, is_value)

    def test_two_star_adjecent_complpart02(self):
        line1 = "...................15....904...........850.................329...................13....................................871....816....697...."
        line2 = "...........53.497........................%....906...610.......*.............735#..&...*......558...68...............68..*......&....*......."
        line3 = "..........*....$....................132.........*..........844....875................350............*...............*..336.364...649........"
        line4 = ".......726.......341..................*...186...358..................*244........57.......@.........738......*.....663.................584.."
        should_value = 1694279

        enginetrouble = EngineTrouble()
        enginetrouble.parse_line(0, line1)
        enginetrouble.parse_line(1, line2)
        enginetrouble.parse_line(2, line3)
        enginetrouble.parse_line(3, line4)
        is_value = enginetrouble.find_gear_ratio()

        self.assertEqual(should_value, is_value)

    def test_with_complete_input(self):
        filename = "inputs/part1-complete-input"
        should_value = 79026871

        enginetrouble = EngineTrouble()
        enginetrouble.parse_engine_file(filename)
        is_value = enginetrouble.find_gear_ratio()

        self.assertEqual(should_value, is_value)

if __name__ == '__main__':
    unittest.main()
