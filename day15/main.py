import sys


def part2_risk2(point, y, x, ny, nx):
    dy = y // ny
    dx = x // nx

    point = space[y % ny][x % nx] + dx + dy
    if point > 9:
        point = point % 9

    return point

def part2_risk(y, x, space) -> int:
    """
    >>> part2_risk(1, 8, [[9,2]])
    5
    >>> part2_risk(4, 1, [[9,2]])
    6
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


def next_min_risk(y, x, shortest) -> int:
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

cache = {}
def solution(y, x, space, my, mx, risk) -> int:
    key = (y, x)
    ret = cache.get(key, None)

    if ret is None:
        if y + 1 == my and x + 1 == mx:
            ret = risk(y, x, space)
        else:
            candidates = []
            if y + 1 < my:
                candidates.append(solution(y+1, x, space, my, mx, risk))
            if x + 1 < mx:
                candidates.append(solution(y, x+1, space, my, mx, risk))

            ret = risk(y, x, space)+min(candidates)

            #print(y,x, ret)

        cache[y,x] = ret

    return ret



if __name__ == '__main__':
    space = []
    with open('input') as f:
        lines = [line.strip() for line in f.readlines()]
        for line in lines:
            space.append(list(int(c) for c in line))

    p1 = solution(0, 0, space, len(space), len(space[0]), part1_risk) - space[0][0]
    print(f'Part1: {p1}')

    # 2851 :(
    # 2845 :(
    cache = {}
    p2 = solution(0, 0, space, len(space) * 5, len(space[0]) * 5, part2_risk)
    print(f'Part2: {p2}')
