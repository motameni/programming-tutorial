class Adam:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sayGreeting(self):
        print("Hello! My name is " + self.name)

a = Adam("Ali", 31)
a.sayGreeting()

n = Adam("Nadiya", 33)
n.sayGreeting()

am = Adam("AmirAli", 21)
am.sayGreeting()
