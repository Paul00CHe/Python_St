class Animal():
    name = ""
    def __init__(self):
        print("Родилось животное")
    def eat(self):
        print("Ням-ням")
    def setName(self, newName):
        self.name = newName
    def getName(self):
        return self.name
    def makeNoise(self):
        print(self.name, "говорит Гррр")
class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Родился кот")
    def makeNoise(self):
        print(self.name, "говорит Мяу")
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Родилась собака")
    def makeNoise(self):
        print(self.name, "говорит Гав")
myCat = Cat()
myCat.name = "Маркиз"
myCat.eat()
myCat.makeNoise()
myDog = Dog()
myDog.name = "Рекс"
myDog.eat()
myDog.makeNoise()
myAnimal = Animal()
myAnimal.name = "Буль"
myAnimal.eat()
myAnimal.makeNoise()
