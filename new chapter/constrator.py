class Point:
    def __init__(self,x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")

point = Point(10, 20)
print(point.x)

###################################### exercise

class Person:
    def __init__(self,name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")

person1 = Person('emmy')
person1.talk()

john = Person('john smith')
john.talk()