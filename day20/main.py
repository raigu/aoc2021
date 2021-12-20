import sys
from enum import Enum


class Pixel(Enum):
    DARK = 0
    LIGHT = 1

    @classmethod
    def from_str(cls, light: str) -> 'Pixel':
        return cls.LIGHT if light == '#' else cls.DARK

    def opposite(self):
        """
        >>> Pixel.DARK.opposite().name
        'LIGHT'
        """
        if self.value == self.DARK.value:
            return self.LIGHT
        else:
            return self.DARK

    def __str__(self) -> str:
        return '#' if self == Pixel.LIGHT else '.'


class Space:

    def __init__(self):
        self.max_y = -sys.maxsize
        self.max_x = -sys.maxsize
        self.min_y = sys.maxsize
        self.min_x = sys.maxsize
        self.default_pixel = Pixel.DARK
        self.pixels = set()

    def add_pixel(self, y: int, x: int, pixel: Pixel):
        if y < self.min_y:
            self.min_y = y
        if y > self.max_y:
            self.max_y = y
        if x < self.min_x:
            self.min_x = x
        if x > self.max_x:
            self.max_x = x

        if pixel != self.default_pixel:
            self.pixels.add((y, x))

    def pixel(self, y, x) -> Pixel:
        if self.min_y <= y <= self.max_x and self.min_x <= x and self.max_x:
            if (y, x) in self.pixels:
                return self.default_pixel.opposite()
            else:
                return self.default_pixel
        else:
            return self.default_pixel

    def output_index(self, y, x) -> int:
        digit = ''
        i = y - 1
        while i < y + 2:
            j = x - 1
            while j < x + 2:
                if str(self.pixel(i, j)) == '#':
                    digit += '1'
                else:
                    digit += '0'
                j += 1
            i += 1

        return int(digit, 2)

    def enhance(self, algorithm: str) -> 'Space':
        output = Space()
        if Pixel.from_str(algorithm[0]) == Pixel.LIGHT:
            output.default_pixel = self.default_pixel.opposite()
        else:
            output.default_pixel = Pixel.DARK

        y = self.min_y - 1
        while y <= self.max_y + 2:
            x = self.min_x - 1
            while x <= self.max_x + 2:
                index = self.output_index(y, x)
                light = Pixel.from_str(algorithm[index])
                output.add_pixel(y, x, light)
                x += 1
            y += 1

        return output

    def print(self) -> None:
        y = self.min_y
        while y <= self.max_y:
            x = self.min_x
            row = []
            while x <= self.max_x:
                if (y, x) in self.pixels:
                    light = str(self.default_pixel.opposite())
                else:
                    light = str(self.default_pixel)
                row.append(light)

                x += 1
            print(''.join(row))
            y += 1

    def light_count(self):
        return len(self.pixels)


if __name__ == '__main__':
    print('Day 20')

    with open('input1') as f:
        lines = [line.strip() for line in f.readlines()]

        space = Space()
        algorithm = lines.pop(0).strip()
        lines.pop(0)
        image = set()
        for y, row in enumerate(lines):
            for x, light in enumerate(row.strip()):
                space.add_pixel(y, x, Pixel.from_str(light))
                if light == '#':
                    image.add((y, x))

    # first 2
    for i in range(2):
        space = space.enhance(algorithm)
    print(f'Part1: {space.light_count()}')

    # next 48
    for i in range(50 - 2):
        space = space.enhance(algorithm)
    print(f'Part2: {space.light_count()}')
