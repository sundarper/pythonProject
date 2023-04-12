
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myFunction(self):
        print("My name is :", self.name)
        print("My Age is :", self.age)

p1 = person("Sundar Rajan", "40")

p1.myFunction()

