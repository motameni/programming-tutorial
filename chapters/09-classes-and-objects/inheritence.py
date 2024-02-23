class Shape:
    name = "unnamed"

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def print_name(self):
        print(self.get_name())

    def length(self):
        pass

    def print_length(self):
        print(self.length())

    def area(self):
        pass

    def print_area(self):
        print(self.area())

    def print(self):
        d = "\n-------------------------\n"
        print("%s%s: length: %.2f, area: %.2f%s" % (d, self.get_name(), self.length(), self.area(), d))

    def __str__(self):
        return "%s (length: %.2f, area: %.2f)" % (self.get_name(), self.length(), self.area())


class Rectangle(Shape):

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.set_name("rectangle")

    def length(self):
        return (self.a + self.b) * 2

    def area(self):
        return self.a * self.b


class Square(Rectangle):

    def __init__(self, a):
        super().__init__(a, a)
        self.set_name("square")


class Circle(Shape):

    def __init__(self, r):
        self.r = r
        self.set_name("circle")

    def length(self):
        return 2 * 3.14 * self.r

    def area(self):
        return 3.14 * self.r ** 2


class Triangle(Shape):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.set_name("triangle")

    def length(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.length() / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5


rectangle = Rectangle(2, 3)
rectangle.print()

circle = Circle(5)
circle.print()

square = Square(2)
square.print()

triangle = Triangle(3, 4, 5)
triangle.print()
print(triangle)
