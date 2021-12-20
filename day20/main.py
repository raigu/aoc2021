import sys
from copy import copy


def calc_index(y, x, image):
    digit = ''
    i = y - 1
    while i < y + 2:
        j = x - 1
        while j < x + 2:
            if (i, j) in image:
                digit += '1'
            else:
                digit += '0'
            j += 1
        i += 1

    return int(digit, 2)


def part1(image, algorithm, count):
    min_x, max_x = sys.maxsize, -sys.maxsize
    min_y, max_y = sys.maxsize, -sys.maxsize

    for p in image:
        if p[0] < min_y:
            min_y = p[0]
        if p[0] > max_y:
            max_y = p[0]

        if p[1] < min_x:
            min_x = p[1]
        if p[1] > max_x:
            max_x = p[1]

    min_x = min_x - 2*count - 1
    max_x = max_x + 2*count + 1
    min_y = min_y - 2*count - 1
    max_y = max_y + 2*count + 1

    for i in range(count):
        min_x += 1
        max_x -= 1
        min_y += 1
        max_y -= 1

        y = min_y
        next = set()
        while y <= max_y:
            x = min_x
            row = []
            while x <= max_x:
                index = calc_index(y, x, image)
                light = algorithm[index]
                if light == '#':
                    next.add((y, x))

                row.append(light)
                x += 1
            #print(''.join(row))
            y += 1

        image = copy(next)

    return len(image)


def part2(data):
    answer = 0

    for line in data:
        answer += 1

    return answer


if __name__ == '__main__':
    with open('input') as f:
        lines = [line.strip() for line in f.readlines()]

        algorithm = lines.pop(0).strip()
        lines.pop(0)
        image = set()
        for y, row in enumerate(lines):
            for x, light in enumerate(row.strip()):
                if light == '#':
                    image.add((y,x))

    print('Day 20')
    # 5673 -- too low
    # 5676
    # 5960 -- to high
    print(f'Part1: {part1(image, algorithm, 2)}')
    print(f'Part2: {part1(image, algorithm, 50)}')
