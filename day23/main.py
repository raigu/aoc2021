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
        return False # in a hallway

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

                    if space[y][x] == '.':
                        energy = step_energy_of_aphipod(space[i][j])
                        if direction == down:
                            # Amphipods will never move from the hallway into a room unless that room is their destination room ...
                            if not is_above_home(space[i][j], x):
                                continue

                            # move as down as possible
                            while space[y + 1][x] == '.':
                                y += 1
                                energy += step_energy_of_aphipod(space[i][j])

                            # ... and that room contains no amphipods which do not also have that room as their own destination.
                            if not (space[y + 1][x] == '#' or space[y + 1][x] == space[i][j]):
                                continue
                        elif direction == up:
                            # if starts to move out then move all the way out
                            while space[y-1][x] == '.':
                                y -= 1
                                energy += step_energy_of_aphipod(space[i][j])

                        new = copy.deepcopy(space)
                        new[y][x] = space[i][j]
                        new[i][j] = '.'

                        ret.append([new, energy])
            j += 1
        i += 1

    return ret

def solution(space, end_hash) -> dict:
    distances = defaultdict(lambda: sys.maxsize)
    s = space_hash(space)  # start
    distances[end_hash] = 100000 # lets look for solution below this number
    distances[s] = 0  # distance from start to start is known
    queue = PriorityQueue()
    queue.put((0, space))
    while not queue.empty():
        d, v = queue.get()
        #print("NEW");        print_space(v)
        for n, edge in neighbours(v):
            #print("----");           print_space(n);
            i = space_hash(n)
            if distances[i] > d + edge:
                distances[i] = d + edge
                if i == end_hash:
                    print('Found: ', distances[i])
                #print(d+edge)
                if distances[i] < distances[end_hash]:
                    queue.put((distances[i], n))

    return distances

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

    space = load_space('input_part2')

    print("Initial space:")
    print_space(space)


    final = load_space('final_part2')
    h = space_hash(final)

    distances = solution(space, h)
    print('Part1: ', distances[h])

