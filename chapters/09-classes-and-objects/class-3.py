class Car:
    engine_status = False

    def __init__(self, brand, color, year, door_numbers, enginee_power):
        self.brand = brand
        self.color = color
        self.year = year
        self.door_numbers = door_numbers
        self.enginee_power = enginee_power

    def drive(self):
        if self.engine_status:
            print("%s Vijjjjjjjjjjjjjjjjjj!" % self.brand)
        else:
            print("%s engine is off! First turn it on!" % self.brand)

    def turn_on(self):
        self.engine_status = True

    def turn_off(self):
        self.engine_status = False


benz = Car("Benz", "Black", 1990, 2, 3000)
bmw = Car("Bmw", "Navy Blue", 2024, 4, 5000)

benz.turn_on()
benz.drive()
benz.turn_off()

bmw.drive()
