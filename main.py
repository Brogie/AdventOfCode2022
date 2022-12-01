import sys
import settings
import requests
from pathlib import Path


def clear_lines(amount):
    for _ in range(amount):
        sys.stdout.write("\x1b[1A")  # cursor up one line
        sys.stdout.write("\x1b[2K")  # delete the last line


def validate():
    if len(sys.argv) != 2:
        print("Missing argument 'Day' eg: python main 12")
        exit()
    if sys.argv[1].isdigit() and 0 < int(sys.argv[1]) <= 25:
        settings.day = sys.argv[1]
    else:
        print("Incorrect argument 'Day': Must be a number between 1-25")
        exit()


def save_sample_file(day, year):
    Path(f"inputs").mkdir(exist_ok=True)
    Path(f"inputs/{year}").mkdir(exist_ok=True)
    Path(f"inputs/{year}/day{day}").mkdir(exist_ok=True)

    filename = f"inputs/{year}/day{day}/sample.txt"
    if not Path(filename).is_file():
        print("Enter sample data:")
        lines = []
        while True:
            line = input()
            if line:
                lines.append(line)
            else:
                clear_lines(len(lines) + 2)
                break
        sample_data = '\n'.join(lines)

        with open(filename, "w") as file:
            file.write(sample_data)
            print(f"├─ 🔽 Sample File: saved")
    else:
        print(f"├─ 💾 Sample File: in cache.")


def save_input_file(day, year, session):
    Path(f"inputs").mkdir(exist_ok=True)
    Path(f"inputs/{year}").mkdir(exist_ok=True)
    Path(f"inputs/{year}/day{day}").mkdir(exist_ok=True)

    filename = f"inputs/{year}/day{day}/input.txt"
    if not Path(filename).is_file():
        response = requests.get(
            f"https://adventofcode.com/{year}/day/{day}/input",
            cookies={"session": session})
        if not response.ok:
            if response.status_code == 404:
                raise FileNotFoundError(response.text)
            raise RuntimeError(f"Request failed, code: {response.status_code}, message: {response.content}")
        else:
            with open(filename, "w") as file:
                file.write(response.text[:-1])
                print(f"├─ 🔽 Input File : downloaded")
    else:
        print(f"├─ 💾 Input File : in cache.")


def generate_solution_file(day, year):
    Path(f"solutions").mkdir(exist_ok=True)
    Path(f"solutions/{year}").mkdir(exist_ok=True)
    Path(f"solutions/{year}/day{day}").mkdir(exist_ok=True)


if __name__ == '__main__':
    validate()

    print("│ Generating files for puzzle {}/{}".format(settings.day, settings.year))
    save_sample_file(settings.day, settings.year)
    save_input_file(settings.day, settings.year, settings.session)
    generate_solution_file(settings.day, settings.year)
