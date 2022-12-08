import time
import numpy as np
from input_formatter import get_grid_as_numbers

timings = []


def check_tree_visibility(trees, found_trees):
    for y in range(len(trees)):
        lowest_tree = -1
        for x in range(len(trees)):
            if trees[x][y] > lowest_tree:
                found_trees[x][y] = True
                lowest_tree = trees[x][y]

# Abandon all hope this had to be restarted
# def calc_scenic(trees, x, y):
#     print(trees[x][y])
#     # top
#     top = 0
#     for scan in reversed(range(0, y)):
#         if trees[x][scan] >= trees[x][y]:
#             top = y - scan + 1
#             break
#
#     bottom = 0
#     for scan in range(y, len(trees)):
#         if trees[x][scan] >= trees[x][y]:
#             bottom = scan - y + 1
#             break
#
#     # left
#     left = 0
#     for scan in reversed(range(0, x)):
#         if trees[scan][y] >= trees[x][y]:
#             left = x - scan + 1
#             break
#
#     # right
#     right = 0
#     for scan in range(x + 1, len(trees)):
#         if trees[scan][y] >= trees[x][y]:
#             right = scan - x + 1
#             break
#
#     print(top, left, right, bottom)
#     return top * bottom * left * right


# I have won, but at what cost?
def calc_scenic(tree, x, y):
    right = 0
    for scan in range(1, len(tree) - x):
        right += 1
        if tree[y][x+scan] >= tree[y][x]:
            break

    left = 0
    for scan in range(x - 1, -1, -1):
        left += 1
        if tree[y][scan] >= tree[y][x]:
            break

    down = 0
    for scan in range(1, len(tree) - y):
        down += 1
        if tree[y + scan][x] >= tree[y][x]:
            break

    up = 0
    for scan in range(y - 1, -1, -1):
        up += 1
        if tree[scan][x] >= tree[y][x]:
            break

    return up * down * left * right


def part1(is_sample):
    trees = np.asarray(get_grid_as_numbers(8, 2022, is_sample))
    found_trees = np.zeros((len(trees), len(trees)), dtype=bool)

    check_tree_visibility(trees, found_trees)

    for _ in range(3):
        trees = np.rot90(trees)
        found_trees = np.rot90(found_trees)
        check_tree_visibility(trees, found_trees)

    return found_trees.sum()


def part2(is_sample):
    trees = get_grid_as_numbers(8, 2022, is_sample)
    top_scenic = 0

    # calc_scenic(trees, 2,3)
    for y in range(1, len(trees) - 1):
        for x in range(1, len(trees) - 1):
            scenic = calc_scenic(trees, x, y)
            if scenic > top_scenic:
                top_scenic = scenic

    return top_scenic


if __name__ == '__main__':
    print(part1(False))
    print(part2(False))
else:
    start = time.time()
    for _ in range(100):
        ans = part1(False)
    end = time.time()
    timings.append(["Day 8", "Part 1", ans, (end - start) / 100])

    start = time.time()
    for _ in range(100):
        ans = part2(False)
    end = time.time()
    timings.append(["Day 8", "Part 2", ans, (end - start) / 100])
