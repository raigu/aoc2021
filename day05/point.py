class Point:
    """I am a point in n-dimensional space. """
    def __init__(self, *coordinates):
        self._coordinates = coordinates

    def __repr__(self):
        return "Point("+",".join(str(coordinate) for coordinate in self._coordinates) + ")"

    def __hash__(self):
        """
        Can be used as a key in a dictionary
        >>> d = {Point(1): 10, Point(2): 20}; d[Point(2)] == 20 and d[Point(1)] == 10
        True
        """
        return hash(repr(self))

    def __getitem__(self, dimension: int) -> int:
        """Access the coordinate in given dimension

        Dimensions are numbered starting from zero.
        >>> Point(0)[0] == 0
        True
        >>> Point(222,333)[1] == 333
        True
        """

        return self._coordinates[dimension]

    def __eq__(self, other):
        """
        >>> Point(1) == Point(1)
        True
        """
        equal = len(self._coordinates) == len(other._coordinates)
        i = len(self._coordinates)
        while equal and i > 0:
            i -= 1
            equal = self._coordinates[i] == other._coordinates[i]

        return equal
