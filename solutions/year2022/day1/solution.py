import time

from input_formatter import get_input_as_numbers


def part1(is_sample):
    data = get_input_as_numbers(1, 2022, is_sample)
    data.append(None)
    max_calories = 0
    total_elf_calories = 0
    for meal in data:
        if meal is not None:
            total_elf_calories += meal
        else:
            if total_elf_calories > max_calories:
                max_calories = total_elf_calories
            total_elf_calories = 0
    return max_calories


def part2(is_sample):
    data = get_input_as_numbers(1, 2022, is_sample)
    data.append(None)
    max_calories = []
    total_elf_calories = 0
    for meal in data:
        if meal is not None:
            total_elf_calories += meal
        else:
            max_calories.append(total_elf_calories)
            total_elf_calories = 0
    return sum(sorted(max_calories, reverse=True)[0:3])


timings = []

start = time.time()
for _ in range(100):
    ans = part1(False)
end = time.time()
timings.append(["Day 1", "Part 1", ans, (end - start) / 100])

start = time.time()
for _ in range(100):
    ans = part2(False)
end = time.time()
timings.append(["Day 1", "Part 2", ans, (end - start) / 100])

print(part1(False))
print(part2(False))

