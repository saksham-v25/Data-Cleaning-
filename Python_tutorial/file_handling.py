# read function
#
#  f=open('file.txt','r')
#  data=f.read()
#  print(data)
#
#  f=open('file.txt') another method to read file
#  data=f.read()
# print(data)
#
#
#
# write function
#  w=open('file2.txt.tx','w')
#  w.write("wlecome to the python ")
#  print(w.read())             #This line will give error beacause in write function we are trying to access read funtcion


# r+ In this mode,open the file in both read and write mode, file handler exists at the beginning,raises i/o error if file doesnot exists
# f1=open('file.txt','r+')
# print(f1.tell())
# f1.write('hi')
# print(f1.read())
# print(f1.tell())
# f1.write('this is python course ')
# print(f1.tell())


#w+ Open file in both read and write mode ,the file handler exists at the beginning of file,it overwrite previous content of the opened file if the file already exists ,it create a new file if no file exists
# f1=open("file.txt","w+")
# print(f1.tell())
# f1.write("Hi Welcome")
# print(f1.tell())
# f1.write("This is python course")
# print(f1.tell())
# f1.seek(0)
# print(f1.tell())
# data=f1.read()
# print(data)
# print(f1.tell())
# f1.close()


#a open file in append /write mode. The file handler exists at the end of the previously written file if file already exists.if file doesnot exists ,it create a new file. The newly written text will be added at the end of the file
# f1=open("file.txt","a")
# print(f1.tell())
# f1.seek(0)
# f1.write("jenny's lecture")
#a+ open file for both append/write and read. file handler execute at the ned of the file already exists or it will execute aa new file if file doesot exits

f1=open("file.txt","a+")
print(f1.tell())
f1.seek(0)
print(f1.tell())
f1.write("jenny's lecture")

