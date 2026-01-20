class Instructor:
    def __init__(self,instructor_name,address):
        self.name=instructor_name
        self.address=address
        self.follower=0
instructor1=Instructor("jenny","gurgaon")
instructor2=Instructor("jimmy","mumbai")

print(instructor1.address)
print(instructor2.address)