from day11.point import Point


def part1(data):
    answer = 0

    for line in data:
        answer += 1

    return answer


def part2(data):
    answer = 0

    for line in data:
        answer += 1

    return answer

def print_matrix(m):
    o = []
    for y in range(10):
        o.append([-1]*10)

    for p in m:
        o[p._coordinates[1]][p._coordinates[0]] = str(m[p])

    for r in o:
        print("".join(r))

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
    part2 = 0
    for i in range(700):
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

        #print(i+1)
        #print_matrix(next)
        #print()

        if len(matrix) == len(flashed) and part2 == 0:
            part2 = i + 1

        matrix = dict(next)


    print(f'Part1: {flashes}')
    print(f'Part2: {part2}')

