import time

timings = []


def part1(is_sample):
    return "Not implemented"


def part2(is_sample):
    return "Not implemented"


if __name__ == '__main__':
    print(part1(True))
    print(part2(True))
else:
    start = time.time()
    for _ in range(100):
        ans = part1(False)
    end = time.time()
    timings.append(["Day x", "Part 1", ans, (end - start) / 100])

    start = time.time()
    for _ in range(100):
        ans = part2(False)
    end = time.time()
    timings.append(["Day x", "Part 2", ans, (end - start) / 100])
