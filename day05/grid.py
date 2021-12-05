from day05.point import Point


class Grid:

    def __init__(self) -> None:
        self._grid = {}

    def add(self, point: Point):
        if point not in self._grid:
            self._grid[point] = 0

        self._grid[point] += 1

    def __getitem__(self, point: Point) -> int:
        return self._grid[point]

    def points(self) -> list[Point]:
        return list(self._grid.keys())