class Board:

    @classmethod
    def from_str(cls, lines: list[str]) -> 'Board':
        r"""
        >>> str(Board.from_str(["1 0", "10 20"]))
        '  1    0 \n 10   20 '
        """
        rows = []
        for line in lines:
            row = [int(n) for n in line.split()]
            rows.append(row)

        return cls(rows)

    def draw(self, number: int) -> None:
        self.drawn.append(number)

    def winner(self) -> bool:
        """
        >>> b=Board.from_str(["1 2", "3 4"]); b.draw(3); b.draw(4); b.winner()
        True
        >>> b=Board.from_str(["1 2", "3 4"]); b.draw(2); b.draw(4); b.winner()
        True
        >>> b=Board.from_str(["1 2", "3 4"]); b.winner()
        False
        """

        drawn = set(self.drawn)

        # rows checking
        for row in self.rows:
            if drawn.issuperset(set(row)):
                return True

        # columns checking
        for c in range(len(self.rows[0])):
            col = [r[c] for r in self.rows]
            if drawn.issuperset(set(col)):
                return True

        return False

    def numbers(self) -> list[int]:
        ret = []
        for row in self.rows:
            ret += row
        return ret

    def unmarked(self) -> list[int]:
        """
        >>> b=Board.from_str(["1", "2"]); b.draw(1); b.unmarked()
        [2]
        """
        return list(set(self.numbers()) - set(self.drawn))

    def __str__(self) -> str:
        lines = []
        for row in self.rows:
            line = [f'[{cell}]' if cell in self.drawn else f'{cell} ' for cell in row]
            line = [cell.rjust(4) for cell in line]
            lines.append(" ".join(line))
        return "\n".join(lines)

    def __init__(self, rows: list[list[int]]):
        self.rows = rows
        self.drawn = []


def part1(boards: list[Board], numbers: list[int]):
    for n in numbers:
        for b in boards:
            b.draw(n)
            if b.winner():
                print("WINNER after", n)
                print(b)
                return sum(b.unmarked()) * n

    return -1


def part2(boards: list[Board], numbers: list[int]):
    for n in numbers:
        for board in list(boards):
            board.draw(n)
            if board.winner():
                boards.remove(board)

            if len(boards) == 0:
                print("LAST after", n)
                print(board)
                return sum(board.unmarked()) * n

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
        print(board)
    '''

    print('Part 1 answer: ', part1(boards, numbers))
    print('Part 2 answer: ', part2(boards, numbers))
