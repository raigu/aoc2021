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
        with open('input1') as f:
            i = 0
            for line in f.readlines():
                for j, c in enumerate(line):
                    if c in ['A', 'B', 'C', 'D']:
                        burrow.space[i][j] = c
                i += 1
        return burrow


if __name__ == '__main__':
    print('Day 23')

    burrow = Burrow.from_file('input1')
    burrow.print()

    print(f'Part1: {burrow.min_energy()}')
    print(f'Part2: {burrow.min_energy()}')

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
