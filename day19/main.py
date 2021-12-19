from itertools import product


def manhattan_distance(locations):
    max = 0
    for i, s0 in enumerate(locations):
        for j, s1 in enumerate(locations):
            if i == j:
                continue

            d = 0
            for c0, c1 in zip(s0, s1):
                d += abs(c0 - c1)
            if d > max:
                max = d

    return max


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

    n = 3
    minimum_match_requirement = 12
    directions = all_directions(n)

    with open(f'input') as f:
        lines = [line.strip() for line in f.readlines()]
        j = -1
        for line in lines:
            if line.startswith('---'):  # new scanner
                scanners.append([])
                j += 1
            elif line != '':
                scanners[j].append(Vector(*list(map(int, line.split(',')))))

    visited = [0]
    queue = [0]
    locations = [[0, 0, 0]]
    while len(visited) != len(scanners):
        i = queue.pop()
        j = 0
        for j in range(len(scanners)):
            if j in visited or i == j:
                continue

            print(i, j)
            k = 0
            found = False
            while k < len(scanners[i]) and not found:
                l = 0
                while l < len(scanners[j]) and not found:
                    for direction in directions:
                        s2 = scanners[i][k] - scanners[j][l].transform(direction)
                        transformed = []
                        for beacon in scanners[j]:
                            beacon = beacon.transform(direction)
                            transformed.append(s2 + beacon)

                        matched = set(transformed).intersection(scanners[i])
                        if len(matched) >= minimum_match_requirement:
                            print("Found ", j, 'coordinates:', s2)
                            found = True
                            scanners[j] = transformed
                            locations.append(list(s2.coordinates))
                            visited.append(j)
                            queue.append(j)
                            break
                    l += 1
                k += 1

    beacons = set()
    for current in scanners:
        beacons |= set(current)

    print('Day 19')
    print(f'Part1:', len(beacons))
    print(f'Part2: {manhattan_distance(locations)}')
