import os


def get_input_raw(day, year, is_sample):
    if "AdventOfCode2022/solutions/" not in os.getcwd():
        filename = f"./inputs/year{year}/day{day}/input.txt"
    else:
        if is_sample:
            filename = f"../../../inputs/year{year}/day{day}/sample.txt"
        else:
            filename = f"../../../inputs/year{year}/day{day}/input.txt"

    with open(filename) as file:
        return file.read()


def get_input(day, year, is_sample):
    return get_input_raw(day, year, is_sample).splitlines()


def get_input_as_numbers(day, year, is_sample):
    return [int_or_null(x) for x in get_input(day, year, is_sample)]


def get_deliminated_input(day, year, is_sample, deliminator):
    output = []
    for line in get_input(day, year, is_sample):
        output.append(line.split(deliminator))

    return output


def get_grid(day, year, is_sample):
    output = []
    for line in get_input(day, year, is_sample):
        output.append(list(line))

    return output


def get_grid_as_numbers(day, year, is_sample):
    output = []
    for line in get_input(day, year, is_sample):
        output.append([int_or_null(x) for x in list(line)])

    return output


def int_or_null(value):
    try:
        int(value)
        return int(value)
    except ValueError:
        return None
