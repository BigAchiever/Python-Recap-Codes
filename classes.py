class PowerPoint:  # The First letter should always be capital
    def move(self):
        print("move")

    def draw(self):
        print("draw")


PowerPoint1 = PowerPoint()  # Creating an object and storing the value in one variable
PowerPoint1.x = 10
PowerPoint1.draw()
print(PowerPoint1.x)

Point2 = PowerPoint()  # creating another object using the class only
Point2.x = 2  # every object have their own instance they are not related to one another
print(Point2.x)