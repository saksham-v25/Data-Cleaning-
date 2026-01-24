#calculate the perimeter of square
class sqaure:

    def __init__(self,side):
        self.side=side

    def get_perimeter(self):
        return 4*self.side


sqaure_1=sqaure(3)
print(f"The perimeter of rectangle is {sqaure_1.get_perimeter()}")
