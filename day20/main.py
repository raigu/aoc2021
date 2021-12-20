import sys
from collections import defaultdict
from enum import Enum


class Brightness(Enum):
    DARK = 0
    LIGHT = 1

    @classmethod
    def from_str(cls, light: str) -> 'Brightness':
        return cls.LIGHT if light == '#' else cls.DARK

    def opposite(self):
        return self.LIGHT if self == self.DARK else self.DARK

    def __str__(self) -> str:
        return '#' if self == Brightness.LIGHT else '.'


class Image:

    def __init__(self, default_brightness: Brightness):
        self.max_y = -sys.maxsize
        self.max_x = -sys.maxsize
        self.min_y = sys.maxsize
        self.min_x = sys.maxsize
        self.default_brightness = default_brightness
        self.pixels = defaultdict(lambda: default_brightness)

    def add_pixel(self, y: int, x: int, brightness: Brightness):
        if y < self.min_y:
            self.min_y = y
        if y > self.max_y:
            self.max_y = y
        if x < self.min_x:
            self.min_x = x
        if x > self.max_x:
            self.max_x = x

        self.pixels[(y, x)] = brightness

    def enhancement_algorithm_index(self, y, x) -> int:
        digit = ''
        i = y - 1
        while i < y + 2:
            j = x - 1
            while j < x + 2:
                if self.pixels[(i, j)] == Brightness.LIGHT:
                    digit += '1'
                else:
                    digit += '0'
                j += 1
            i += 1

        return int(digit, 2)

    def enhance(self, algorithm: str) -> 'Image':
        if Brightness.from_str(algorithm[0]) == Brightness.LIGHT:
            default_brightness = self.default_brightness.opposite()
        else:
            default_brightness = Brightness.DARK
        output = Image(default_brightness)

        y = self.min_y - 1
        while y <= self.max_y + 2:
            x = self.min_x - 1
            while x <= self.max_x + 2:
                index = self.enhancement_algorithm_index(y, x)
                brightness = Brightness.from_str(algorithm[index])
                output.add_pixel(y, x, brightness)
                x += 1
            y += 1

        return output

    def lit_pixels_count(self) -> int:
        if self.default_brightness == Brightness.LIGHT:
            raise Exception('There is no number big enough to answer your question!')
        return len([v for c,v in self.pixels.items() if v == Brightness.LIGHT])

    def print(self) -> None:
        i = self.min_y
        while i <= self.max_y:
            row = []
            j = self.min_x
            while j <= self.max_x:
                row.append(str(self.pixels[(i,j)]))
                j += 1
            print(''.join(row))
            i += 1


if __name__ == '__main__':
    print('Day 20')

    with open('input') as f:
        lines = [line.strip() for line in f.readlines()]

        algorithm = lines.pop(0).strip()
        lines.pop(0)
        image = Image(Brightness.DARK)
        for y, row in enumerate(lines):
            for x, brightness in enumerate(row.strip()):
                image.add_pixel(y, x, Brightness.from_str(brightness))

    # first 2
    for i in range(2):
        #print(f'{i})')
        image = image.enhance(algorithm)
        #image.print()
    print(f'Part1: {image.lit_pixels_count()}')

    # next 48
    for i in range(50 - 2):
        image = image.enhance(algorithm)
    print(f'Part2: {image.lit_pixels_count()}')
