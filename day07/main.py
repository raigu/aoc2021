import sys


def part2(data):
    min = sys.maxsize
    for e in range(len(data)):
        fuel = 0
        for b in range(len(data)):
            step = abs(e-data[b])
            fuel += step * (step + 1) // 2
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

