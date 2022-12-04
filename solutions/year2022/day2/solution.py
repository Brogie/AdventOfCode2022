import time
from input_formatter import get_deliminated_input, get_input

timings = []


def play_game(player1, player2):
    if (player1 == "A" and player2 == "Z") or \
       (player1 == "B" and player2 == "X") or \
       (player1 == "C" and player2 == "Y"):
        return 0
    elif (player1 == "A" and player2 == "X") or \
         (player1 == "B" and player2 == "Y") or \
         (player1 == "C" and player2 == "Z"):
        return 3
    return 6


def play_game_new_rules(player1, player2):
    if player1 == "A" and player2 == "X":
        return 3
    if player1 == "B" and player2 == "X":
        return 1
    if player1 == "C" and player2 == "X":
        return 2
    if player1 == "A" and player2 == "Y":
        return 4
    if player1 == "B" and player2 == "Y":
        return 5
    if player1 == "C" and player2 == "Y":
        return 6
    if player1 == "A" and player2 == "Z":
        return 8
    if player1 == "B" and player2 == "Z":
        return 9
    if player1 == "C" and player2 == "Z":
        return 7


def play_game_new_rules_2(game):
    match game:
        case "A X": return 3
        case "B X": return 1
        case "C X": return 2
        case "A Y": return 4
        case "B Y": return 5
        case "C Y": return 6
        case "A Z": return 8
        case "B Z": return 9
        case "C Z": return 7


def part1(is_sample):
    data = get_deliminated_input(2, 2022, is_sample, " ")
    score = 0

    for game in data:
        score += (ord(game[1]) - 87) + play_game(game[0], game[1])

    return score


def part2(is_sample):
    data = get_deliminated_input(2, 2022, is_sample, " ")
    score = 0

    for game in data:
        score += play_game_new_rules(game[0], game[1])

    return score


def part2_cleaner(is_sample):
    data = get_input(2, 2022, is_sample)
    score = 0

    for game in data:
        score += play_game_new_rules_2(game)

    return score


if __name__ == '__main__':
    print(part1(False))
    print(part2(False))
    print(part2_cleaner(False))
else:
    start = time.time()
    for _ in range(100):
        ans = part1(False)
    end = time.time()
    timings.append(["Day 2", "Part 1", ans, (end - start) / 100])

    start = time.time()
    for _ in range(100):
        ans = part2(False)
    end = time.time()
    timings.append(["Day 2", "Part 2", ans, (end - start) / 100])

    start = time.time()
    for _ in range(100):
        ans = part2_cleaner(False)
    end = time.time()
    timings.append(["Day 2", "Part 2 (Refined)", ans, (end - start) / 100])
