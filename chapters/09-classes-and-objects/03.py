class Circle:
    _r = None

    def __init__(self, r):
        self._r = r

    def radius(self):
        return self._r

    def length(self):
        return 2 * 3.14 * self._r

    def area(self):
        return 3.14 * self._r ** 2

    def print(self):
        print("Radius: %.2f, Length: %.2f, Area: %.2f" % (self.radius(), self.length(), self.area()))


for radius in range(1, 100):
    circle = Circle(radius)
    circle.print()
