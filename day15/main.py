import sys
from collections import defaultdict


def part1_risk(n, space):
    (y, x) = n
    return space[y][x]


def part2_risk(n, space) -> int:
    """
    >>> part2_risk((1, 8), [[9,2]])
    5
    >>> part2_risk((4, 1), [[9,2]])
    6
    >>> part2_risk((8, 8), [[8]])
    6
    >>> part2_risk((2, 2), [[8]])
    3
    >>> part2_risk((1, 1), [[8]])
    1
    >>> part2_risk((0, 0), [[9]])
    9
    >>> part2_risk((1, 1), [[9]])
    2
    >>> part2_risk((0, 1), [[9]])
    1
    >>> part2_risk((1, 1), [[1]])
    3
    >>> part2_risk((1, 0), [[1]])
    2
    >>> part2_risk((0, 1), [[1]])
    2
    >>> part2_risk((0, 0), [[1]])
    1
    """
    y, x = n

    ny = y % len(space)
    nx = x % len(space[0])

    dy = y // len(space)
    dx = x // len(space[0])

    point = space[ny][nx] + dx + dy
    if point > 9:
        point = point % 9

    return point


def neighbours(p: tuple, size_y, size_x):
    (y, x) = p
    for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < size_y and 0 <= nx < size_x:
            yield ny, nx


def solution(y, x, space, size_y, size_x, edge) -> int:
    s = (y, x)  # start
    distances = defaultdict(lambda: sys.maxsize)

    distances[s] = 0  # distance from start to start is known
    queue = {s}
    while len(queue):

        # let's take next shortest node to continue
        v = None
        d = sys.maxsize
        for e in queue:
            if distances[e] < d:
                v = e
                d = distances[e]
        queue.remove(v)

        for n in neighbours(v, size_y, size_x):
            if distances[n] > distances[v] + edge(n, space):
                distances[n] = distances[v] + edge(n, space)
                # We found shorter path for node n
                # This also affects the n's neighbours.
                # Let's add n to queue for processing its neighbours later.
                if n not in queue:
                    queue.add(n)

    return distances[(size_y - 1, size_x - 1)]


if __name__ == '__main__':
    space = []
    with open('input') as f:
        lines = [line.strip() for line in f.readlines()]
        for line in lines:
            space.append(list(int(c) for c in line))

    p1 = solution(0, 0, space, len(space), len(space[0]), part1_risk)
    print(f'Part1: {p1}')

    p2 = solution(0, 0, space, len(space) * 5, len(space[0]) * 5, part2_risk)
    print(f'Part2: {p2}')
