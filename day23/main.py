import sys
from collections import defaultdict
from queue import PriorityQueue


def print_space(space):
    for layer in space:
        print(''.join(layer))

def space_hash(space):
    return hash(''.join(''.join(layer) for layer in space))


def neighbours(space):


    return [(space, 0)]

def solution(space) -> dict:
    distances = defaultdict(lambda: sys.maxsize)
    s = space_hash(space)  # start
    distances[s] = 0  # distance from start to start is known
    queue = PriorityQueue()
    queue.put((0, space))
    while not queue.empty():
        d, v = queue.get()
        for n, edge in neighbours(v):
            i = space_hash(n)
            if distances[i] > d + edge:
                distances[i] = d + edge
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

    space = load_space('input1')

    print("Initial space:")
    print_space(space)

    distances = solution(space)

    final = load_space('final1')

    h = space_hash(final)
    print('Part1: ', distances[h])

