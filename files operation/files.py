#!usr/bin/python

#open an file 
f1=open("./f1.txt","w")

#writting into the file
f1.write("this is first line i am writting into this file\n")

#open an existing file in read mode 
f2=open("./f2.txt","r")

#print file contents reading line by line
for i in f2:
 	print(i)

#seeking this file cursor to 0th location of file 
f2.seek(0)

#print file contents reading character by character
for j in f2.read():
	print(j)
f2.seek(0)

#reading from one file and writting into other file
for k in f2:
	f1.write(k)

#closing both the files
f1.close()
f2.close()
