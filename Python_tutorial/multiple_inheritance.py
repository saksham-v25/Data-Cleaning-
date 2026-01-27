class Human():

    def __init__(self,num_heart):
        print("calling from Human")
        self.num_eyes=2
        self.num_nose=1
        self.num_heart=num_heart
    def eat(self):
        print("I can Eat")
    def work(self):
        print("I can Work")

class Male():
    print("Calling from Male")
    def __init__(self,name):
        self.name=name
    def flirt(self):
        print("I can Flirt")
    def work(self):
        print("I can Code")


class Boy(Human,Male):
    def __init__(self,name,heart,language):
        Human.__init__(self,heart)
        Male.__init__(self,name)
        self.language=language
    def sleep(self):
        print("I can sleep")
    def work(self):
        print("I can test")

    def display(self):
        return print(f"I am {self.name} and I work on {self.language}")



# Boy_1=Boy()
# Boy_1.work()
# print(Boy.mro())  #mro=method resolution order
# Boy.work(Boy_1)



Boy_1=Boy("Karn",1,"python")
Boy_1.display()

