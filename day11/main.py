from day11.point import Point

if __name__ == '__main__':
    print('Day 11')

    with open('input') as f:
        matrix = {}
        for y, line in enumerate([line.strip() for line in f.readlines()]):
            for x, c in enumerate(line.strip()):
                matrix[Point(x,y)] = int(c)

    flashes = 0
    part1 = 0
    part2 = -1
    i = 0
    while part2 == -1:
        i = i+1

        # step increase
        for p in matrix:
            matrix[p] += 1

        # flashing
        any = True # true means someone flashed and increased neighbours energy level
        flashed = []
        while any:
            any = False
            for p in matrix:
                if matrix[p] > 9: # FLASH!
                    any = True
                    matrix[p] = 0

                    if p not in flashed: # only once can flash in one step
                        flashed.append(p)
                        flashes += 1

                        # radiate energy to non-flashed neighbours
                        for n in p.neighbors():
                            if 0 <= n._coordinates[0] < 10 and 0 <= n._coordinates[1] < 10:
                                if n not in flashed:
                                    matrix[n] += 1

        if len(matrix) == len(flashed):
            part2 = i

        if i == 100:
            part1 = flashes


    print(f'Part1: {part1}')
    print(f'Part2: {part2}')

