def main(lines):
    counter = 0

    bits = []
    for line in lines:
        for i in range(len(line.strip())):
            if i + 1 > len(bits):
                bits.append(0)

            if line[i] == '1':
                bits[i] += 1
        counter += 1

    print(counter)
    print(bits)

    gamma = []
    beta = []

    for b in bits:
        if b > counter / 2:
            beta.append(0)
            gamma.append(1)
        else:
            beta.append(1)
            gamma.append(0)

    print(gamma)
    print(beta)

    g = 0
    for d in gamma:
        g = g * 2 + d

    b = 0
    for d in beta:
        b = b * 2 + d

    print(g)
    print(b)

    return g * b


if __name__ == '__main__':
    with open('input') as f:
        lines = f.readlines()
    print('Answer', main(lines))
