import time

from input_formatter import get_input_raw

timings = []


def part1(is_sample):
    signal = get_input_raw(6, 2022, is_sample)
    sample = signal[:4]
    for i in range(3, len(signal)):
        sample = sample[1:]
        sample += signal[i]
        if len(set(sample)) == 4:
            return i + 1
    return "Not Found"


def part2(is_sample):
    signal = get_input_raw(6, 2022, is_sample)
    sample = signal[:14]
    for i in range(13, len(signal)):
        sample = sample[1:]
        sample += signal[i]
        if len(set(sample)) == 14:
            return i + 1
    return "Not Found"


if __name__ == '__main__':
    print(part1(False))
    print(part2(False))
else:
    start = time.time()
    for _ in range(100):
        ans = part1(False)
    end = time.time()
    timings.append(["Day 6", "Part 1", ans, (end - start) / 100])

    start = time.time()
    for _ in range(100):
        ans = part2(False)
    end = time.time()
    timings.append(["Day 6", "Part 2", ans, (end - start) / 100])
