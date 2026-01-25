#calculate the perimeter of square
#calculate the area of square
#calculate the diagonal of square
import math
class sqaure:

    def __init__(self,side):
        self.side=side

    def get_perimeter(self):
        return 4*self.side

    def get_area(self):
        return self.side * self.side

    def get_diagonal(self):
        return math.sqrt(2) * self.side


sqaure_1=sqaure(3)
print(f"The perimeter of rectangle is {sqaure_1.get_perimeter()}")
print(f"The perimeter of rectangle is {sqaure_1.get_area()}")
print(f"The perimeter of rectangle is {sqaure_1.get_diagonal()}")