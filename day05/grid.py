from enum import Enum

from day05.point import Point


class Direction(Enum):
    HORIZONTAL = 0
    VERTICAL = 1
    DIAGONAL = 2


class Grid:

    def __init__(self) -> None:
        self._grid = {}

    def add(self, point: Point):
        if point not in self._grid:
            self._grid[point] = 0

        self._grid[point] += 1

    def draw_lines(self, lines, directions: set[Direction]) -> None:
        for b, e in lines:
            if Direction.HORIZONTAL in directions and b[0] == e[0]:
                for y in range(min(b[1], e[1]), max(b[1], e[1]) + 1):
                    self.add(Point(b[0], y))

            if Direction.VERTICAL in directions and b[1] == e[1]:
                for x in range(min(b[0], e[0]), max(b[0], e[0]) + 1):
                    self.add(Point(x, b[1]))

            if Direction.DIAGONAL in directions and abs(b[0] - e[0]) == abs(b[1] - e[1]):
                r = range(0, abs(b[0] - e[0]) + 1)
                xsign = 1 if b[0] < e[0] else -1
                ysign = 1 if b[1] < e[1] else -1

                for i in r:
                    self.add(Point(b[0] + xsign * i, b[1] + ysign * i))

    def number_of_intersecting_points(self) -> int:
        answer = 0
        points = list(self._grid.keys())
        for point in points:
            if self._grid[point] > 1:
                answer += 1
        return answer