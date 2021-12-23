import copy
import sys


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


class Amphipod:
    @classmethod
    def none(cls):
        return Amphipod()


class Burrow:

    def __init__(self, depth=2):
        self.space = [
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ]
        for i in range(depth):
            self.space.append(['#', '#', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', '#', '#'])

        self.space.append(['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'])

        self.amphipods = []

    def print(self):
        for layer in self.space:
            print(''.join(layer))

    def min_energy(self) -> int:
        min_energy = sys.maxsize
        i = 0
        amphipod = Amphipod.none()
        while i < len(self.amphipods):
            if self.amphipods[i].can_make_a_move():
                if amphipod.energy_per_step() > self.amphipods[i].energy_per_step():
                    amphipod = self.amphipods[i]
            i += 1

        id = amphipod.id()
        for destination in amphipod.all_possible_destinations():
            burrow = burrow.clone()
            amphipod = burrow.get_amphibod_by_id(id)
            amphipod.move(destination)
            energy = burrow.min_energy()
            if energy < min_energy:
                min_energy = energy

        return min_energy

    @classmethod
    def from_file(cls, filename):
        burrow = Burrow()
        with open(filename) as f:
            i = 0
            for line in f.readlines():
                for j, c in enumerate(line):
                    if c in ['A', 'B', 'C', 'D']:
                        burrow.space[i][j] = c
                i += 1
        return burrow


def is_amphipod(c: str) -> bool:
    return c in ['A', 'B', 'C', 'D']


def step_energy_of_aphipod(a: str) -> int:
    map = {
        'A': 1,
        'B': 10,
        'C': 100,
        'D': 1000,
    }
    return map[a]


def is_home(space, y1, x1) -> bool:
    a = space[y1][x1]
    if not is_above_home(a, x1):
        return False

    while space[y1 + 1][x1] != '#':
        y1 += 1
        if space[y1][x1] != a:
            return False

    return True


def all_possible_paths(space, y1, x1) -> list[list[list]]:
    """
    >>> list(all_possible_paths([['#', '#', '#', '#', '#'], ['#', 'B',' ', ' ', '#'], ['#', '#', '#', '#', '#']], 1, 1))
    [[[0, 1]], [[0, 1], [0, 1]]]
    >>> list(all_possible_paths([['#', '#', '#', '#'], ['#', ' ', '#', '#'], ['#', 'B',' ', '#'], ['#', '#', '#', '#']], 2, 1))
    [[[-1, 0]], [[0, 1]]]
    >>> list(all_possible_paths([['#', '#', '#', '#'], ['#', 'B',' ', '#'], ['#', '#', '#', '#']], 1, 1))
    [[[0, 1]]]
    """

    # does not move if at home
    if is_home(space, y1, x1):
        raise StopIteration
    # up, down, left, right
    down = [1, 0]
    up = [-1, 0]
    directions = ([-1, 0], [1, 0], [0, -1], [0, 1])
    for direction in directions:
        y2 = y1 + direction[0]
        x2 = x1 + direction[1]

        if space[y2][x2] == ' ':  # empty, can move there
            if direction == down:
                # down movement is restricted
                if not is_home(space, y1, x1):
                    # does not go to other's hole
                    continue
            elif direction == up:
                # does not move up if it is home and in place
                if is_home(space, y1, x1):
                    if space[y1 + 1][x1] in ['#', space[y1][x1]]:
                        continue

            next_space = copy.deepcopy(space)
            a = next_space[y1][x1]
            next_space[y1][x1] = 'V'  # mark visited
            next_space[y2][x2] = a

            yield [direction]

            for alternatives in all_possible_paths(next_space, y2, x2):
                yield [direction] + alternatives


def print_space(space):
    for layer in space:
        print(''.join(layer))


def space_hash(space):
    return hash(''.join(''.join(layer) for layer in space))


def is_above_home(c, x):
    """
    >>> is_above_home('A', 3)
    True
    >>> is_above_home('B', 5)
    True
    >>> is_above_home('A', 2)
    False
    """
    return x == 3 + (ord(c) - ord('A')) * 2


def min_energy(space, covered) -> int:
    covered = copy.deepcopy(covered)
    print_space(space)
    ret = sys.maxsize

    down = [1, 0]
    up = [-1, 0]
    left = [0, -1]
    right = [0, 1]

    i = 1
    while i < len(space) - 1:
        j = 1
        while j < len(space[0]) - 1:
            if is_amphipod(space[i][j]) and not is_home(space, i, j):
                directions = [up, down, left, right]
                for direction in directions:
                    y = i + direction[0]
                    x = j + direction[1]

                    if space[y][x] == ' ':
                        if direction == down:
                            # Amphipods will never move from the hallway into a room unless that room is their destination room ...
                            if not is_above_home(space[i][j], x):
                                continue

                            # move as down as possible
                            while space[y + 1][x] == ' ':
                                y += 1

                            # ... and that room contains no amphipods which do not also have that room as their own destination.
                            if not (space[y + 1][x] == '#' or space[y + 1][x] == space[i][j]):
                                continue

                        new = copy.deepcopy(space)
                        new[y][x] = space[i][j]
                        new[i][j] = ' '

                        h = space_hash(new)
                        if h not in covered:
                            covered.add(h)

                            m = min_energy(new, covered)

                            if ret > m + step_energy_of_aphipod(space[i][j]):
                                ret = m + step_energy_of_aphipod(space[i][j])

            j += 1
        i += 1

    if ret == sys.maxsize:  # no moves, is it final?
        suits = True
        i = 0
        while i < 4 and suits:
            c = ord('A') + i
            x = 3 + ((c - ord('A')) * 2)
            y = 2
            while y < len(space) - 1 and suits:
                if ord(space[y][x]) != c:
                    suits = False
                else:
                    y += 1
            i += 1
        if suits:
            return 0  # yee! final!

    return ret


if __name__ == '__main__':
    print('Day 23')

    burrow = Burrow.from_file('input2')

    part1 = min_energy(burrow.space, set())

    print(f'Part1: {part1}')

    part2 = -1

    print(f'Part2: {part2}')

'''
Part1 in R:
> a <- 1
> b <- 10
> c <- 100
> d <- 1000
> s = 9*a+b*2+a*5+b*3+7*b+9*d+4*c+5*d+5*c+7*c+3*a+3*a
> s
[1] 15740
> s = 9*a+b*2+a*5+b*3+7*b+9*d+3*c+5*d+3*c+7*c+3*a+3*a
> s
[1] 15440
> s = 2*a+2*b+5*a+3*b+7*b+9*d+2*c+5*d+3*c+7*c+3*a+8*a
> s
[1] 15338
'''
