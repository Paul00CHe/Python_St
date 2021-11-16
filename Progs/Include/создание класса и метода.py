class Cat():
    name = ""
    color = ""
    weight = ""
    # конструктор ввода имени при создании класса
    def __init__(self, newName):
        self.name = newName
        print("Родилось животное", self.name)
    # вводит новое имя
    def setName(self, newName):
        self.name = newName
    # выводит текущее имя
    def getName(self):
        return self.name
    def eat(self):
        print("Ням-ням")
    def meow(self):
        print(self.name, "мяукает!")
myCat = Cat("Барсик")
# myCat.name = "Барсик"
# myCat.color = "черный"
# myCat.weight = 10
myCat.meow()
myCat.eat()
myCat.setName("Мурзик")
print(myCat.getName())
myCat.meow()
