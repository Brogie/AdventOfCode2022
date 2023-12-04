import time
from input_formatter import get_deliminated_input


timings = []


def part1(is_sample):
    games = get_deliminated_input(2, 2023, is_sample, ':')
    max_red = 12
    max_green = 13
    max_blue = 14
    output = 0
    game_number = 0
    for game in games:
        game_number += 1
        possible = True
        for hand in game[1].split(';'):
            for dice in hand.strip().split(','):
                combo = dice.strip().split(' ')
                match combo[1]:
                    case 'red':
                        if int(combo[0]) > max_red: possible = False
                    case 'green':
                        if int(combo[0]) > max_green: possible = False
                    case 'blue':
                        if int(combo[0]) > max_blue: possible = False
        if possible:
            output += game_number

    return output


def part2(is_sample):
    games = get_deliminated_input(2, 2023, is_sample, ':')
    output = 0
    for game in games:
        min_red = 0
        min_green = 0
        min_blue = 0
        for hand in game[1].split(';'):
            for dice in hand.strip().split(','):
                combo = dice.strip().split(' ')
                match combo[1]:
                    case 'red':
                        if int(combo[0]) > min_red: min_red = int(combo[0])
                    case 'green':
                        if int(combo[0]) > min_green: min_green = int(combo[0])
                    case 'blue':
                        if int(combo[0]) > min_blue: min_blue = int(combo[0])
        output += min_red * min_green * min_blue

    return output


if __name__ == '__main__':
    print(part1(False))
    print(part2(False))
else:
    start = time.time()
    for _ in range(100):
        ans = part1(False)
    end = time.time()
    timings.append(["Day 2", "Part 1", ans, (end - start) / 100])

    start = time.time()
    for _ in range(100):
        ans = part2(False)
    end = time.time()
    timings.append(["Day 2", "Part 2", ans, (end - start) / 100])
