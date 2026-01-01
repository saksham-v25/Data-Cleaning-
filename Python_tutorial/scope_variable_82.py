# a=10  #Global variable
# def display():
#     a=15  #Local variable
#     print(a)
#
# display()

def display():
    a=15  #Local variable
    def show():
        print(a)
    show()
display()
