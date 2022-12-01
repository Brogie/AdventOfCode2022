from input_formatter import get_input_as_numbers


def part1():
    data = get_input_as_numbers(1, 2022, False)
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


def part2():
    data = get_input_as_numbers(1, 2022, False)
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


print(part1())
print(part2())
