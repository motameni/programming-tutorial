class Adam:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_greeting(self):
        print("Hello! My name is " + self.name)


a = Adam("Ali", 31)
a.say_greeting()

n = Adam("Nadiya", 33)
n.say_greeting()

am = Adam("AmirAli", 21)
am.say_greeting()
