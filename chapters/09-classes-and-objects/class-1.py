class Rectangle:
    a = None
    b = None

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def print_area(self):
        print(self.area())


r = Rectangle(2, 3)
area_r = r.area()

p = Rectangle(5, 6)
p.print_area()
