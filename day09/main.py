
def part1(data):
    lows = []
    r = len(data)
    c = len(data[0])
    for i in range(r):
        for j in range(c):
            up = (j == 0) or (data[i][j-1] > data[i][j])
            down = (j == c - 1) or (data[i][j+1] > data[i][j])
            left = (i == 0) or (data[i-1][j] > data[i][j])
            right = (i == r-1) or (data[i+1][j] > data[i][j])

            if up and down and left and right:
                print(i, j, data[i][j])
                lows.append(data[i][j])

    return sum([l+1 for l in lows])


def find_basin(x, y, data):
    """
    >>> find_basin(0, 0, [[0]])
    {(0, 0)}
    >>> find_basin(0, 0, [[0,1]])
    {(0, 1), (0, 0)}
    >>> find_basin(0, 1, [[0,1]])
    {(0, 1)}
    >>> find_basin(0, 0, [[9]])
    set()
    """
    r = len(data)
    c = len(data[0])

    ret = set()

    if data[x][y] == 9:
        return ret

    ret.add((x,y))

    # up
    i = x
    while i > 0 and data[i-1][y] > data[i][y]:
        ret |= find_basin(i-1, y, data)
        i -= 1

    # down
    i = x
    while i < r-1 and data[i+1][y] > data[i][y]:
        ret |= find_basin(i+1, y, data)
        i += 1

    # left
    j = y
    while j > 0 and data[x][j-1] > data[x][j]:
        ret |= find_basin(x, j-1, data)
        j -= 1

    # right
    j = y
    while j < c - 1 and data[x][j+1] > data[x][j]:
        ret |= find_basin(x, j+1, data)
        j += 1

    return ret

def part2(data):
    basins = []

    r = len(data)
    c = len(data[0])
    u = 0
    for i in range(r):
        for j in range(c):
            basin = find_basin(i, j, data)
            basins.append(len(basin))

    basins = sorted(basins, reverse=True)

    return basins[0] * basins[1] * basins[2]


if __name__ == '__main__':
    matrix = []
    with open('input') as f:
        for line in f.readlines():
            matrix.append([int(c) for c in line.strip()])

    #print(matrix)

    print(f'Part1: {part1(matrix)}')
    print(f'Part2: {part2(matrix)}')

