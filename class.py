from Lists import names


class Point:
    def move(self):
        print("move")
    def draw(self):
        print("draw")
point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x, point1.y)
point1.draw()


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, i am {self.name}")


zubaet = Person("zubaet ahmed")
print(zubaet.name)
zubaet.talk()


class asdfg:
    def walk(self):
        print("walk")
class Dog(asdfg):
    pass
class Cat(asdfg):
    pass
dog = Dog()
dog.walk()
cat = Cat()
cat.walk()

class asdfg:
    def walk(self):
        print("walk")
class Dog(asdfg):
    def bark(self):
        print("bark")
class Cat(asdfg):
    def be_annoying(self):
        print("annoying")
dog = Dog()
dog.bark()
cat = Cat()
cat.be_annoying()