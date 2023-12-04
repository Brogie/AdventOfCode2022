import time
import math
from input_formatter import get_deliminated_input, int_or_null

timings = []


def get_numbers(string_to_split):
    return [int_or_null(x) for x in string_to_split.split()]


def get_card_scores(cards):
    card_scores = []
    card_wins = []
    for card in cards:
        matches = 0
        winning_numbers = get_numbers(card[0])
        card_numbers = get_numbers(card[1])

        for number in winning_numbers:
            if card_numbers.__contains__(number): matches += 1

        card_wins.append(matches)
        if matches > 0:
            card_scores.append(math.trunc(pow(2, matches - 1)))
        else:
            card_scores.append(0)

    return card_scores, card_wins


def part1(is_sample):
    cards = get_deliminated_input(4, 2023, is_sample, ' | ', r'Card \d:\s+')
    card_scores, card_wins = get_card_scores(cards)

    return sum(card_scores)


def part2(is_sample):
    cards = get_deliminated_input(4, 2023, is_sample, ' | ', r'Card \d:\s+')
    card_scores, card_wins = get_card_scores(cards)
    card_amounts = [1]*len(card_wins)

    for i in range(len(card_wins)):
        for j in range(card_wins[i]):
            card_amounts[i + j + 1] = card_amounts[i + j + 1] + card_amounts[i]

    return sum(card_amounts)


if __name__ == '__main__':
    print(part1(False))
    print(part2(False))
else:
    start = time.time()
    for _ in range(100):
        ans = part1(False)
    end = time.time()
    timings.append(["Day 4", "Part 1", ans, (end - start) / 100])

    start = time.time()
    for _ in range(100):
        ans = part2(False)
    end = time.time()
    timings.append(["Day 4", "Part 2", ans, (end - start) / 100])
