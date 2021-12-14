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


def part2(pairs, rules, steps):
    """
    >>> part2({"NN": 1}, {"NN":"C"}, 1)
    {'NC': 1, 'CN': 1}
    >>> rules = {"CH":"B","HH":"N","CB":"H","NH":"C","HB":"C","HC":"B","HN":"C","NN":"C","BH":"H","NC":"B","NB":"B","BN":"B","BB":"N","BC":"B","CC":"N","CN":"C"}
    >>> part2(["NN"], rules, 2)
    {'NB': 1, 'BC': 1, 'CC': 1, 'CN': 1}
    >>> part2({'NB': 1, 'BC': 1, 'CC': 1, 'CN': 1}, rules, 1)
    {'NB': 2, 'BC': 2, 'CC': 1, 'CN': 1, 'BB': 2, 'CB': 3, 'BH': 1, 'HC': 1}
    """

    letters = defaultdict(lambda: 0)

    for i in range(steps):
        next = defaultdict(lambda: 0)
        for pair in pairs:
            m = rules[pair]
            letters[m] += 1
            next[pair[0]+m] += 1
            next[m+pair[1]] += 1
        pairs = next

    return dict(pairs)


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

    pairs = defaultdict(lambda: 0)
    for j in range(len(template)-1):
        pair = template[j:j+2]
        pairs[pair] += 1

    print(pairs)

    p1 = part2(pairs, rules, 10)
    print(p1)
    g = defaultdict(lambda: 0)
    for pair in p1:
        g[pair[0]] += p1[pair]
        g[pair[1]] += p1[pair]

    g = dict(g)
    g[template[0]] -= 1
    g[template[-1]] -= 1

    print(dict(g))

    print(sum(list(g.values())), max(list(g.values())), min(list(g.values())))
    e = max(list(g.values())) - min(list(g.values()))
    print(f'Part2: {e}')
