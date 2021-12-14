from collections import defaultdict


def part1(template, rules, steps=10):
    for i in range(steps):
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
    >>> part2("NNCB", rules, 4)
    {'N': 11, 'C': 10, 'B': 23, 'H': 5}
    >>> part2("NNCB", rules, 3)
    {'N': 5, 'C': 5, 'B': 11, 'H': 4}
    >>> part2("NNCB", rules, 1)
    {'N': 2, 'C': 2, 'B': 2, 'H': 1}
    >>> part2("NN", {"NN":"C"}, 1)
    {'N': 2, 'C': 1}
    >>> part2("NN", rules, 2)
    {'N': 2, 'C': 2, 'B': 1}
    """

    pairs = defaultdict(int)
    for j in range(len(template)-1):
        pair = template[j:j+2]
        pairs[pair] += 1

    letters = defaultdict(int)
    for c in template:
        letters[c] += 1

    for i in range(steps):
        next = defaultdict(int)
        for pair in pairs:
            m = rules[pair]
            letters[m] += pairs[pair]
            next[pair[0]+m] += pairs[pair]
            next[m+pair[1]] += pairs[pair]
        pairs = next

    return dict(letters)


if __name__ == '__main__':
    rules = {}
    template = ''
    with open('input') as f:
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
    g = defaultdict(int)
    for c in p1:
        g[c] += 1
    e = max(list(g.values())) - min(list(g.values()))
    print(f'Part1: {e}')

    letters  = part2(template, rules, 40)
    e = max(list(letters.values())) - min(list(letters.values()))
    print(f'Part2: {e}')

