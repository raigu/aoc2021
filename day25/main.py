
def print_cucumbers(cucumbers, rows, cols):
    for y in range(rows):
        line = []
        for x in range(cols):
            if (y, x) in cucumbers:
                c = cucumbers[(y, x)]
            else:
                c = '.'
            line.append(c)
        print(''.join(line))


if __name__ == '__main__':
    floor = []
    with open('input') as f:
        lines = [line.strip() for line in f.readlines()]

    cucumbers = {}
    rows = 0
    cols = 0
    for line in lines:
        rows += 1
        cols = 0
        for cols, cucumber in enumerate(line):
            if cucumber in ['>', 'v']:
                cucumbers[(rows - 1, cols)] = cucumber
    cols += 1

    any = True
    steps = 0
    while any:
        # print(steps)
        # print_cucumbers(cucumbers, rows, cols)
        next = {}
        any = False

        # east
        for p, cucumber in cucumbers.items():
            if cucumber != '.':
                if cucumber == '>':
                    y = p[0]
                    x = (p[1] + 1) % cols
                    if (y, x) not in cucumbers:
                        any = True
                        next[(y, x)] = cucumber
                        continue
                next[p] = cucumber

        cucumbers = next

        # south
        next1 = {}
        for p, cucumber in next.items():
            if cucumber != '.':
                if cucumber == 'v':
                    y = (p[0] + 1) % rows
                    x = p[1]
                    if (y, x) not in cucumbers:
                        any = True
                        next1[(y, x)] = cucumber
                        continue
                next1[p] = cucumber

        cucumbers = next1
        steps += 1

    print('Day 25')
    print(f'Part1: {steps}')
    print(f'Part2: RTFI')
