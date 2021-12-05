from day05.line import Line
from day05.point import Point


class Grid:

    def __init__(self) -> None:
        self._grid = {}

    def add_point(self, point: Point) -> None:
        if point not in self._grid:
            self._grid[point] = 0

        self._grid[point] += 1

    def add_line(self, line: Line) -> None:
        for point in line.points():
            self.add_point(point)

    def number_of_intersecting_points(self) -> int:
        answer = 0
        points = list(self._grid.keys())
        for point in points:
            if self._grid[point] > 1:
                answer += 1
        return answer
