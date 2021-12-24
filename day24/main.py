
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


def process(instructions: list, input: str) -> dict:
    """
    >>> process(['inp x', 'mul x -1'], '3')
    {'w': 0, 'x': -3, 'y': 0, 'z': 0}

    It has integer variables w, x, y, and z. These variables all start with the value 0.
    >>> process([],'')
    {'w': 0, 'x': 0, 'y': 0, 'z': 0}

    mod a b - Divide the value of a by the value of b, then store the remainder in variable a.
    (This is also called the modulo operation.)
    >>> process(['inp w', 'mod w 3'], '8')
    {'w': 2, 'x': 0, 'y': 0, 'z': 0}

    div a b - Divide the value of a by the value of b, truncate the result to an integer
    >>> process(['inp w', 'div w 2'], '8')
    {'w': 4, 'x': 0, 'y': 0, 'z': 0}

    div - truncate the result to an integer /.../ (Here, "truncate" means to round the value toward zero.)
    >>> process(['inp w', 'div w 2'], '5')
    {'w': 2, 'x': 0, 'y': 0, 'z': 0}

    >>> process(['inp a', 'add a 3'], "1")
    {'w': 0, 'x': 0, 'y': 0, 'z': 0, 'a': 4}

    >>> process(["inp z", "inp x","mul z 3","eql z x"], '13')
    {'w': 0, 'x': 3, 'y': 0, 'z': 1}

    Sample dats
    >>> process([ 'inp w', 'add z w', 'mod z 2', 'div w 2', 'add y w', 'mod y 2', 'div w 2', 'add x w', 'mod x 2', 'div w 2', 'mod w 2'], '4')
    {'w': 0, 'x': 1, 'y': 0, 'z': 0}
    >>> process([ 'inp w', 'add z w', 'mod z 2', 'div w 2', 'add y w', 'mod y 2', 'div w 2', 'add x w', 'mod x 2', 'div w 2', 'mod w 2'], '7')
    {'w': 0, 'x': 1, 'y': 1, 'z': 1}
    """
    memory = {
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0,
    }
    cursor = 0

    for i in instructions:
        # print(i)
        if i.startswith('inp'):
            c, op1 = i.split(' ')
            memory[op1] = int(input[cursor])
            cursor += 1
        else:
            c, op1, op2 = i.split(' ')
            op2 = memory[op2] if op2 in memory else int(op2)
            # op2 = int(op2) if op2.isdigit() else memory[op2]
            if c == 'mul':
                memory[op1] = memory[op1] * op2
            elif c == 'eql':
                memory[op1] = 1 if memory[op1] == op2 else 0
            elif c == 'add':
                memory[op1] = memory[op1] + op2
            elif c == 'div':
                memory[op1] = memory[op1] // op2
            elif c == 'mod':
                memory[op1] = memory[op1] % op2
            else:
                raise Exception("Unknown command: " + i)

    return memory


def reverse(instructions):
    """
    >>> reverse(['add z y'])
    0
    """
    memory = {
        'z': 0
    }

    return memory


if __name__ == '__main__':
    print("Day 24")

    with open('input') as f:
        lines = [line.strip() for line in f.readlines()]

    '''
    found = False
    number = '11199999999999'
    i = 0
    while not found and len(number) >= 14:
        i += 1
        if i % 1000000 == 0:
            print(number)
        memory = process(lines, number)
        print(memory['z'], number)
        if memory['z'] == 0:
            found = True
        else:
            number = str(int(number) - 1)
            while '0' in number:
                number = str(int(number)-1)

    answer = number if found else -1
    '''

    i = 0
    parts = []
    params = []
    while i < len(lines):
        #print(i)
        a = lines[i + 4]
        b = lines[i + 5]
        c = lines[i + 15]

        # print(a,b,c)

        a = int(a.split(' ')[2])
        b = int(b.split(' ')[2])
        c = int(c.split(' ')[2])

        part = lines[i:i + 18]
        part[4] = 'div z #'
        part[5] = 'add x #'
        part[15] = 'add y #'
        parts.append(part)

        # print(a,b,c)
        params.append([a, b, c])

        i += 18

    print(params)
    '''
    for i in range(len(parts)):
        if ';'.join(parts[0]) != ';'.join(parts[i]):
            print('jama!')
    '''

    def calc(number, invariant=26):
        z = 0
        for i in range(len(number)):
            a, b, c = params[i]
            w = int(number[i])
            x = 1 if ((z % 26) + b) != w else 0
            z = (z // a) * ((25 * x) + 1) + (w + c) * x

            if z > invariant:
                return -1
        return z





    found = False
    number = '9'
    i = 0
    counter = 0
    max = '99999999999999'
    while not found:
        #print(number)
        counter += 1
        if counter % 1000000 == 0:
            print(counter, number)

        z = calc(number, 2000)
        if z == -1: # with this beginning the invariants are not met:
            number = str(int(number)-1)
        else:
            if z == 0 and len(number) == 14:
                found = True
            else:

                number = number + '9'

    if found:
        print("Found!", number)
    else:
        print("did not found :(")

    '''
    w <- ?
    x = 0
    x = x + z
    x = x % 26
    z = z // a
    x = x + b
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    
    y = 0
    y = y + 25
    y = y * x
    y = y + 1
    z = z * y
    y = 0
    y = y + w
    y = y + c
    y = y * x
    z = z + y
    '''

    '''
    w <- ?
    x = 0
    x = x + z
    x = x % 26
    z = z // a
    x = x + b
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    
    y = 0
    y = y + 25
    y = y * x
    y = y + 1
    z = z * y
    y = 0
    y = y + w
    y = y + c
    y = y * x
    z = z + y
    '''
    answer = 0
    print(f'Part1: {answer}')

    print(f'Part2: {part2(lines)}')
