# Example 1: calling parent class method using child class(super())
# class A:
#     def m1(self):
#         print("this is m1 method from class A")
# class B(A):
#     def m1(self):
#         print("this is m1 method from class B")
#         super().m1()        # this is m1 method from class A
#
# bobj=B()
# bobj.m1()  #this is m1 method from class B

#Example 2: OverRiding concept
# class A:
#    a,b=10,20
#
# class B(A):
#     i,j=100,200
#     def m(self,x,y):
#         print(x+y)   # local variable
#         print(self.i+self.j) # class variables from class B
#         print(self.a+self.b) # class variables from class A
#
# bobj=B()
# bobj.m(1000,2000) # 3000 , 300, 30

# Example 3: Overriding variables
# class Parent:
#     name='Scott'
#
# class Child(Parent):
#     name = 'john'  # Overriding the variable value
#
# cobj=Child()
# print(cobj.name)  #john

# Example 4: Overriding Methods
class Bank:
    def rateofInterest(self):
        return 5

class XBank(Bank):
    def rateofInterest(self):
        return 10

class YBank(Bank):
    def rateofInterest(self):
        return 12

objx=XBank()
print(objx.rateofInterest()) # 10

objy=YBank()
print(objy.rateofInterest()) #12