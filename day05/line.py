from enum import Enum

from day05.point import Point


class Direction(Enum):
    HORIZONTAL = 0
    VERTICAL = 1
    DIAGONAL = 2


class Line:
    """2D line"""

    def direction(self) -> Direction:
        if self._begin[0] == self._end[0]:
            return Direction.HORIZONTAL
        elif self._begin[1] == self._end[1]:
            return Direction.VERTICAL
        elif abs(self._begin[0] - self._end[0]) == abs(self._begin[1] - self._end[1]):
            return Direction.DIAGONAL
        else:
            raise Exception(
                f"Can not detect the direction. Points {self._begin} and {self._end} to not form a straight line.")

    def __init__(self, begin: Point, end: Point):
        self._begin = begin
        self._end = end

    def points(self) -> list[Point]:
        """
        Return points of horizontal line
        >>> Line(Point(0,0), Point(2,0)).points()
        [Point(0,0), Point(1,0), Point(2,0)]

        Return points of vertical line
        >>> Line(Point(0,0), Point(2,0)).points()
        [Point(0,0), Point(1,0), Point(2,0)]

        Return points of diagonal line
        >>> Line(Point(0,0), Point(2,2)).points()
        [Point(0,0), Point(1,1), Point(2,2)]
        >>> Line(Point(0,2), Point(2,0)).points()
        [Point(0,2), Point(1,1), Point(2,0)]
        >>> Line(Point(2,0), Point(0,2)).points()
        [Point(2,0), Point(1,1), Point(0,2)]
        >>> Line(Point(2,2), Point(0,0)).points()
        [Point(2,2), Point(1,1), Point(0,0)]

        Handles one unit long lines
        >>> Line(Point(0,0), Point(0,0)).points()
        [Point(0,0)]
        """

        points = []

        if self.direction() == Direction.HORIZONTAL:
            for y in range(min(self._begin[1], self._end[1]), max(self._begin[1], self._end[1]) + 1):
                points.append(Point(self._begin[0], y))
            return points

        if self.direction() == Direction.VERTICAL:
            for x in range(min(self._begin[0], self._end[0]), max(self._begin[0], self._end[0]) + 1):
                points.append(Point(x, self._begin[1]))
            return points

        if self.direction() == Direction.DIAGONAL:
            r = range(0, abs(self._begin[0] - self._end[0]) + 1)
            xsign = 1 if self._begin[0] < self._end[0] else -1
            ysign = 1 if self._begin[1] < self._end[1] else -1

            for i in r:
                points.append(Point(self._begin[0] + xsign * i, self._begin[1] + ysign * i))

        return points
