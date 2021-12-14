from collections import defaultdict


def part1(template, rules, steps=10):
    for i in range(steps):
        print(i + 1)
        next = ''
        for j in range(len(template) - 1):
            pair = template[j:j + 2]
            next = next + template[j] + rules[pair]
        next += template[-1]
        template = next

    return template


def part2(template, rules, steps):
    """
    >>> rules = {"CH":"B","HH":"N","CB":"H","NH":"C","HB":"C","HC":"B","HN":"C","NN":"C","BH":"H","NC":"B","NB":"B","BN":"B","BB":"N","BC":"B","CC":"N","CN":"C"}
    >>> part2("NN", rules, 2)
    'NBCCN'
    >>> part2("NCNBCHB", rules, 1)
    'NBCCNBBBCBHCB'
    >>> part2("NN", {"NN":"C", "NC": "N", "CN": "N"}, 2)
    'NNCNN'
    >>> part2("NN", {"NN":"C"}, 1)
    'NCN'
    """

    def middle(pair, rules, steps):
        m = rules[pair]
        if steps == 0:
            return m
        else:
            return middle(pair[0] + m, rules, steps - 1) + m + middle(m + pair[1], rules, steps - 1)

    ret = ''
    for j in range(len(template) - 1):
        pair = template[j:j + 2]
        print(pair)
        m = middle(pair, rules, steps - 1)
        ret = ret + template[j] + m
    ret = ret + template[-1]

    return ret


if __name__ == '__main__':
    rules = {}
    template = ''
    with open('input1') as f:
        lines = [line.strip() for line in f.readlines()]
        for line in lines:
            if line == '':
                continue
            if '-' in line:
                pair, res = line.split(' -> ')
                rules[pair] = res
            else:
                template = line


    p1 = part1(template, rules, 10)
    g = defaultdict(lambda: 0)
    for c in p1:
        g[c] += 1

    e = max(list(g.values())) - min(list(g.values()))

    print(f'Part1: {e}')

    p1 = part2(template, rules, 40)
    g = defaultdict(lambda: 0)
    for c in p1:
        g[c] += 1

    e = max(list(g.values())) - min(list(g.values()))
    print(f'Part2: {e}')
