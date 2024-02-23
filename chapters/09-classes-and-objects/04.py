class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def length(self):
        return 2 * (self.a + self.b)
    
    def area(self):
        return self.a * self.b

class Squre(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)

rec1 = Rectangle(2, 3)
print(rec1.area())

rec2 = Rectangle(4, 5)
print(rec2.length())

squ1 = Squre(4)
print(squ1.area())
