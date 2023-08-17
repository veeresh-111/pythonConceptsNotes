#Example 1:
# class Myclass:
#     def myfun(self):
#         pass
#     def display(self,name):
#         print(name)
#
# mc1=Myclass()
# mc1.myfun()
# mc1.display('scott')  #scott

#Example 2:
# class Myclass:
#      def m1(self):
#          print("this is instance method....")
#      @staticmethod
#      def m2(self,num):
#          print(self,num)
#
# mc=Myclass()
# mc.m1()
# mc.m2(100,200) # 100 200
#
# Myclass.m2(10,20) # 10, 20 # here calling static method diractly using class not through object

# Example 3:
# class myclass:
#     a,b=10,20 #class variables
#     def add(self):
#         print(self.a+self.b)
#     def mul(self):
#         print(self.a*self.b)
#
# mc=myclass()
# mc.add() #30
# mc.mul()  #200

# Example 4:
# i, j=15,25  # global varables
# class myclass:
#     a,b=10,20  # class variables
#     def add(self,x,y):
#         print(x+y)  # x, y are local variables
#         print(self.a+self.b) # a, b are class variables
#         print(i+j)  # i, j are global variables
#
# mc=myclass()
# mc.add(100,200)

#Example 5:
# a,b=15,25  # global variables
# class myclass:
#     a,b=10,20  # class variables
#     def add(self,a,b):
#         print(a+b)  # a, b are local variables
#         print(self.a+self.b) # a, b are class variables
#         print(globals()['a']+globals()['b'])  # a, b are global variables
#
# mc=myclass()
# mc.add(100,200)

# Example 6: one class can have multiple objects
# class myclass:
#     def display(self,name):
#         print("this is display method.....")
#         print(name)
#
# obj1=myclass()
# obj1.display("john")
#
# obj2=myclass()
# obj2.display('scott')

# Example 7: Constructor example
# class myclass:
#     def __init__(self):
#         print("this is constructor.........")
#     def m1(self):
#         print("this is method....")
#     def m2(self,x,y):
#         return (x+y)
#
# mc=myclass()  # invoke constructor automatically
# mc.m1()  # method we have call explicitly by using object
# print(mc.m2(10,20))  #30


# Example 8:
# class myclass:
#     name='john'
#     def __init__(self,name): # here constructor axpecting one argument
#         print(name)
#         print(self.name)
#
# mc=myclass("david") # passing parameter to the constructor

# Example 9:
# Req: Emp
     # constructor : eid, ename, sal
     # display() : print eid, ename, & sal

# class Emp:
#     def __init__(self,eid,ename,sal):
#         self.eid=eid
#         self.ename=ename
#         self.sal=sal
#     def display(self):
#         print(self.eid,self.ename,self.sal)
#
# e1=Emp(101,'john',500000)
# e1.display()
#
# e2=Emp(102,'scott',70000)
# e2.display()

# Example 10:
# Req: Emp
     # constructor : eid, ename, sal
     # constructor : print eid, ename, & sal

# class Emp:
#     def __init__(self,eid,ename,sal):
#         self.eid=eid
#         self.ename=ename
#         self.sal=sal
#     def __str__(self):   # it only return string type of values
#         return(self.ename)
#
# e1=Emp(101,'john',500000)
# print(e1)





