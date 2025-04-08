class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        """Magic method that returns a string representation of a Point object"""
        return f"({self.x},{self.y})"

    def dist_from_origin(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    def translate_x(self, dx: float) -> None:
        self.x += dx

    def translate_y(self, dy: float) -> None:
        self.y += dy


pt: Point = Point(2.0, 1.0)

well: Point = Point(2.0, 1.0)
print(well)


class Line:
    start: Point
    end: Point

    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def get_length(self) -> float:
        length: float = self.end.x - self.start.y
        return length

    def __str__(self) -> str:
        """Magic method to print str representation of a line"""
        return f"({self.start.x}, {self.start.y} to {self.end.x}, {self.end.y})"


planet: Point = Point(5.0, 7.0)
my_line: Line = Line(well, planet)
print(my_line)
