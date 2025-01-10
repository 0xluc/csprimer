class Vec:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self: "Vec", other: "Vec") -> "Vec":
        return Vec(self.x + other.x, self.y + other.y)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Vec):
            return False
        return self.x == other.x and self.y == other.y

    def __mul__(self, other):
        if not isinstance(other, int) and not isinstance(self, int):
            raise Exception(
                "Error, multiplication must be done between a vector and an scalar"
            )
        return Vec(self.x * other, self.y * other)

    def __str__(self):
        return f"<{self.x},{self.y}>"

    def __sub__(self, other):
        return self + -other

    def __neg__(self):
        return Vec(-self.x, -self.y)

    def magnitude(self):
        return (self.x**2 + self.y**2) ** 0.5


class Displacement(Vec):
    def move(self, velocity, time):
        self.x = self.x + velocity * time
        self.y = self.y + velocity * time


if __name__ == "__main__":
    v1 = Vec(3, 2)
    v2 = Vec(1, 1)
    v3 = Vec(3, 4)
    assert v1 + v2 == Vec(4, 3)
    assert v1 * 2 == Vec(6, 4)
    assert v1 - v2 == Vec(2, 1)
    assert v1 + v3 + v2 == Vec(7, 7)
    assert v3.magnitude() == 5.0
    d = Displacement(3, 2)
    d.move(1, 2)
    assert (d) == Vec(5, 4)
    print("All tests passed")
