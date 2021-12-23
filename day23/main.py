import copy
import sys
from collections import defaultdict
from queue import PriorityQueue


def print_space(space):
    for layer in space:
        print(''.join(layer))


def space_hash(space):
    return hash(''.join(''.join(layer) for layer in space))


def is_amphipod(c: str) -> bool:
    return c in ['A', 'B', 'C', 'D']


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


def is_home(space, y1, x1) -> bool:
    if y1 < 2:
        return False  # in a hallway

    a = space[y1][x1]
    if not is_above_home(a, x1):
        return False

    while space[y1 + 1][x1] != '#':
        y1 += 1
        if space[y1][x1] != a:
            return False

    return True


def step_energy_of_aphipod(a: str) -> int:
    map = {
        'A': 1,
        'B': 10,
        'C': 100,
        'D': 1000,
    }
    return map[a]


def neighbours(space):
    ret = []

    amphipods_out = PriorityQueue()
    amphipods_home = PriorityQueue()
    i = 1
    while i < len(space) - 1:
        j = 1
        while j < len(space[0]) - 1:
            if is_amphipod(space[i][j]) and not is_home(space, i, j):
                c = space[i][j]
                if i == 1:  # in the hall
                    amphipods_home.put((-step_energy_of_aphipod(c), (c, i, j)))
                else:  # in the hole
                    if space[i - 1][j] == '.':  # can move up?
                        amphipods_out.put((step_energy_of_aphipod(c), (c, i, j)))
            j += 1
        i += 1

    # priority is to get home
    while not amphipods_home.empty():
        (e, (c, i, j)) = amphipods_home.get()

        # is in the hallway. Let's see if it can move back to home
        home_index = 3 + (ord(c) - ord('A')) * 2
        y = i
        x = j
        energy = 0
        direction = -1 if home_index < x else 1
        blocked = False
        while home_index != x and not blocked:
            x += direction
            energy += step_energy_of_aphipod(c)
            if space[y][x] != '.':
                blocked = True

        if not blocked:  # at the top of hole.
            # move as down as possible
            while space[y + 1][x] == '.':
                y += 1
                energy += step_energy_of_aphipod(c)

            # make sure there are no other aphipd
            u = 1
            while space[y + u][x] != '#' and not blocked:
                if space[y + u][x] != c:
                    blocked = True
                else:
                    u += 1

            # ... and that room contains no amphipods which do not also have that room as their own destination.
            if not blocked:
                new = copy.deepcopy(space)
                new[y][x] = c
                new[i][j] = '.'

                ret.append([new, energy])

    while not amphipods_out.empty():
        (e, (c, i, j)) = amphipods_out.get()
        energy = 0
        # move all the way out
        y = i
        x = j
        while space[y - 1][x] == '.':
            y -= 1
            energy += step_energy_of_aphipod(c)

        # first try to get to own hole.
        x2 = x
        y2 = y
        energy2 = energy
        # ----
        # is in the hallway. Let's see if it can move back to home
        home_index = 3 + (ord(c) - ord('A')) * 2
        direction = -1 if home_index < x else 1
        blocked = home_index == x  # lets interrupt also if it crawled out from same hole ;)
        while home_index != x and not blocked:
            x += direction
            energy += step_energy_of_aphipod(c)
            if space[y][x] != '.':
                blocked = True

        if not blocked:  # at the top of hole.
            # move as down as possible
            while space[y + 1][x] == '.':
                y += 1
                energy += step_energy_of_aphipod(c)

            # make sure there are no other aphipd
            u = 1
            while space[y + u][x] != '#' and not blocked:
                if space[y + u][x] != c:
                    blocked = True
                else:
                    u += 1

            # ... and that room contains no amphipods which do not also have that room as their own destination.
            if not blocked:
                new = copy.deepcopy(space)
                new[y][x] = c
                new[i][j] = '.'

                ret.append([new, energy])

                continue  # moving one hole to another is best option, do not search other options.
        # ---

        # restore what was before checking if can go to hole
        y = y2
        x = x2
        energy = energy2

        # when reached out, move as far left as you can and produce possible outcomes
        x2 = x
        left_energy = energy
        while space[y][x2 - 1] == '.':
            x2 -= 1
            left_energy += step_energy_of_aphipod(c)

            # do not stop on top of hole:
            if x2 not in [3, 5, 7, 9]:
                new = copy.deepcopy(space)
                new[y][x2] = space[i][j]
                new[i][j] = '.'

                ret.append([new, left_energy])

        # when reached out, move as right as you can and produce possible outcomes
        x2 = x
        right_energy = energy
        while space[y][x2 + 1] == '.':
            x2 += 1
            right_energy += step_energy_of_aphipod(c)

            # do not stop on top of hole:
            if x2 not in [3, 5, 7, 9]:
                new = copy.deepcopy(space)
                new[y][x2] = c
                new[i][j] = '.'

                ret.append([new, right_energy])

    return ret


def dijkstra(space, end_hash):
    mapping = {}
    parents = {}
    distances = defaultdict(lambda: sys.maxsize)
    s = space_hash(space)  # start
    distances[end_hash] = 100000  # lets look for solution below this number
    distances[s] = 0  # distance from start to start is known
    queue = PriorityQueue()
    queue.put((0, space))
    while not queue.empty():
        d, v = queue.get()
        parent_hash = space_hash(v)
        for n, edge in neighbours(v):
            i = space_hash(n)

            if i not in mapping:
                mapping[i] = n

            if distances[i] > d + edge:
                distances[i] = d + edge
                parents[i] = parent_hash
                if distances[i] < distances[end_hash]:
                    queue.put((distances[i], n))

    return distances, parents, mapping


def load_space(filename):
    space = []
    with open(filename) as f:
        for line in f.readlines():
            line = line.replace(" ", "#")
            row = [c for c in line.strip()]
            while len(space) > 0 and len(row) < len(space[0]):
                row.append('#')
            space.append(row)
    return space


if __name__ == '__main__':
    print('Day 23')

    space = load_space('input_part1')
    final = load_space('final_part1')
    h = space_hash(final)
    distances, parents, mapping = dijkstra(space, h)
    print('Part1: ', distances[h])

    space = load_space('input_part2')
    final = load_space('final_part2')
    h = space_hash(final)
    distances, parents, mapping = dijkstra(space, h)
    print('Part2: ', distances[h])
    s = space_hash(space)

    print("Solution (backward)")
    print("  (commented out in code)")
    '''
    i = h
    while i != s:
        print("")
        print_space(mapping[i])
        i = parents[i]

    print("")
    print_space(space)
    '''
