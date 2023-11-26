class Adam:
    name: str
    age: int
    wieght: int
    height: int
    
    def __init__(self, name, age, wieght, height):
        self.name = name
        self.age = age
        self.wieght = wieght
        self.height = height
    
    def get_age_in_days(self):
        return self.age * 365
    
    def increase_age(self, years=1):
        self.age += years

ali = Adam(age=31, name="Ali", height=178, wieght=100)
erfaneh = Adam("Erfaneh", 24, 67, 158)

ali.increase_age()

adams = [ali, erfaneh]

print("---------------")
for adam in adams:
    print("Name:", adam.name)
    print("Age:", adam.age)
    print("Age in days:", adam.get_age_in_days())
    print("Weight:", adam.wieght)
    print("Height:", adam.height)
    print("---------------")
