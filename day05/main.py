from day05.point import Point
from day05.grid import Grid

def part1(line_of_vents):
    answer = 0

    grid = Grid()
    for (b, e) in line_of_vents:
        if b[0] == e[0]:
            for y in range(min(b[1], e[1]), max(b[1], e[1]) + 1):
                grid.add(Point(b[0], y))

        if b[1] == e[1]:
            for x in range(min(b[0], e[0]), max(b[0], e[0]) + 1):
                grid.add(Point(x, b[1]))

    for point in grid.points():
        if grid[point] > 1:
            answer += 1
    return answer


def part2(line_of_vents):
    answer = 0

    grid = Grid()
    for b,e in line_of_vents:
        if b[0] == e[0]:
            for y in range(min(b[1], e[1]), max(b[1], e[1])+1):
                grid.add(Point(b[0], y))

        if b[1] == e[1]:
            for x in range(min(b[0], e[0]), max(b[0], e[0])+1):
                grid.add(Point(x, b[1]))

        if abs(b[0] - e[0]) == abs(b[1] - e[1]):
            r = range(0, abs(b[0] - e[0])+1)
            xsign = 1 if b[0] < e[0] else -1
            ysign = 1 if b[1] < e[1] else -1

            for i in r:
                grid.add(Point(b[0] + xsign * i, b[1] + ysign * i))

    for point in grid.points():
        if grid[point] > 1:
            answer += 1
    return answer


if __name__ == '__main__':
    with open('input') as f:
        lines = f.readlines()

    lines_of_vents = []
    for line in lines:
        (b, e) = line.split(' -> ')
        b = b.split(',')
        b = Point(int(b[0]), int(b[1]))

        e = e.split(',')
        e = Point(int(e[0]), int(e[1]))

        lines_of_vents.append([b,e])

    print('Part 1: ', part1(lines_of_vents))
    print('Part 2: ', part2(lines_of_vents))
