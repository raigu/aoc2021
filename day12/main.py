
def to_end(start, points, visited) -> list:
    ret = []

    if start == 'end':
        return [['end']]

    if start in points:
        neighbours = points[start]
    else:
        neighbours = [start]  # last, go back
    for n in neighbours:
        if n == 'start':
            continue  # Do not visit start again
        if (start, n) not in visited:  # avoid loops
            if n[0] >= 'a':  # big cave
                done = False
                for (s, e) in visited:
                    if e == n:
                        done = True
                        break
                if done:
                    continue  # skip looking to subpathes

            next_visited = set(visited)
            next_visited.add((start, n))
            for a in to_end(n, points, next_visited):
                ret.append([start] + a)

    return ret


def to_end2(start, points, visited) -> list:
    ret = []

    if start == 'end':
        return [['end']]

    if start in points:
        neighbours = points[start]
    else:
        neighbours = [start]  # last, go back

    for n in neighbours:
        if n == 'start':
            continue  # Do not visit start again

        # if next is small - make sure the max 2 small limit is exceeded already
        if n[0] >= 'a' and n != 'end' and n in visited:
            smalls = {}
            for c in visited:
                if not c[0] >= 'a':  # big cave
                    continue
                if c not in smalls:
                    smalls[c] = 0
                smalls[c] += 1

            if len(smalls) < sum(smalls.values()):
                continue
        else:
            # big cave. Make sure there is no looping
            i = 0
            loop = False
            while i < len(visited) - 1 and not loop:
                if start == visited[i] and n == visited[i + 1] and not start[0] >= 'a':
                    loop = True
                else:
                    i += 1
            if loop:
                continue

        next_visited = list(visited)
        next_visited.append(start)
        for a in to_end2(n, points, next_visited):
            ret.append([start] + a)

    return ret


def part1(data):
    pathes = to_end('start', data, set())

    return len(pathes)


def is_small(point) -> bool:
    return point[0] >= 'a' and point != 'start' and 'point' != 'end'


def incorrect(data):
    """
    >>> incorrect(['a','a', 'b', 'b'])
    True
    >>> incorrect(['a','a'])
    False
    """

    smalls = {}
    for c in data:
        if is_small(c):
            if c not in smalls:
                smalls[c] = 0
            smalls[c] += 1

    return len(smalls)+1 < sum(smalls.values())


def part2(data):
    pathes = to_end2('start', data, set())

    unique = set()
    for p in pathes:
        if not incorrect(p):
            unique.add(','.join(p))

    return len(unique)


if __name__ == '__main__':
    points = dict()
    with open('input') as f:
        for line in [line.strip() for line in f.readlines()]:
            (b, e) = line.strip().split('-')
            ends = points.get(b, [])
            ends.append(e)
            points[b] = ends

    # points by other direction
    next = dict(points)
    for p in points:
        for e in points[p]:
            ends = next.get(e, [])
            if p not in ends:
                ends.append(p)
                next[e] = ends

    points = dict(next)

    print(f'Part1: {part1(points)}')
    print(f'Part2: {part2(points)}')
