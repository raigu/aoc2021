
if __name__ == '__main__':
    with open('input') as f:
        lines = f.readlines()

    h = 0
    depth = 0
    aim = 0

    for line in lines:
        p = line.split(' ')
        d = p[0]
        i = int(p[1])
        if d == 'down':
            aim = aim + i
        elif d == 'up':
            aim = aim - i
        elif d == 'forward':
            h = h + i
            depth = depth + aim * i
        else:
            raise Exception(f'Unknown operation {d}')

        print("---")
        print((h, depth, aim))

    print(h)
    print(depth)
    print(h*depth)



