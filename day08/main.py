import itertools

def trans(i, mapping):
    """
    >>> trans('a', 'abcdefg')
    'a'
    >>> trans('abcdefg', 'gfedcba')
    'gfedcba'
    >>> trans('bb', 'gfedcba')
    'ff'
    """

    r = ''
    for c in i:
        r += mapping[ord(c)-ord('a')]

    return r

def decode(line):
    """
    >>> decode('acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf')
    5353
    """

    (input, output) = line.split('|')
    inputs = input.strip().split(' ')
    inputs = ["".join(sorted(i)) for i in inputs]

    outputs = output.strip().split(' ')
    outputs = ["".join(sorted(i)) for i in outputs]

    allowed = [
        'abcefg',
        'cf',
        'acdeg',
        'acdfg',
        'bcdf', #4
        'abdfg',
        'abdefg',
        'acf',
        'abcdefg',
        'abcdfg',
    ]

    signals = 'abcdefg'
    comb = list(itertools.permutations(signals))

    for c in comb:
        b = ''.join(c)

        accepted = ["".join(sorted(trans(a, b))) for a in allowed]

        contradiction = False
        for i in inputs:
            if i not in accepted:
                contradiction = True
                break

        for o in outputs:
            if o not in accepted:
                contradiction = True
                break

        if not contradiction:
            r = ''
            for o in outputs:
                r += str(accepted.index(o))

            return int(r)

    return -1



if __name__ == '__main__':
    answer = 0
    answer2 = 0
    with open('input') as f:
        lines = [line.strip() for line in f.readlines()]
        for line in lines:
            # part 1
            (input, output) = line.split('|')
            inputs = input.strip().split(' ')
            outputs = output.strip().split(' ')
            for o in outputs:
                if len(o) in [2,3,4,7]:
                    answer += 1
            # part 2
            answer2 += decode(line)

    print(f'Part1: {answer}')
    print(f'Part2: {answer2}')

