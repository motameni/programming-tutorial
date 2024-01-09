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

    def door_status(self):
        if self.is_door_open:
            return "The %s pen door is open!" % self.color
        else:
            return "The %s pen door is closed!" % self.color

    def open_door(self):
        if not self.is_door_open:
            self.is_door_open = True
        else:
            print("The pen door is already open!")

    def close_door(self):
        if self.is_door_open:
            self.is_door_open = False
        else:
            print("The pen door is already close!")


red_pen = Pen("red", "beak", True)
blue_pen = Pen("blue", "panten", True)

print(red_pen.get_color())
print(blue_pen.get_color())

print(red_pen.door_status())
red_pen.open_door()
red_pen.open_door()
print(red_pen.door_status())
