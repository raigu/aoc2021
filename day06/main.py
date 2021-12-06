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
    answer = 0

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
    new = {}
    for fish in data:
        count = new.get(fish, 0)
        new[fish] = count + 1

    for day in range(days):
        fishes = dict(new)
        new = {}
        for fish in fishes:
            count = fishes[fish]
            fish -= 1
            if fish < 0:
                fish = 6
                new[8] = new.get(8, 0) + count

            new[fish] = new.get(fish, 0) + count

    return sum(new.values())


if __name__ == '__main__':
    with open('input') as f:
        line = f.readline().strip()

    i = list(map(int, line.split(',')))
    print('Part 1: ', part1(i, 80))
    print('Part 2: ', part2(i, 256))
