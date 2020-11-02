
class Point:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __mul__(self, other):
        return Point(self.x * other.x,
                     self.y * other.y,
                     self.z * other.z)


if __name__ == "__main__":
    p1 = Point(1, 2, 3)
    p2 = Point(1, 2, 3)
    p3 = p1 * p2
    print(p3.x, p3.y, p3.z)
