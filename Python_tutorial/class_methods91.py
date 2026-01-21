
class instructor:

    followers=0  # class object variable
    def __init__(self,name,address):
        self.name=name
        self.address=address

    def display(self,subject_name):
        print(f"Hi , I am {self.name} and i teach {subject_name} ")


instructor1=instructor("jimmy","delhi")
print(instructor1.name)
instructor1.display("python")