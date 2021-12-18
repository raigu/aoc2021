import json


def magnitude(number):
    """
    >>> magnitude(json.loads('[9,1]'))
    29
    """
    if isinstance(number, list):
        return magnitude(number[0]) * 3 + magnitude(number[1]) * 2
    else:
        return number


def part1(data):
    sum = data[0]
    i = 1
    while i < len(data):
        sum = '[' + sum + ',' + data[i] + ']'
        sum = reduce(sum)
        i += 1

    return magnitude(json.loads(sum))


def part2(data):
    max = -1
    for i in range(len(data)):
        for j in range(len(data)):
            sum = '[' + data[i] + ',' + data[j] + ']'
            sum = reduce(sum)
            m = magnitude(json.loads(sum))
            if m > max:
                max = m

    return max


def add(op1, op2):
    pass


def reduce(op):
    """
    >>> reduce('[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]')
    '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]'
    >>> reduce('[11, 2]')
    '[[5,6], 2]'
    >>> reduce('[10, 2]')
    '[[5,5], 2]'
    >>> reduce('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]')
    '[[3,[2,[8,0]]],[9,[5,[7,0]]]]'
    >>> reduce('[[6,[5,[4,[3,2]]]],1]')
    '[[6,[5,[7,0]]],3]'
    >>> reduce('[7,[6,[5,[4,[3,2]]]]]')
    '[7,[6,[5,[7,0]]]]'
    >>> reduce('[[[[[9,8],1],2],3],4]')
    '[[[[0,9],2],3],4]'
    """
    ret = ''
    reduced = op
    while ret != reduced:
        ret = reduced

        # exlode
        i = 0
        level = 0
        while i < len(ret) and level < 5:
            if ret[i] == '[':
                level += 1
            elif ret[i] == ']':
                level -= 1
            i += 1

        if level == 5:
            k = i + 1
            while ret[k] != ']':
                k += 1
            op1, op2 = tuple(map(int, ret[i:k].split(',')))

            left = ret[:i - 1]
            right = ret[k + 1:]

            # modify left value
            j = len(left) - 1
            while j >= 0 and not ('0' <= left[j] <= '9'):
                j -= 1
            if j >= 0:
                # extract number position
                k = j
                while '0' <= left[k - 1] <= '9':
                    k -= 1

                left = left[:k] + str(int(left[k:j + 1]) + int(op1)) + left[j + 1:]

            # replace right value
            j = 0
            while j < len(right) and not ('0' <= right[j] <= '9'):
                j += 1
            if j < len(right):
                k = j + 1
                while k < len(right) and '0' <= right[k] <= '9':
                    k += 1

                right = right[:j] + str(int(right[j:k]) + int(op2)) + right[k:]

            reduced = left + '0' + right
            continue

        # split
        i = 0
        while i < len(ret):
            if '0' <= ret[i] <= '9' and '0' <= ret[i + 1] <= '9':
                n = int(ret[i:i + 2])
                left = ret[:i]
                right = ret[i + 2:]
                reduced = left + '[' + str(n // 2) + ',' + str(n // 2 + (n % 2)) + ']' + right
                i = len(ret)
            else:
                i += 1

    return ret


if __name__ == '__main__':
    print("Day 18")
    with open('input') as f:
        lines = [line.strip() for line in f.readlines()]

    print(f'Part1: {part1(lines)}')
    print(f'Part2: {part2(lines)}')
