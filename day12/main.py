
def to_end(start, points, visited) -> list:
    ret = [[]]

    if start in points:
        neighbours = points[start]
    else:
        neighbours
    for n in points[start]:
        if (start, n) not in visited:  # avoid loops

            if n[0] >= 'a': # big cave
                done = False
                for (s,e) in visited:
                    if s == n[0] or e == n[0]:
                        done = True
                        break
                if done:
                    continue # skip looking to subpathes

            next_visited = set(visited)
            next_visited.add((start, n))
            ret.append([start] + to_end(n, points, next_visited))

    return ret

def part1(data):

    pathes = to_end('start', data, set())

    return len(pathes)


def part2(data):
    answer = 0

    for line in data:
        answer += 1

    return answer


if __name__ == '__main__':
    points = []
    with open('input1') as f:
        for line in [line.strip() for line in f.readlines()]:
            (b, e) = line.strip().split('-')
            points.append(ends)
            ends = points.get(b, [])
            ends.append(e)
            points[b] = ends

    print(points)

    print(f'Part1: {part1(points)}')
    print(f'Part2: {part2(points)}')

