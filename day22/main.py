
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


class Reactor:

    def __init__(self) -> None:
        self.cubes = set()

    def switch(self, op, coordinates):

        for i in range(len(coordinates)):
            if coordinates[i][0] < -50:
                coordinates[i][0] = 50
            if coordinates[i][1] > 50:
                coordinates[i][1] = 50

        [x1, x2], [y1, y2], [z1, z2] = coordinates

        while x1 <= x2:
            if x1 < -50:
                x1 = -50
            y1 = coordinates[1][0]
            while y1 <= y2:
                if y1 < -50 or 50 < y1:
                    y1 = y2

                z1 = coordinates[2][0]
                while z1 <= z2:
                    if z1 < -50 or 50 < z1:
                        z1 = z2

                    cube = (x1, y1, z1)
                    if op == 'on':
                        # print(cube)
                        self.cubes.add(cube)
                    elif cube in self.cubes:
                        self.cubes.remove(cube)
                    z1 += 1
                y1 += 1
            x1 += 1

    def on_count(self) -> int:
        return len(self.cubes)


class Line:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'Line({self.a},{self.b})'

    def __repr__(self):
        """
        >>> Line(1,2)
        Line(1,2)
        """
        return str(self)

    def diff(self, other: 'Line') -> list['Line']:
        """
        >>> Line(0,5).diff(Line(4,6))
        [Line(0,3)]
        >>> Line(2, 3).diff(Line(0,5))
        []
        >>> Line(0,1).diff(Line(2,3))
        [Line(0,1)]
        >>> Line(0, 0).diff(Line(0,0))
        []
        >>> Line(0, 5).diff(Line(2, 3))
        [Line(0,1), Line(4,5)]
        """

        if other.a <= self.a <= other.b and other.a <= self.b <= other.b:
            return []

        if not (self.a <= other.a <= self.b or self.a <= other.b <= self.b):
            return [self]

        parts = []

        cutter = min(self.a, other.a)
        if cutter < other.a:
            parts.append(Line(cutter, other.a - 1))
            cutter = other.a

        if self.b < other.a:
            parts.append(Line(cutter, self.b))
        elif other.b < self.b:
            parts.append(Line(other.b + 1, self.b))

        return parts

    def intersection(self, other: 'Line') -> list['Line']:
        """
        >>>
        """

class Cube:

    def __init__(self, coords) -> None:
        self.coords = coords

    def intersect(self, other: 'Cube') -> 'Cube':
        intersections = []
        for i in range(3):
            line1 = Line(self.coords[i][0], self.coords[i][1])
            line2 = Line(other.coords[i][0], other.coords[i][1])
            intersections.append(line1.intersection(line2))
        return self

class Reactor2:

    def __init__(self) -> None:
        self.cubes = []

    def switch(self, op, cube):

        next = []
        for [o, c] in self.cubes:
            intersections = []
            for i in range(3):
                line1 = Line(c[i][0], c[i][1])
                line2 = Line(cube[i][0], cube[i][1])
                intersections.append(line1.diff(line2))

            for x in intersections[0]:
                line2 = Line(c[0][0], c[0][1])
                for line in line2.diff(x):
                    for y in intersections[1]:
                        for z in intersections[2]:
                            next.append((o, [[line.a, line.b], [y.a, y.b], [z.a, z.b]]))

            for y in intersections[1]:
                line2 = Line(c[1][0], c[1][1])
                for line in line2.diff(y):
                    for x in intersections[0]:
                        for z in intersections[2]:
                            next.append((o, [[x.a, x.b], [line.a, line.b], [z.a, z.b]]))

            for z in intersections[2]:
                line2 = Line(c[2][0], c[2][1])
                for line in line2.diff(z):
                    for x in intersections[0]:
                        for y in intersections[1]:
                            next.append((o, [[x.a, x.b], [y.a, y.b], [line.a, line.b]]))

            for x in intersections[0]:
                for y in intersections[1]:
                    for z in intersections[2]:
                        next.append((o, [[x.a, x.b], [y.a, y.b], [z.a, z.b]]))

        next.append((op, coordinates))

        self.cubes = next

    def on_count(self) -> int:
        ret = 0
        for op, cube in self.cubes:
            x, y, z = cube
            if op == 'on':
                ret += (x[1] - x[0]+1) * (y[1] - y[0]+1) * (z[1] - z[0]+1)
        return ret


if __name__ == '__main__':
    print('Day 22')
    with open('input2') as f:
        lines = [line.strip() for line in f.readlines()]

    '''
    reactor = Reactor()
    for line in lines:
        print(line)
        op, cubes = line.split(' ')
        coordinates = []
        for coord in cubes.split(','):
            axes, min_max = coord.split('=')
            coordinates.append(list(map(int, min_max.split('..'))))
        reactor.switch(op, coordinates)
        print(reactor.on_count())

    print(f'Part1: {reactor.on_count()}')
    '''

    reactor = Reactor2()
    for line in lines:
        print(line)
        op, cubes = line.split(' ')
        coordinates = []
        for coord in cubes.split(','):
            axes, min_max = coord.split('=')
            coordinates.append(list(map(int, min_max.split('..'))))
        reactor.switch(op, coordinates)
        print(reactor.on_count())

    print(f'Part2: {reactor.on_count()}')
