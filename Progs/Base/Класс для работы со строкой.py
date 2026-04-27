class StringVar():
    data = ""
    def __init__(self, newData):
        self.data = newData
        print(self.data)
    def set(self, newData):
        self.data = newData
    def get(self):
        return self.data
myString = StringVar("О дивный, новый мир!")
myString.set("О давний, новый мир!")
print(myString.get())
