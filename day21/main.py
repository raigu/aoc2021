import copy
from collections import defaultdict
from itertools import product


def part1(position1, points1, position2, points2):
    dice = 1
    i = 0
    while points1 < 1000 and points2 < 1000:
        points = 3 * dice + 1 + 2
        print('Round: ', i + 1, 'dice: ', dice, 'points:', points)

        if i % 2 == 0:
            position1 = (position1 + points-1) % 10 + 1
            points1 += position1
            print('Player1 ', position1, points1)
        else:
            position2 = (position2 + points-1) % 10 + 1
            while position2 > 10:
                position2 -= 10
            points2 += position2
            print('Player2 ', position2, points2)

        dice = (dice + 3 - 1) % 100 + 1

        i += 1

    print('END: ', points1, points2)

    return min(points1, points2) * (i * 3)


def part2(player, turn):
    if player[0][1] >= 21:
        return [1, 0]
    elif player[1][1] >= 21:
        return [0, 1]
    else:
        ret = [0, 0]
        points = defaultdict(int)
        for combination in product([1, 2, 3], repeat=3):
            points[sum(combination)] += 1

        for points, count in points.items():
            parallel_player = copy.deepcopy(player)
            parallel_player[turn][0] = (parallel_player[turn][0] + points - 1) % 10 + 1
            parallel_player[turn][1] += parallel_player[turn][0]

            [win1, win2] = part2(parallel_player, (turn + 1) % 2)

            ret[0] += win1 * count
            ret[1] += win2 * count

        return ret


if __name__ == '__main__':
    with open('input1') as f:
        lines = [line.strip() for line in f.readlines()]

    position1 = 4
    position2 = 8

    # position1 = 5
    # position2 = 10

    # print(f'Part1: {part1(position1, 0, position2, 0)}')
    print(f'Part2: {part2([[position1, 0], [position2, 0]], 0)}')
