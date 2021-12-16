
def bits(hex):
    """
    >>> list(bits('1'))
    ['0', '0', '0', '1']
    """
    for c in hex:
        nibble = str(bin(int(c, 16)))[2:]
        for c in nibble.zfill(4):
            yield c


class Transmission:

    def __init__(self, sequence: str):
        self.sequence = bits(sequence)
        self.counter = 0

    def read(self, bytes: int) -> str:
        ret = ''
        while bytes > 0:
            ret += next(self.sequence)
            self.counter += 1
            bytes -= 1
        return ret

    @property
    def position(self):
        return self.counter

    def end_byte(self):
        # end the hex bits
        while self.counter % 8 != 0:
            self.read(1)


def solution(transmission):
    """
    >>> solution(Transmission('38006F45291200'))
    ['001', '110', '010']
    >>> solution(Transmission('8A004A801A8002F478'))
    ['100', '001', '101', '110']
    >>> solution(Transmission('EE00D40C823060'))
    ['111', '010', '100', '001']
    >>> solution(Transmission('D2FE28'))
    ['110']
    """

    versions = []
    versions.append(transmission.read(3))
    type = transmission.read(3)
    if type == '100':  # literals
        literals = []
        group = '1'
        while group == '1':
            group = transmission.read(1)
            literals.append(transmission.read(4))
    else:
        length_type_id = transmission.read(1)
        if length_type_id == '0':
            length = int(transmission.read(15), 2)
            end = transmission.position + length
            while transmission.position < end:
                versions += solution(transmission)
        else:
            count = int(transmission.read(11), 2)
            while count > 0:
                count -= 1
                versions += solution(transmission)

    return versions


def solution2(transmission):
    version = transmission.read(3)
    type = transmission.read(3)
    if type == '100':  # literals
        literals = []
        group = '1'
        while group == '1':
            group = transmission.read(1)
            literals.append(transmission.read(4))
        return int(''.join(literals), 2)
    else:
        operands = []
        length_type_id = transmission.read(1)
        if length_type_id == '0':
            length = int(transmission.read(15), 2)
            end = transmission.position + length
            while transmission.position < end:
                operands.append(solution2(transmission))
        else:
            count = int(transmission.read(11), 2)
            while count > 0:
                count -= 1
                operands.append(solution2(transmission))

        type = int(type, 2)
        if type == 0:
            return sum(operands)
        elif type == 1:
            p = 1
            for n in operands:
                p *= n
            return p
        elif type == 2:
            return min(operands)
        elif type == 3:
            return max(operands)
        elif type == 5:
            return 1 if operands[0] > operands[1] else 0
        elif type == 6:
            return 1 if operands[0] < operands[1] else 0
        elif type == 7:
            return 1 if operands[0] == operands[1] else 0
        else:
            raise Exception(f"Unknown type: {type}")


if __name__ == '__main__':
    with open('input') as f:
        line = f.read().strip()

    versions = solution(Transmission(line))
    answer = sum([int(v,2) for v in versions])
    print(f'Part1: {answer}')

    print('Part2: '+str(solution2(Transmission(line))))