import re

def parse(str):
    with open(str) as file:
        dict ={}
        for line in file:
            game = re.search(r'Game (\d+):', line).group(1)
            sets = line.split(';')
            counts = []
            for set in sets:
                red_count = re.search(r'(\d+) red', set)
                green_count = re.search(r'(\d+) green', set)
                blue_count = re.search(r'(\d+) blue', set)

                red = int(red_count.group(1)) if red_count else 0
                green = int(green_count.group(1)) if green_count else 0
                blue = int(blue_count.group(1)) if blue_count else 0

                counts.append((red, green, blue))

            dict[game] = counts
    return dict

def find_possible_games(sets, max):
    return all(t <= m for t, m in zip(sets, max))

def find_maxset(sets):
    max_red = max(set[0] for set in sets)
    max_green = max(set[1] for set in sets)
    max_blue = max(set[2] for set in sets)
    return max_red * max_green * max_blue

max_values = (12,13,14)
dict = parse('input.txt')
print("first question:", sum(int(key) for key, value in dict.items() if all(find_possible_games(sets, max_values) for sets in value)))
print("second question:", sum(find_maxset(value) for value in dict.values()))