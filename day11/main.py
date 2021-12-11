from day11.point import Point

if __name__ == '__main__':
    print('Day 11')

    with open('input') as f:
        matrix = {}
        for y, line in enumerate([line.strip() for line in f.readlines()]):
            for x, c in enumerate(line.strip()):
                point = Point(x,y)
                matrix[point] = int(c)

    next = {}
    flashes = 0
    part1 = 0
    part2 = -1
    i = 0
    while part2 == -1:
        i = i+1
        for p in matrix:
            next[p] = matrix[p] + 1

        # flashing
        any = True
        flashed = []
        while any:
            any = False
            for n in next:
                if next[n] > 9:
                    any = True
                    next[n] = 0

                    if n not in flashed:
                        flashed.append(n)
                        flashes += 1

                        for j in n.neighbors():
                            if 0 <= j._coordinates[0] < 10 and 0 <= j._coordinates[1] < 10:
                                if j not in flashed:
                                    next[j] += 1

        if len(matrix) == len(flashed):
            part2 = i

        if i == 100:
            part1 = flashes

        matrix = dict(next)


    print(f'Part1: {part1}')
    print(f'Part2: {part2}')

