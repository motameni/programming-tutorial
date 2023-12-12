class Pen:
    color = None
    brand = None
    has_door = None
    is_door_open = False
    
    def __init__(self, color, brand, had_door):
        self.color = color
        self.brand = brand
        self.has_door = had_door
        
    def get_color(self):
        return self.color
    
    def doorStatus(self):
        if self.is_door_open:
            return "The %s pen door is open!" % self.color
        else:
            return "The %s pen door is closed!" % self.color

    def openDoor(self):
        if self.is_door_open == False:
            self.is_door_open = True
        else:
            print("The pen door is already open!")
        
    def closeDoor(self):
        if self.is_door_open == True:
            self.is_door_open = False
        else:
            print("The pen door is already close!")

red_pen = Pen("red", "beak", True)
blue_pen = Pen("blue", "panten", True)

print(red_pen.get_color())
print(blue_pen.get_color())

print(red_pen.doorStatus())
red_pen.openDoor()
red_pen.openDoor()
print(red_pen.doorStatus())
