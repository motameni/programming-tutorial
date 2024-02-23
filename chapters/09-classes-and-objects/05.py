class Animal:
    def __init__(self, name):
        self.name = name
        
    def make_sound(self):
        pass
    
    def say_hello(self):
        print("Hello!")
        
class Cat(Animal):
    def make_sound(self):
        print("Miawwwww!")

class Dog(Animal):
    def make_sound(self):
        print("Hooooop!")

class Human(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        
    def make_sound(self):
        print("Hellooooo! I am Human!")
    
    def walk(self):
        print("I am walking!")

# cat1 = Cat("Milo")
# cat1.say_hello()
# cat1.make_sound()

# dog1 = Dog("Charlie")
# dog1.say_hello()
# dog1.make_sound()

hum1 = Human("Ali", 31)
hum1.make_sound()
hum1.say_hello()
hum1.walk()
