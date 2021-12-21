from collections import defaultdict
from functools import cache
from itertools import product


def part1(position1, points1, position2, points2):
    dice = 1
    i = 0
    turn = 0
    player = [[position1, points1], [position2, points2]]
    while player[0][1] < 1000 and player[1][1] < 1000:
        points = 3 * dice + 1 + 2

        player[turn][0] = (player[turn][0] + points - 1) % 10 + 1
        player[turn][1] += player[turn][0]

        turn = (turn + 1) % 2
        dice = (dice + 3 - 1) % 100 + 1
        i += 1

    return min(player[0][1], player[1][1]) * (i * 3)

@cache
def part2(position1, points1, position2, points2, turn):

    if points1 >= 21:
        return [1, 0]
    elif points2 >= 21:
        return [0, 1]
    else:
        ret = [0, 0]

        grouping = defaultdict(int)
        for combination in product([1, 2, 3], repeat=3):
            grouping[sum(combination)] += 1

        for points, count in grouping.items():
            player = [[position1, points1], [position2, points2]]
            player[turn][0] = (player[turn][0] + points - 1) % 10 + 1
            player[turn][1] += player[turn][0]

            [win1, win2] = part2(player[0][0], player[0][1], player[1][0], player[1][1], (turn + 1) % 2)

            ret[0] += count*win1
            ret[1] += count*win2

        return ret


if __name__ == '__main__':
    position1 = 5
    position2 = 10

    print(f'Part1: {part1(position1, 0, position2, 0)}')

    part2 = max(part2(position1, 0, position2, 0, 0))
    print(f'Part2: {part2}')
