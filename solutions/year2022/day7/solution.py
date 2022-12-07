import time
from input_formatter import get_deliminated_input

timings = []


def part1(is_sample):
    commands = get_deliminated_input(7, 2022, is_sample, " ")
    current_tree = [">"]
    dir_sizes = {}

    for command in commands:
        if command[0] == "$":
            match command[1]:
                case "cd":
                    if command[2] == "..":
                        current_tree = current_tree[:-1]
                    else:
                        current_tree.append(current_tree[-1] + "/" + command[2])
        elif command[0] != "dir":
            for directory in current_tree:
                if directory not in dir_sizes:
                    dir_sizes[directory] = int(command[0])
                else:
                    dir_sizes[directory] += int(command[0])

    score = 0
    for directory in dir_sizes:
        if dir_sizes[directory] <= 100000 and directory != ">" and directory != ">//":
            score += dir_sizes[directory]

    return score


def part2(is_sample):
    commands = get_deliminated_input(7, 2022, is_sample, " ")
    current_tree = [">"]
    dir_sizes = {}

    for command in commands:
        if command[0] == "$":
            match command[1]:
                case "cd":
                    if command[2] == "..":
                        current_tree = current_tree[:-1]
                    else:
                        current_tree.append(current_tree[-1] + "/" + command[2])
        elif command[0] != "dir":
            for directory in current_tree:
                if directory not in dir_sizes:
                    dir_sizes[directory] = int(command[0])
                else:
                    dir_sizes[directory] += int(command[0])

    unused_space = 70000000 - dir_sizes[">"]
    smallest_dir_size = 100000000000
    for directory in dir_sizes:
        if unused_space + dir_sizes[directory] > 30000000:
            if dir_sizes[directory] < smallest_dir_size:
                smallest_dir_size = dir_sizes[directory]

    return smallest_dir_size


if __name__ == '__main__':
    print(part1(False))
    print(part2(False))
else:
    start = time.time()
    for _ in range(100):
        ans = part1(False)
    end = time.time()
    timings.append(["Day 7", "Part 1", ans, (end - start) / 100])

    start = time.time()
    for _ in range(100):
        ans = part2(False)
    end = time.time()
    timings.append(["Day 7", "Part 2", ans, (end - start) / 100])
