class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")

point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 1
print(point2.x)

#N.B: we use calss to define new,these type can have method that we define in the body of the class
#and they can also have attribute that we can set anywhere in our project.