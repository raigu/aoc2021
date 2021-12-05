from day05.grid import Grid, Direction
from day05.point import Point


if __name__ == '__main__':
    with open('input') as f:
        lines = f.readlines()

    lines_of_vents = []
    for line in lines:
        (b, e) = line.split(' -> ')
        b = Point(*map(int, b.split(',')))
        e = Point(*map(int, e.split(',')))

        lines_of_vents.append([b, e])

    part1 = Grid()
    part1.add_lines(lines_of_vents, {Direction.HORIZONTAL, Direction.VERTICAL})
    print('Part 1: ', part1.number_of_intersecting_points())

    part2 = Grid()
    part2.add_lines(lines_of_vents, {Direction.HORIZONTAL, Direction.VERTICAL, Direction.DIAGONAL})
    print('Part 2: ', part2.number_of_intersecting_points())
