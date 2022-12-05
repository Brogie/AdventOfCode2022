import time
import re
from input_formatter import get_input_raw

timings = []


def create_crate_map(is_sample):
    if is_sample:
        return {
            "1": ["Z", "N"],
            "2": ["M", "C", "D"],
            "3": ["P"],
        }
    else:
        return {
            "1": ["Z", "J", "G"],
            "2": ["Q", "L", "R", "P", "W", "F", "V", "C"],
            "3": ["F", "P", "M", "C", "L", "G", "R"],
            "4": ["L", "F", "B", "W", "P", "H", "M"],
            "5": ["G", "C", "F", "S", "V", "Q"],
            "6": ["W", "H", "J", "Z", "M", "Q", "T", "L"],
            "7": ["H", "F", "S", "B", "V"],
            "8": ["F", "J", "Z", "S"],
            "9": ["M", "C", "D", "P", "F", "H", "B", "T"]
        }


def part1(is_sample):
    data = get_input_raw(5, 2022, is_sample)
    _, instructions = data.split("\n\n")
    instructions = instructions.split("\n")
    crate_map = create_crate_map(is_sample)

    for instruction in instructions:
        moves = re.findall(r"\d+", instruction)
        for _ in range(int(moves[0])):
            crate = crate_map[moves[1]].pop()
            crate_map[moves[2]].append(crate)

    answer = ""
    for stack in crate_map:
        answer += crate_map[stack].pop()
    return answer


def part2(is_sample):
    data = get_input_raw(5, 2022, is_sample)
    _, instructions = data.split("\n\n")
    instructions = instructions.split("\n")
    crate_map = create_crate_map(is_sample)

    for instruction in instructions:
        moves = re.findall(r"\d+", instruction)
        crates = crate_map[moves[1]][-int(moves[0]):]
        crate_map[moves[1]] = crate_map[moves[1]][:-int(moves[0])]
        crate_map[moves[2]] = crate_map[moves[2]] + crates

    answer = ""
    for stack in crate_map:
        answer += crate_map[stack].pop()
    return answer


if __name__ == '__main__':
    print(part1(False))
    print(part2(False))
else:
    start = time.time()
    for _ in range(100):
        ans = part1(False)
    end = time.time()
    timings.append(["Day5", "Part 1", ans, (end - start) / 100])

    start = time.time()
    for _ in range(100):
        ans = part2(False)
    end = time.time()
    timings.append(["Day5", "Part 2", ans, (end - start) / 100])
