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


def next(p, v):
    x, y = p
    vx, vy = v

    x = x + vx
    y = y + vy
    if vx != 0:
        vx = vx + (-1 if vx > 0 else 1)

    vy = vy - 1

    return ((x, y), (vx, vy))


def reached(p, xt, yt):
    return xt[0] <= p[0] <= xt[1] and yt[0] <= p[1] <= yt[1]


def passes(p, v, xt, yt):
    x, y = p
    vx, vy = v

    if vx == 0:

        if not (xt[0] <= x <= xt[1]):  # fell pass it
            return True
        elif y < min(yt[0], yt[1]):  # fell under it
            return True

    return False


if __name__ == '__main__':

    xt = (88, 125)
    yt = (-157, -103)

    #xt = (20, 30)
    #yt = (-10, -5)

    max_y = -9999
    x_range = (0, 125)
    y_range = (0, 10000)
    for x in range(x_range[0], x_range[1]):
        for y in range(y_range[0], y_range[1]):
            p = (0, 0)
            v = (x, y)
            current_max_y = -9999
            while not reached(p, xt, yt) and not passes(p, v, xt, yt):
                p, v = next(p, v)
                if current_max_y < p[1]:
                    current_max_y = p[1]

            if reached(p, xt, yt):
                if max_y < current_max_y:
                    max_y = current_max_y
                print(f'({x},{y})', ' -> ', p, v, ':', current_max_y, max_y)

    # 12246
    print('Part1', max_y)
    print('end')
