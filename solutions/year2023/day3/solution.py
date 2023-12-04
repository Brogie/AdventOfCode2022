import time
from input_formatter import get_grid_padded

timings = []


def contains_symbol(num_start, num_end, schematic):
    for i in range(num_start[0] - 1, num_end[0] + 2):
        for j in range(num_start[1] - 1, num_end[1] + 2):
            if not schematic[i][j].isdigit() and schematic[i][j] != '.':
                return True
    return False


def contains_gear(num_start, num_end, schematic):
    for i in range(num_start[0] - 1, num_end[0] + 2):
        for j in range(num_start[1] - 1, num_end[1] + 2):
            if schematic[i][j] == '*':
                return i, j
    return False


def part1(is_sample):
    output = 0
    schematic = get_grid_padded(3, 2023, is_sample, '.')

    num_start = (0, 0)
    num_end = (0, 0)

    reading_number = False
    for i in range(1, len(schematic) - 1):
        for j in range(1, len(schematic[i]) - 1):
            if schematic[i][j].isdigit() and not reading_number:
                num_start = (i, j)
                reading_number = True
            if reading_number:
                if not schematic[i][j+1].isdigit():
                    reading_number = False
                    num_end = (i, j)
                    if contains_symbol(num_start, num_end, schematic):
                        output += int(''.join(schematic[i][num_start[1]:num_end[1]+1]))

    return output


def part2(is_sample):
    output = 0
    schematic = get_grid_padded(3, 2023, is_sample, '.')

    num_start = (0, 0)
    num_end = (0, 0)

    gears = {}

    reading_number = False
    for i in range(1, len(schematic) - 1):
        for j in range(1, len(schematic[i]) - 1):
            if schematic[i][j].isdigit() and not reading_number:
                num_start = (i, j)
                reading_number = True
            if reading_number:
                if not schematic[i][j + 1].isdigit():
                    reading_number = False
                    num_end = (i, j)
                    gear = contains_gear(num_start, num_end, schematic)
                    if gear != False:
                        ratio = int(''.join(schematic[i][num_start[1]:num_end[1] + 1]))
                        if gear in gears:
                            output += ratio * gears[gear]
                        else:
                            gears[gear] = ratio
    return output


if __name__ == '__main__':
    print(part1(False))
    print(part2(False))
else:
    start = time.time()
    for _ in range(100):
        ans = part1(False)
    end = time.time()
    timings.append(["Day 3", "Part 1", ans, (end - start) / 100])

    start = time.time()
    for _ in range(100):
        ans = part2(False)
    end = time.time()
    timings.append(["Day 3", "Part 2", ans, (end - start) / 100])
