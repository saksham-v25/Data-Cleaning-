#calculate circumerence of cicle

class circle :

    pie=3.14
    def __init__(self,radius):
        self.radius=radius
        self.area=circle.pie*radius*radius

    def get_circumference(self):
        return 2 * circle.pie *self.radius


circle_1=circle(4)
print(f"The circumference of circle_1 {circle_1.get_circumference()}")

print(f"The area of circle {circle_1.area}")