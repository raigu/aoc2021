
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

    def intersection(self, other: 'Line') -> list['Line']:
        """
        >>> Line(-20,26).intersection(Line(-22,28))
        [Line(-20,26)]
        >>> Line(4,8).intersection(Line(2,6))
        [Line(4,6)]
        >>> Line(1,5).intersection(Line(2,3))
        [Line(2,3)]
        >>> Line(0,3).intersection(Line(1,5))
        [Line(1,3)]
        >>> Line(0,1).intersection(Line(2,3))
        []
        """

        a, b = max(self.a, other.a), min(self.b, other.b)
        if a < b:
            return [Line(a,b)]
        else:
            return []


class Cube:

    def __init__(self, coords) -> None:
        self.coords = coords

    def count(self):
        """
        >>> Cube(((10,12), (10,12), (10,12))).count()
        27
        """
        x, y, z = self.coords
        return (x[1] - x[0] + 1) * (y[1] - y[0] + 1) * (z[1] - z[0] + 1)

    def __str__(self) -> str:
        return f'Cube((({self.coords[0][0]},{self.coords[0][1]}),({self.coords[1][0]},{self.coords[1][1]}),({self.coords[2][0]},{self.coords[2][1]}))'

    def __repr__(self) -> str:
        return str(self)

    def intersection(self, cube):
        """
        >>> Cube(((10,12),(10,12),(10, 12))).intersection(Cube(((11,13),(11,13),(11,13))))
        [Cube(((11,12),(11,12),(11,12))]
        """
        coords = []
        for i in range(3):
            line1 = Line(self.coords[i][0], self.coords[i][1])
            line2 = Line(cube.coords[i][0], cube.coords[i][1])

            intersection = line1.intersection(line2)
            if intersection:
                coords.append((intersection[0].a, intersection[0].b))
            else:
                return []
        return [Cube(coords)]


class OnCube:

    def __init__(self, cube: Cube) -> None:
        self.cube = cube
        self.offs = []

    def turn_off(self, cube: Cube):
        intersection = self.cube.intersection(cube)
        self.offs += intersection

    def count(self):

        ret = self.cube.count()

        for i in range(len(self.offs)):
            ret -= self.offs[i].count()
            for j in range(i):
                intersection = self.offs[j].intersection(self.offs[i])
                if intersection:
                    ret += intersection[0].count()

        return ret


class Reactor2:

    def __init__(self) -> None:
        self.cubes = []

    def switch(self, op, cube: Cube):

        for c in self.cubes:
            c.turn_off(cube)

        if op == 'on':
            self.cubes.append(OnCube(cube))

    def on_count(self) -> int:
        ret = 0
        for c in self.cubes:
            ret += c.count()
        return ret


if __name__ == '__main__':
    print('Day 22')
    with open('input4') as f:
        lines = [line.strip() for line in f.readlines()]

    old = Reactor()
    reactor = Reactor2()
    for line in lines:
        op, cubes = line.split(' ')
        coordinates = []
        for coord in cubes.split(','):
            axes, min_max = coord.split('=')
            min_max = list(map(int, min_max.split('..')))
            coordinates.append(min_max)

        out = False
        for i, min_max in enumerate(coordinates):
            a, b = min_max
            if a < -50 and b < -50:
                out = True
                continue
            if a > 50 and b > 50:
                out = True
                continue

            if a < -50:
                a = -50
            if b < -50:
                b = -50
            if a > 50:
                a = 50
            if b > 50:
                b = 50

            coordinates[i] = (a, b)

        print(line)
        if not out:
            print(coordinates)
            old.switch(op, coordinates)
            reactor.switch(op, Cube(coordinates))

            print('  ', old.on_count(), reactor.on_count())



        # print(reactor.on_count())

    print(f'Part1: {reactor.on_count()}')

    reactor = Reactor2()
    for line in lines:
        # print(line)
        op, cubes = line.split(' ')
        coordinates = []
        for coord in cubes.split(','):
            axes, min_max = coord.split('=')
            coordinates.append(list(map(int, min_max.split('..'))))
        reactor.switch(op, Cube(coordinates))
        #print(reactor.on_count())

    # 1667280076479371 <-- too high
    print(f'Part2: {reactor.on_count()}')
