from queue import PriorityQueue, SimpleQueue

if __name__ == '__main__':
    print("Day 24")

    with open('input') as f:
        lines = [line.strip() for line in f.readlines()]

    i = 0
    parts = []
    params = []
    while i < len(lines):
        #print(i)
        a = lines[i + 4]
        b = lines[i + 5]
        c = lines[i + 15]

        # print(a,b,c)

        a = int(a.split(' ')[2])
        b = int(b.split(' ')[2])
        c = int(c.split(' ')[2])

        part = lines[i:i + 18]
        part[4] = 'div z #'
        part[5] = 'add x #'
        part[15] = 'add y #'
        parts.append(part)

        # print(a,b,c)
        params.append([a, b, c])

        i += 18

    print(params)

    def calc(number, invariant=26):
        # reverse engineered from input
        z = 0
        for i in range(len(number)):
            a, b, c = params[i]
            w = int(number[i])
            x = 1 if ((z % 26) + b) != w else 0
            z = (z // a) * ((25 * x) + 1) + (w + c) * x

            if z > invariant:
                return -1
        return z


    queue = PriorityQueue()


    for i in range(9):
        queue.put((-9 * 10 ** 13, str(9-i)))

    found = False
    counter = 0
    invariant = 10000000
    while not found and not queue.empty():
        x, prefix = queue.get()

        counter += 1
        if counter % 10000 == 0:
            print(prefix,'...')

        for i in range(9):
            number = prefix + str(9-i)
            z = calc(number, invariant)
            if z == 0 and len(number) == 14:
                found = True
                break

            if z != -1:   # with this beginning the invariants are met.
                if len(number) < 14:
                    queue.put((-int(number) * 10 ** (14-len(number)), number))

    if found:
        print("Found part 1", number)
    else:
        print("did not found :(. Invariant:", invariant)


    queue = PriorityQueue()

    for i in range(9):
        queue.put((9 * 10 ** 13, str(9 - i)))

    found = False
    counter = 0
    invariant = 1200000
    while not found and not queue.empty():
        x, prefix = queue.get()

        counter += 1
        if counter % 100000 == 0:
            print(prefix, invariant, '...')

        for i in range(9):
            number = prefix + str(9 - i)
            z = calc(number, invariant)
            if z == 0 and len(number) == 14:
                found = True
                break

            if z != -1:  # with this beginning the invariants are met:
                if len(number) < 14:
                    queue.put((int(number) * 10 ** (14 - len(number)), number))

    if found:
        print("Found part2", number)
    else:
        print("did not found :(. Invariant:", invariant)

