import time
import numpy as np
from input_formatter import get_input


def find_dupe(compartment1, compartment2):
    for item in compartment1:
        if item in compartment2:
            return item


def find_dupe_2(rucksack1, rucksack2, rucksack3):
    for item in rucksack1:
        if item in rucksack2 and item in rucksack3:
            return item


def get_priority(item):
    if item.isupper():
        return ord(item) - 38
    else:
        return ord(item) - 96


def part1(is_sample):
    data = get_input(3, 2022, is_sample)
    total_priority = 0
    for rucksack in data:
        compartment1, compartment2 = rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:]
        dupe = find_dupe(compartment1, compartment2)
        total_priority += get_priority(dupe)
    return total_priority


def part2(is_sample):
    data = get_input(3, 2022, is_sample)
    groups = np.array_split(data, len(data)/3)
    total_priority = 0
    for group in groups:
        dupe = find_dupe_2(group[0], group[1], group[2])
        total_priority += get_priority(dupe)
    return total_priority


timings = []

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

print(part1(False))
print(part2(False))
