from functools import singledispatchmethod

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    @singledispatchmethod
    def move(self, d: "Point") -> "Point":
        x = self.x + d.x
        y = self.y + d.y
        return Point(x, y)

    @move.register
    def _(self, dx: int, dy: int):
        self.x += dx
        self.y += dy

    def __eq__(self, __value: object) -> bool:
        return (self.x == __value.x and self.y == __value.y)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

if __name__ == '__main__':
    p = Point(3, 4)
    v = Point(5, 6)
    m = p.move(v)
    p.move(2, 2)
    print(p)
    print(m)

    assert m.x == 8 and m.y == 10
