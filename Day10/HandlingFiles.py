#Example 1: writing data in to file
# file=open("C:\DemoFiles\myfile.txt.txt",'w')
# file.write("this is my first statement...\n")
# file.write("this is my second statement...\n")
# file.write("this is my third statement...\n")
# file.write("this is my fourth statement....\n")
# file.write("this is my fifth statement....\n")
# file.close()
# print("program completed.......")

#Example 2: Reading data in the file
# file=open("C:\DemoFiles\myfile.txt.txt",'r')
# print(file.read())
# #print(file.readline())
# file.close()

#Example 3: appending data into text file
file=open("C:\DemoFiles\myfile.txt.txt",'a')
file.write(("\nthis is my sixth line..\n"))
file.write("this is my seventh line..\n")
file.close()
print("program is completed....")