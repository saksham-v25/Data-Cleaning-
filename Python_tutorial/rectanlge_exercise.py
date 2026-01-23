#calculate the perimeter of reactangle
class rectangle:

    def __init__(self,base,height):
        self.height=height
        self.base=base

    def get_perimeter(self):
        return 2 *(self.base + self.height)


rectangle_1=rectangle(3,4)
print(f"The perimeter of rectangle is {rectangle_1.get_perimeter()}")
