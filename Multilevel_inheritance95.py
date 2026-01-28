class Human():
    def __init__(self,num_heart):
        print("Calling init form human class ")
        self.eye=2
        self.heart=num_heart
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")


class Male(Human):
    def __init__(self,name):
        print("Calling init from Male class")
        self.name=name
    def sleep(self):
        print("I can sleep whole day ")


class Boy(Male):

    def __init__(self,heart,name,can_dance):
        print("Calling init form Boy class")
        Human.__init__(self,heart)
        Male.__init__(self, name)
        self.know_dancing=can_dance
    def work(self):
        #Human.work(self)
        super().work()
        print("I can test")



B1=Boy(1,"karn",True)
B1.work()
print(B1.name)
print(B1.know_dancing)
print(Boy.mro())




