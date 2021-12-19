from itertools import product, permutations


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

def identity_matrix(n):
    """
    >>> identity_matrix(3)
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    >>> identity_matrix(2)
    [[1, 0], [0, 1]]
    """
    ret = []*n
    for i in range(n):
        row = []
        for j in range(n):
            if j == i:
                row.append(1)
            else:
                row.append(0)
        ret.append(row)
    return ret


class Vector:
    """
    >>> Vector(1,2,3) + Vector(5,2,2)
    Vector(6,4,5)
    >>> {Vector(1,2)}.intersection({Vector(1,2)})
    {Vector(1,2)}
    >>> Vector(1,2) == Vector(2,1)
    False
    >>> Vector(1,2) == Vector(1,2)
    True
    >>> Vector(1,2) - Vector(3, 4)
    Vector(-2,-2)
    >>> Vector(1,2) + Vector(3, 4)
    Vector(4,6)
    """

    def __init__(self, *coordinates) -> None:
        super().__init__()
        self.coordinates = coordinates

    def __add__(self, other: 'Vector') -> 'Vector':
        ret = []
        for i in range(len(self.coordinates)):
            ret.append(self.coordinates[i] + other.coordinates[i])
        return Vector(*ret)

    def __sub__(self, other: 'Vector') -> 'Vector':
        ret = []
        for i in range(len(self.coordinates)):
            ret.append(self.coordinates[i] - other.coordinates[i])
        return Vector(*ret)

    def __eq__(self, o: 'Vector') -> bool:
        for i in range(len(self.coordinates)):
            if self.coordinates[i] != o.coordinates[i]:
                return False

        return True

    def transform(self, direction: list) -> 'Vector':
        """
        >>> Vector(1, 2).transform([[0, 1], [1, 0]])
        Vector(2,1)
        >>> Vector(1,2,3).transform([[1,0,0],[0,1,0],[0,0,1]])
        Vector(1,2,3)
        """

        ret = []
        for row in direction:
            ret.append(sum(d * c for d, c in zip(row, self.coordinates)))

        return Vector(*ret)

    def all_directions(self):
        """
        >>> Vector(1,2).all_directions()
        [Vector(-1,-2), Vector(-2,-1), Vector(-1,2), Vector(-2,1), Vector(1,-2), Vector(2,-1), Vector(1,2), Vector(2,1)]
        >>> Vector(1).all_directions()
        [Vector(-1), Vector(1)]
        """

        ret = []
        for shift in product([-1, 1], repeat=len(self.coordinates)):
            for coordinate in permutations(self.coordinates, len(self.coordinates)):
                coordinate = list(coordinate)
                for i, c in enumerate(coordinate):
                    coordinate[i] = c * shift[i]
                ret.append(Vector(*coordinate))
        return ret

    def __hash__(self) -> int:
        return hash(repr(self))

    def __repr__(self) -> str:
        coordinates = ','.join([str(c) for c in self.coordinates])
        return f'Vector({coordinates})'


def all_directions(n) -> list:
    rows = []
    for row in list(product([-1, 0, 1], repeat=n)):
        if len([x for x in row if x == 0]) == n - 1:
            rows.append(row)

    ret = []
    for direction in list(product(rows, repeat=n)):
        i = 0
        suits = True
        while i < n and suits:
            col = [direction[j][i] for j in range(n)]
            if len([x for x in col if x == 0]) != n - 1:
                suits = False
            else:
                i += 1
        if suits:
            ret.append(direction)

    return ret


if __name__ == '__main__':
    scanners = []

    input = 2

    if input == 1:
        minimum_match_requirement = 3
        directions = all_directions(2)
    else:
        minimum_match_requirement = 12
        directions = all_directions(3)

    with open(f'input{input}') as f:
        lines = [line.strip() for line in f.readlines()]
        j = -1
        for line in lines:
            if line.startswith('---'):  # new scanner
                scanners.append(set())
                j += 1
            elif line != '':
                scanners[j].add(Vector(*list(map(int, line.split(',')))))



    beacons = scanners[0] # first scanner beacons we already know

    for i in range(len(scanners)):
        j = i + 1
        while j < len(scanners):
            print(i, j)
            for sui0 in scanners[i]:
                for sui1 in scanners[j]:
                    s2 = sui0 - sui1
                    for direction in directions:
                        transformed = set()
                        for beacon in scanners[j]:
                            beacon = beacon.transform(direction)
                            transformed.add(s2 + beacon)

                        matched = transformed.intersection(scanners[0])
                        if len(matched) >= minimum_match_requirement:
                            beacons |= matched
                            break
            j += 1
    print(beacons)
    print(len(beacons))

    print('Day 19')
    print(f'Part1: {part1(lines)}')
    print(f'Part2: {part2(lines)}')
