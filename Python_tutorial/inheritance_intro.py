class vehicle():
    def __init__(self,brand):
        self.brand=brand

    def show_info(self):
        print(f"Brand :{self.brand}")

class car(vehicle):

    def __init__(self,brand):
        super().__init__(brand)
        self.door=4

    def show_detail(self):
        print(f"Doors : {self.door}")


c=car("Toyota")
c.show_info()
c.show_detail()





