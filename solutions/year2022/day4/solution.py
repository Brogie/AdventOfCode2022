import time
from input_formatter import get_deliminated_input

timings = []


def is_contained_within(a, b):
    elf_a = list(map(int, a.split('-')))
    elf_b = list(map(int, b.split('-')))

    return elf_a[0] >= elf_b[0] and elf_a[1] <= elf_b[1]


def is_overlapping(a, b):
    elf_a = list(map(int, a.split('-')))
    elf_b = list(map(int, b.split('-')))

    contained =     elf_a[0] >= elf_b[0] and elf_a[1] <= elf_b[1]
    left_overlap =  elf_a[0] <= elf_b[0] <= elf_a[1]
    right_overlap = elf_a[0] <= elf_b[1] <= elf_a[0]
    return contained or left_overlap or right_overlap


def part1(is_sample):
    data = get_deliminated_input(4, 2022, is_sample, ',')
    priority = 0
    for group in data:
        if is_contained_within(group[0], group[1]) or is_contained_within(group[1], group[0]):
            priority += 1

    return priority


def part2(is_sample):
    data = get_deliminated_input(4, 2022, is_sample, ',')
    priority = 0
    for group in data:
        if is_overlapping(group[0], group[1]) or is_overlapping(group[1], group[0]):
            priority += 1

    return priority


if __name__ == '__main__':
    print(part1(False))
    print(part2(False))
else:
    start = time.time()
    for _ in range(100):
        ans = part1(False)
    end = time.time()
    timings.append(["Day 4", "Part 1", ans, (end - start) / 100])

    start = time.time()
    for _ in range(100):
        ans = part2(False)
    end = time.time()
    timings.append(["Day 4", "Part 2", ans, (end - start) / 100])
