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

    def __mul__(self, other: int):
        return Vec(self.x * other, self.y * other)


if __name__ == "__main__":
    v1 = Vec(3, 2)
    v2 = Vec(1, 1)
    assert v1 + v2 == Vec(4, 3)
    assert v1 * 2 == Vec(6, 4)
    print("All tests passed")
