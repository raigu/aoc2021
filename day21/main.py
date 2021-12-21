import copy
from itertools import product
from functools import cache


def part1(position1, points1, position2, points2):
    dice = 1
    i = 0
    while points1 < 1000 and points2 < 1000:
        points = 3 * dice + 1 + 2
        #print('Round: ', i + 1, 'dice: ', dice, 'points:', points)

        if i % 2 == 0:
            position1 = (position1 + points-1) % 10 + 1
            points1 += position1
            #print('Player1 ', position1, points1)
        else:
            position2 = (position2 + points-1) % 10 + 1
            points2 += position2
            #print('Player2 ', position2, points2)

        dice = (dice + 3 - 1) % 100 + 1

        i += 1

    return min(points1, points2) * (i * 3)

@cache
def part2(position1, points1, position2, points2, turn):

    if points1 >= 21:
        return [1, 0]
    elif points2 >= 21:
        return [0, 1]
    else:
        ret = [0, 0]
        for combination in product([1, 2, 3], repeat=3):
            points = sum(combination)
            player = [[position1, points1], [position2, points2]]
            player[turn][0] = (player[turn][0] + points - 1) % 10 + 1
            player[turn][1] += player[turn][0]

            [win1, win2] = part2(player[0][0], player[0][1], player[1][0], player[1][1], (turn + 1) % 2)

            ret[0] += win1
            ret[1] += win2

        return ret


if __name__ == '__main__':
    with open('input1') as f:
        lines = [line.strip() for line in f.readlines()]

    #position1 = 4
    #position2 = 8

    position1 = 5
    position2 = 10

    print(f'Part1: {part1(position1, 0, position2, 0)}')

    part2 = max(part2(position1, 0, position2, 0, 0))
    print(f'Part2: {part2}')
