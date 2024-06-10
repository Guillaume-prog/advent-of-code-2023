from aoc import load_input
import re
from pprint import pprint

input = load_input(__file__)

def parse_set(set):
    rgb = (0, 0, 0)
    order = ['red', 'green', 'blue']

    for item in set.strip().split(', '):
        num, color = item.split(' ')
        rgb[order.index(color)] += int(num)

    return rgb

constraints = (12, 13, 14)
id_sum = 0

for line in input:
    
    game, items = line.split(':')
    game_id = int(game.split(' ')[1])

    for set in items.split(";"):
        rgb = parse_set(set)
        if any([rgb[i] > constraints[i] for i in range(3)]):
            break

    id_sum += game_id

print(id_sum)

    