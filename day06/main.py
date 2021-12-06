from collections import defaultdict


def part1(data,days):
    """
    >>> part1([0], 1)
    2
    >>> part1([0], 7)
    2
    >>> part1([0], 1)
    2
    >>> part1([1], 1)
    1
    >>> part1([3,4,3,1,2], 2)
    6
    >>> part1([3,4,3,1,2], 18)
    26
    >>> part1([3,4,3,1,2],80)
    5934
    """
    new = list(data)
    for day in range(days):
        fishes = list(new)
        new = []
        for fish in list(fishes):
            if fish == 0:
                fish = 6
                new.append(8)
            else:
                fish = fish - 1
            new.append(fish)

    return len(new)


def part2(data, days):
    """
    >>> part2([3,4,3,1,2], 3)
    7
    >>> part2([0], 1)
    2
    >>> part2([3,4,3,1,2], 1)
    5
    >>> part2([0], 7)
    2
    >>> part2([0], 6)
    2
    >>> part2([0], 8)
    3
    >>> part2([1], 1)
    1
    >>> part2([3,4,3,1,2], 2)
    6
    >>> part2([3,4,3,1,2], 4)
    9
    >>> part2([3,4,3,1,2], 5)
    10
    >>> part2([3,4,3,1,2], 10)
    12
    >>> part2([3,4,3,1,2], 12)
    17
    >>> part2([3,4,3,1,2], 18)
    26
    >>> part2([3,4,3,1,2],80)
    5934
    """
    next_day = defaultdict(int)
    for fish in data:
        next_day[fish] += 1

    for day in range(days):
        current_day = dict(next_day)
        next_day = defaultdict(int)
        for fish, count in current_day.items():
            fish -= 1
            if fish < 0:
                fish = 6
                next_day[8] += count
            next_day[fish] += count

    return sum(next_day.values())


if __name__ == '__main__':
    with open('input') as f:
        line = f.readline().strip()

    i = list(map(int, line.split(',')))
    print('Part 1: ', part1(i, 80))
    print('Part 2: ', part2(i, 256))
