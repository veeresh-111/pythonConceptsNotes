# Example 1:
# class A:
#     def m1(self):
#         print("this is m1 method from class A")
#
# class B(A):
#     def m2(self):
#         print("this is m2 method from class B")
#
# bobj=B()
# bobj.m1()   #this is m1 method from class A
# bobj.m2()   #this is m2 method from class B

# Example 2: Single level Inheritence
# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B(A):
#     a,b=200,100
#     def m2(self):
#         print(self.a-self.b)
#
# bobj=B()
# bobj.m1()   # 30
# bobj.m2()    # 100

# Example 3: Multi level Inheritence
# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B(A):
#     a,b=200,100
#     def m2(self):
#         print(self.a-self.b)
# class C(B):
#     i,j=5,2
#     def m3(self):
#         print(self.i*self.j)
#
# cobj=C()
# cobj.m1()  # 30
# cobj.m2()  #100
# cobj.m3()  #10

# Example 4: Hierarchy Inheritence
# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B(A):
#     a,b=200,100
#     def m2(self):
#         print(self.a-self.b)
# class C(A):
#     i,j=5,2
#     def m3(self):
#         print(self.i*self.j)
#
# bobj=B()
# bobj.m1()  # 30
# bobj.m2()  #100
#
# cobj=C()
# cobj.m1()  # 30
# cobj.m3()  #10


# Example 5: Multiple Inheritence
# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B:
#     a,b=200,100
#     def m2(self):
#         print(self.a-self.b)
# class C(A,B):
#     i,j=5,2
#     def m3(self):
#         print(self.i*self.j)
#
# cobj=C()
# cobj.m1()  # 30
# cobj.m2()  # 100
# cobj.m3()  #10







