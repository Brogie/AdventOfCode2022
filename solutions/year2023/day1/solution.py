import time
from input_formatter import get_input
timings = []


def part1(is_sample):
    data = get_input(1, 2023, is_sample)
    output = 0
    for calibrationValue in data:
        filtered = ''.join(filter(str.isdigit, calibrationValue))
        output += int(filtered[0] + filtered[-1])

    return output


def part2(is_sample):
    data = get_input(1, 2023, is_sample)
    output = 0
    for calibration_value in data:
        fixed_calibration_value = calibration_value
        offset = 1
        for i in range(0, len(calibration_value)):
            substring = calibration_value[i: len(calibration_value)]
            substring = ''.join(filter(str.isalpha, substring))
            if substring.startswith('one'):
                fixed_calibration_value = fixed_calibration_value[:offset + i] + '1' + fixed_calibration_value[offset + i:]
                offset += 1
            if substring.startswith('two'):
                fixed_calibration_value = fixed_calibration_value[:offset + i] + '2' + fixed_calibration_value[offset + i:]
                offset += 1
            if substring.startswith('three'):
                fixed_calibration_value = fixed_calibration_value[:offset + i] + '3' + fixed_calibration_value[offset + i:]
                offset += 1
            if substring.startswith('four'):
                fixed_calibration_value = fixed_calibration_value[:offset + i] + '4' + fixed_calibration_value[offset + i:]
                offset += 1
            if substring.startswith('five'):
                fixed_calibration_value = fixed_calibration_value[:offset + i] + '5' + fixed_calibration_value[offset + i:]
                offset += 1
            if substring.startswith('six'):
                fixed_calibration_value = fixed_calibration_value[:offset + i] + '6' + fixed_calibration_value[offset + i:]
                offset += 1
            if substring.startswith('seven'):
                fixed_calibration_value = fixed_calibration_value[:offset + i] + '7' + fixed_calibration_value[offset + i:]
                offset += 1
            if substring.startswith('eight'):
                fixed_calibration_value = fixed_calibration_value[:offset + i] + '8' + fixed_calibration_value[offset + i:]
                offset += 1
            if substring.startswith('nine'):
                fixed_calibration_value = fixed_calibration_value[:offset + i] + '9' + fixed_calibration_value[offset + i:]
                offset += 1

        filtered = ''.join(filter(str.isdigit, fixed_calibration_value))
        output += int(filtered[0] + filtered[-1])

    return output


def optimised(is_sample):
    data = get_input(1, 2023, is_sample)
    output = 0
    for calibration_value in data:
        calibration_value = calibration_value.replace('one', 'o1e')
        calibration_value = calibration_value.replace('two', 't2o')
        calibration_value = calibration_value.replace('three', 't3ree')
        calibration_value = calibration_value.replace('four', 'f4ur')
        calibration_value = calibration_value.replace('five', 'f5ive')
        calibration_value = calibration_value.replace('six', 's6x')
        calibration_value = calibration_value.replace('seven', 's7even')
        calibration_value = calibration_value.replace('eight', 'e8ght')
        calibration_value = calibration_value.replace('nine', 'n9ne')
        filtered = ''.join(filter(str.isdigit, calibration_value))
        output += int(filtered[0] + filtered[-1])

    return output


if __name__ == '__main__':
    print(part1(False))
    print(part2(False))
    print(optimised(False))
else:
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

    start = time.time()
    for _ in range(100):
        ans = optimised(False)
    end = time.time()
    timings.append(["Day 1", "Optimised Part 2", ans, (end - start) / 100])
