
def part1(data):
    answer = 0

    for line in data:
        answer += 1

    return answer


def part2(data):
    answer = 0

    for line in data:
        answer += 1

    return answer


if __name__ == '__main__':
    with open('input1') as f:
        lines = [line.strip() for line in f.readlines()]

    print(f'Part1: {part1(lines)}')
    print(f'Part2: {part2(lines)}')

