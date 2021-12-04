class Board:

    @classmethod
    def from_str(cls, lines: list) -> 'Board':
        r"""
        >>> str(Board.from_str(["1 0", "10 20"]))
        '   1    0\n   10   20\n'
        """

        rows = []
        for line in lines:
            row = [int(n) for n in line.split()]
            rows.append(row)

        return cls(rows)

    def draw(self, number: int) -> None:
        self.numbers.append(number)

    def winner(self) -> bool:
        """
        >>> b=Board.from_str(["1 2", "3 4"]); b.draw(3); b.draw(4); b.winner()
        True
        >>> b=Board.from_str(["1 2", "3 4"]); b.draw(2); b.draw(4); b.winner()
        True
        >>> b=Board.from_str(["1 2", "3 4"]); b.winner()
        False
        """
        # row wins:
        for row in self.rows:
            w = True
            for n in row:
                if n not in self.numbers:
                    w = False
                    break
            if w:
                return True

        for c in range(len(self.rows[0])):
            w = True
            for r in self.rows:
                if r[c] not in self.numbers:
                    w = False
                    break
            if w:
                return True

        return False

    def unmarked(self) -> list:
        ret = []
        for row in self.rows:
            for col in row:
                if col not in self.numbers:
                    ret.append(col)
        return ret

    def __str__(self):
        lines = []
        for r in self.rows:
            line = []
            for c in r:
                if c in self.numbers:
                    c = f'[{c}]'
                else:
                    c = str(c)
                line.append(str(c).rjust(4))
            lines.append(" ".join(line) + "\n")
        return " ".join(lines)

    def __init__(self, rows: list):
        self.rows = rows
        self.numbers = []


def part1(boards, numbers):
    for n in numbers:
        for b in boards:
            b.draw(n)
            if b.winner():
                print("WINNER after", n)
                print(b)
                return sum(b.unmarked()) * n

    return -1


def part2(boards, numbers):
    l = len(boards)
    winners = []
    for n in numbers:
        for (i, b) in enumerate(boards):
            if i not in winners:
                b.draw(n)
                if b.winner():
                    winners.append(i)

                if len(winners) == l:
                    print("LAST after", n)
                    print(b)
                    return sum(b.unmarked()) * n

    return -1


if __name__ == '__main__':
    with open('input') as f:
        lines = f.readlines()

    boards = []
    numbers = [int(n) for n in lines[0].strip().split(',')]
    rows = []
    lines.append("")
    for line in lines[2:]:
        if line.strip() == "":
            boards.append(Board.from_str(rows))
            rows = []
        else:
            rows.append(line.strip())

    '''
    for (i, board) in enumerate(boards):
        print("Board:", i)
        print(str(board))
    '''

    print('Part 1 answer: ', part1(boards, numbers))
    print('Part 2 answer: ', part2(boards, numbers))
