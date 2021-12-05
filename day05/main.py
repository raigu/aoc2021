def part1(data):
    answer = 0

    # Solution here

    grid = {}

    for line in data:
        (b, e) = line.split(' -> ')
        b = b.split(',')

        b = [int(b[0]), int(b[1])]

        e = e.split(',')
        e = [int(e[0]), int(e[1])]

        points = []
        if b[0] == e[0]:
            for y in range(min(b[1], e[1]) + 1, max(b[1], e[1])):
                points.append([b[0], y])

        if b[1] == e[1]:
            for x in range(min(b[0], e[0]) + 1, max(b[0], e[0])):
                points.append([x, b[1]])

        if len(points) > 0:
            if b not in points:
                points.append(b)
            if e not in points:
                points.append(e)

        for point in points:
            key = f"{point[0]},{point[1]}"
            if key not in grid:
                grid[key] = 1
            else:
                grid[key] += 1

    for v in grid.values():
        if v > 1:
            answer += 1
    return answer


def part2(data):
    answer = 0

    # Solution here

    grid = {}

    for line in data:
        (b, e) = line.split(' -> ')
        b = b.split(',')

        b = [int(b[0]), int(b[1])]

        e = e.split(',')
        e = [int(e[0]), int(e[1])]

        points = []
        if b[0] == e[0]:
            points.append(b)
            for y in range(min(b[1], e[1]) + 1, max(b[1], e[1])):
                points.append([b[0], y])
            points.append(e)

        if b[1] == e[1]:
            points.append(b)
            for x in range(min(b[0], e[0]) + 1, max(b[0], e[0])):
                points.append([x, b[1]])
            points.append(e)

        if abs(b[0] - e[0]) == abs(b[1] - e[1]):
            points.append(b)

            r = range(1, abs(b[0] - e[0]))
            xsign = 1 if b[0] < e[0] else -1
            ysign = 1 if b[1] < e[1] else -1

            for i in r:
                points.append([b[0] + xsign * i, b[1] + ysign * i])

            points.append(e)

        for point in points:
            key = f"{point[0]},{point[1]}"
            if key not in grid:
                grid[key] = 1
            else:
                grid[key] += 1

        # print(points)
        # print(grid)

    '''
    vs = grid.keys()
    sorted(vs)
    for k in vs:
        print(k, ":", grid[k])
    '''

    for v in grid.values():
        if v > 1:
            answer += 1
    return answer


if __name__ == '__main__':
    with open('input') as f:
        lines = f.readlines()
    print('Part 1: ', part1(lines))
    print('Part 2: ', part2(lines))
