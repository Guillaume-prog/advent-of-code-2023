from aoc import load_input
import re


data = load_input(__file__)





def parse_line(line):
    numbers = re.findall(r"\d", line)
    return int(numbers[0] + numbers[-1])

answer1 = sum([ parse_line(l) for l in data ])
print(f"Part 1: {answer1}")





def parse_line_2(line):
    # (?=...) -> positive lookahead that allows overlapping matches
    numbers = re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line)

    num_dict = { "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9" }
    convert_word = lambda word: num_dict[word] if word in num_dict else word

    return int(convert_word(numbers[0]) + convert_word(numbers[-1]))

answer2 = sum([ parse_line_2(l) for l in data ])
print(f"Part 2: {answer2}")