read function

 f=open('file.txt','r')
 data=f.read()
 print(data)

 f=open('file.txt') another method to read file
 data=f.read()
print(data)



write function
 w=open('file2.txt.tx','w')
 w.write("wlecome to the python ")
 print(w.read())             #This line will give error beacause in write function we are trying to access read funtcion


# r+ In this mode,open the file in both read and write mode, file handler exists at the beginning,raises i/o error if file doesnot exists
f1=open('file.txt','r+')
print(f1.tell())
f1.write('hi')
print(f1.read())
print(f1.tell())
f1.write('this is python course ')
print(f1.tell())