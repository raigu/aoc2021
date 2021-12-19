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


def multiply(matrix, vector):
    """
    >>> multiply([[1,2], []])
    [[2,-1]]
    """


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
                    coordinate[i] = c*shift[i]
                ret.append(Vector(*coordinate))
        return ret

    def __hash__(self) -> int:
        return hash(repr(self))

    def __repr__(self) -> str:
        coordinates = ','.join([str(c) for c in self.coordinates])
        return f'Vector({coordinates})'


if __name__ == '__main__':
    scanners = []
    with open('input2') as f:
        lines = [line.strip() for line in f.readlines()]
        j = -1
        for line in lines:
            if line.startswith('---'):  # new scanner
                scanners.append(set())
                j += 1
            elif line != '':
                scanners[j].add(Vector(*list(map(int, line.split(',')))))

    beacons = set()
    minimum_match_requirement = 12
    for sui0 in scanners[0]:
        for sui1 in scanners[1]:
            s2 = sui0 - sui1
            for direction in directions:
                transformed = set()
                for beacon in transform(scanners[1], direction):
                    transformed.add(s2 + beacon)

                matched = transformed.intersection(scanners[0])
                if len(matched) >= minimum_match_requirement:
                    beacons |= matched
                    break

    print(beacons)

    print('Day 19')
    print(f'Part1: {part1(lines)}')
    print(f'Part2: {part2(lines)}')
