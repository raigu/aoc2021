def part1(data,days):
    """
    >>> part1([3,4,3,1,2], 18)
    26
    >>> part1([3,4,3,1,2],80)
    5934
    >>> part1([3,4,3,1,2],256)
    26984457539
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


def part2(data):
    answer = 0

    # Solution here

    return answer


if __name__ == '__main__':
    with open('input') as f:
        line = f.readline().strip()

    print('Part 1: ', part1(map(int, line.split(',')), 80))
#    print('Part 2: ', part2(lines))
