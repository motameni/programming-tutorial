class Shape:
    name: str
    edge_count: int
    
    def __init__(self, name, edge_count):
        self.name = name
        self.edge_count = edge_count
    
class Triagle(Shape):
    def __init__(self):
        super().__init__("Triangle", 3)

class Square(Shape):
    edge_lenght: float
    
    def __init__(self, edge_lenght):
        super().__init__("Square", 4)
        self.edge_lenght = edge_lenght
        
    def lenght(self):
        return self.edge_lenght * 4
    
    def area(self):
        return self.edge_lenght ** 2
        
square = Square(edge_lenght=3.2)

print(square.area())
