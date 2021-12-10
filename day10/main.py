def first_corrupted(line):
    """
    >>> first_corrupted('(')
    '?'
    >>> first_corrupted('()')
    ''
    >>> first_corrupted('{([(<{}[<>[]}>{[]{[(<()>')
    '}'
    """
    openers = []

    other = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>',
    }
    for c in line:
        if c in ['(', '[', '{', '<']:
            openers.append(c)
        else:
            e = openers.pop()
            if c != other[e]:
                return c  # Corrupted

    return ''


def part1(data):
    answer = 0

    map = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }

    for line in data:
        line = line.strip()

        char = first_corrupted(line)

        if char != '':
            answer += map[char]

    return answer


def score(tail):
    """
    >>> score('}}]])})]')
    288957
    >>> score('])}>')
    294
    """
    points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }

    ret = 0
    for c in tail:
        ret = (ret * 5) + points[c]

    return ret

def tail(data):
    """
    >>> tail('[({(<(())[]>[[{[]{<()<>>')
    '}}]])})]'
    """
    openers = []

    other = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>',
    }
    for c in data:
        if c in ['(', '[', '{', '<']:
            openers.append(c)
        else:
            e = openers.pop()
            if c != other[e]:
                return '' # Corrupted

    openers = openers[::-1] # reverse array
    t = ''.join(openers)
    t = ''.join([other[t] for t in t])

    return t




if __name__ == '__main__':
    print("Day 10")

    with open('input') as f:
        lines = [line.strip() for line in f.readlines()]

    print(f'Part1: {part1(lines)}')

    p2 = 0
    all = []
    for line in lines:
        t = tail(line.strip())
        s = score(t)
        if s > 0:
            all.append(score(t))

    all = sorted(all)
    p2 = all[len(all)//2]
    print(f'Part2: {p2}')
