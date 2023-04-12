
class person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def myFunction(self):
        print("My name is :", self.name)
        print("My Age is :", self.age)

    def myCity(self):
        print("My Place : ", self.city)

# name = input("Enter your name : ")
# age = int(input("Enter your age : "))

p1 = person("Sundar Rajan", "40", "Fairfax")
#p1 = person(name, age)
p1.myFunction()
p1.myCity()




