def get_input_raw(day, year, is_sample):
    if is_sample:
        filename = f"../../../inputs/{year}/day{day}/sample.txt"
    else:
        filename = f"../../../inputs/{year}/day{day}/input.txt"

    with open(filename) as file:
        return file.read()


def get_input(day, year, is_sample):
    return get_input_raw(day, year, is_sample).splitlines()


def get_input_as_numbers(day, year, is_sample):
    return [int_or_null(x) for x in get_input(day, year, is_sample)]


def int_or_null(value):
    try:
        int(value)
        return int(value)
    except ValueError:
        return None
