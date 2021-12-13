def fold(dots, instruction):
    """
    >>> fold({(2,2)}, ('x', 1))
    {(0, 2)}
    >>> fold({(0,2)}, ('y', 1))
    {(0, 0)}
    """
    next = set()
    if instruction[0] == 'x':
        for x, y in dots:
            if x > instruction[1]:
                next.add((instruction[1] - (x - instruction[1]), y))
            else:
                next.add((x, y))
    else:
        for x, y in dots:
            if y > instruction[1]:
                next.add((x, instruction[1] - (y - instruction[1])))
            else:
                next.add((x, y))

    return next


def output(points):
    max_x = max(x for x, y in points)
    max_y = max(y for x, y in points)

    for y in range(max_y+1):
        row = []
        for x in range(max_x+1):
            if (x, y) in points:
                row.append('#')
            else:
                row.append('.')
        print(''.join(row))


if __name__ == '__main__':
    with open('input') as f:
        lines = [line.strip() for line in f.readlines()]
        instructions = []
        dots = set()
        for line in lines:
            if line == '':
                continue

            if line.startswith('fold along'):
                (d, pos) = line[11:].split('=')
                instructions.append((d, int(pos)))
            else:
                x, y = line.split(',')
                dots.add((int(x), int(y)))

    print(dots)

    a = len(fold(dots, instructions[0]))

    print(f'Part1: {a}')

    for i in range(len(instructions)):
        dots = fold(dots, instructions[i])

    output(dots)
