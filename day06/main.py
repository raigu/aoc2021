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


def part2(fishes, days):
    """
    >>> part2([0], 7)
    2
    >>> part2([0], 6)
    2
    >>> part2([0], 8)
    3
    >>> part2([0], 1)
    2
    >>> part2([1], 1)
    1
    >>> part2([3,4,3,1,2], 1)
    5
    >>> part2([3,4,3,1,2], 2)
    6
    >>> part2([3,4,3,1,2], 8)
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

    answer = len(fishes)

    new = []
    for fish in fishes:
        new.append((fish, days))
    fishes = new

    while len(fishes):
        (fish, fish_days) = fishes.pop()
        while fish_days > fish:
            fish_days = fish_days - fish - 1
            fishes.append((8, fish_days))
            answer += 1
            fish = 6
    return answer


def part3(data, days):
    """
    >>> part3([3,4,3,1,2], 3)
    7
    >>> part3([0], 1)
    2
    >>> part3([3,4,3,1,2], 1)
    5
    >>> part3([0], 7)
    2
    >>> part3([0], 6)
    2
    >>> part3([0], 8)
    3
    >>> part3([1], 1)
    1
    >>> part3([3,4,3,1,2], 2)
    6
    >>> part3([3,4,3,1,2], 4)
    9
    >>> part3([3,4,3,1,2], 5)
    10
    >>> part3([3,4,3,1,2], 10)
    12
    >>> part3([3,4,3,1,2], 12)
    17
    >>> part3([3,4,3,1,2], 18)
    26
    >>> part3([3,4,3,1,2],80)
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
            if fish == 0:
                fish = 6
                a = new.get(8, 0)
                new[8] = a + count
            else:
                fish = fish - 1

            a = new.get(fish, 0)
            new[fish] = a + count

    return sum(new.values())


if __name__ == '__main__':
    with open('input') as f:
        line = f.readline().strip()

    '''
    fishes = [3,4,3,1,2]
    i = 0
    print('day', i)
    while part1(fishes, i) == part2(fishes,i):
        i += 1
        print('day', i)
    '''

    i = list(map(int, line.split(',')))
    print('Part 1: ', part1(i, 80))
    print('Part 2: ', part3(i, 256))
