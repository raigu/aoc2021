import sys


def part2_risk(y, x, space) -> int:
    """
    >>> part2_risk(8, 8, [[8]])
    6
    >>> part2_risk(2, 2, [[8]])
    3
    >>> part2_risk(1, 1, [[8]])
    1
    >>> part2_risk(0, 0, [[9]])
    9
    >>> part2_risk(1, 1, [[9]])
    2
    >>> part2_risk(0, 1, [[9]])
    1
    >>> part2_risk(1, 1, [[1]])
    3
    >>> part2_risk(1, 0, [[1]])
    2
    >>> part2_risk(0, 1, [[1]])
    2
    >>> part2_risk(0, 0, [[1]])
    1
    """
    ny = y % len(space)
    nx = x % len(space[0])

    dy = y // len(space)
    dx = x // len(space[0])

    point = space[ny][nx] + dx + dy
    if point > 9:
        point = point % 9

    return point


def my_min(y, x, shortest) -> int:
    if y + 1 < len(shortest):
        down = shortest[y + 1][x]
    else:
        down = sys.maxsize

    if x + 1 < len(shortest[0]):
        right = shortest[y][x + 1]
    else:
        right = sys.maxsize

    m = min(right, down)
    if m == sys.maxsize:
        m = 0

    return m


def part1_risk(y, x, space):
    return space[y][x]


def solution(space, my, mx, risk) -> int:
    shortest = [] * my
    for y in range(my):
        shortest.append([0] * mx)

    y = my
    while y > 0:
        y -= 1
        x = mx
        while x > y:
            x -= 1
            shortest[y][x] = risk(y, x, space) + my_min(y, x, shortest)
            if x != y:
                shortest[x][y] = risk(x, y, space) + my_min(x, y, shortest)

    return shortest[0][0] - space[0][0]


if __name__ == '__main__':
    space = []
    with open('input') as f:
        lines = [line.strip() for line in f.readlines()]
        for line in lines:
            space.append(list(int(c) for c in line))

    p1 = solution(space, len(space), len(space[0]), part1_risk)
    print(f'Part1: {p1}')

    # 2851 :(
    p2 = solution(space, len(space) * 5, len(space[0]) * 5, part2_risk)
    print(f'Part1: {p2}')
