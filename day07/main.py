import sys


def consumption(b, e):
    """
    >>> consumption(16,5)
    66
    >>> consumption(14, 5)
    45
    """
    r = 0
    for i in range(abs(e - b)):
        r += i + 1
    return r


def part2(data):
    min = sys.maxsize
    for e in range(len(data)):
        fuel = 0
        for b in range(len(data)):
            fuel += consumption(data[b], e)
        if fuel < min:
            min = fuel
    return min


def part1(data):
    min = sys.maxsize
    for e in range(len(data)):
        fuel = 0
        for b in range(len(data)):
            fuel += abs(data[e] - data[b])
        if fuel < min:
            min = fuel
    return min


if __name__ == '__main__':
    with open('input') as f:
        lines = [int(line.strip()) for line in f.readline().split(',')]

    print(f'Part1: {part1(lines)}')
    print(f'Part2: {part2(lines)}')

