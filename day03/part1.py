def patterns(lines):
    bits = []
    answer = 0
    for line in lines:
        for i in range(len(line.strip())):
            if i+1 > len(bits):
                bits.append(0)

            if line[i] == '1':
                bits[i] += 1
        answer += 1

    gamma = []
    beta = []

    for b in bits:
        if b >= answer / 2:
            beta.append(0)
            gamma.append(1)
        else:
            beta.append(1)
            gamma.append(0)

    return (gamma, beta)

def main(lines):

    (gamma, beta) = patterns(lines)

    g = 0
    for d in gamma:
        g = g*2 + d

    b = 0
    for d in beta:
        b = b * 2 + d

    print(g)
    print(b)

    lines = [line.strip() for line in lines]

    print("----")
    ox = lines
    co2 = lines
    n = len(gamma)
    for i in range(n):  # positions
        if len(ox) > 1:
            (gamma, beta) = patterns(ox)
            nox = []
            for line in ox:
                if int(line[i]) == gamma[i]:
                    nox.append(line)
            ox = nox

        if len(co2) > 1:
            (gamma, beta) = patterns(co2)
            print(beta)
            nox = []
            for line in co2:
                if int(line[i]) == beta[i]:
                    nox.append(line)
            co2 = nox

            print(i, co2)

    print(ox)
    print(co2)

    g = 0
    for d in ox[0]:
        g = g * 2 + int(d)

    b = 0
    for d in co2[0]:
        b = b * 2 + int(d)

    print(g,b)

    return g * b


if __name__ == '__main__':
    with open('input') as f:
        lines = f.readlines()
    print('Answer', main(lines))
