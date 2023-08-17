#Example 1: OverLoading (Polymorphism concept)
# class Human:
#     def sayhello(self,name=None):
#         if name is not None:
#             print("hello" +name)
#         else:
#             print("Hello")
#
# h=Human()
# h.sayhello("scott")
# h.sayhello()

# Example 2:
class Calculation:
    def add(self,a=0,b=0,c=0):
        print(a+b+c)

calobj=Calculation()
calobj.add()  # 0
calobj.add(10,20)  # 30
calobj.add(100,200,300) # 600

