from day05.grid import Grid
from day05.line import Direction, Line
from day05.point import Point

if __name__ == '__main__':
    with open('input') as f:
        lines = f.readlines()

    lines_of_vents = []
    for line in lines:
        (b, e) = line.split(' -> ')
        b = Point(*map(int, b.split(',')))
        e = Point(*map(int, e.split(',')))

        lines_of_vents.append(Line(b, e))

    part1 = Grid()
    suitable_directions = {Direction.HORIZONTAL, Direction.VERTICAL}
    for line in lines_of_vents:
        if line.direction() in suitable_directions:
            part1.add_line(line)

    print('Part 1: ', part1.number_of_intersecting_points())

    part2 = Grid()
    suitable_directions = {Direction.HORIZONTAL, Direction.VERTICAL, Direction.DIAGONAL}
    for line in lines_of_vents:
        if line.direction() in suitable_directions:
            part2.add_line(line)

    print('Part 2: ', part2.number_of_intersecting_points())
