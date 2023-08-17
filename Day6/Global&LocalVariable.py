# Example 1:
# global_var=20  # global variable
#
# def func():
#     local_var=10  # local variable
#     print(local_var)
#     print(global_var)
#
# func()
# #
# # print(local_var) # invalid bcoz local_var is local variable of func()
# print(global_var) # valid bcoz global_var is global variable access any where

# Example 2:
# xy=100 # global variable
#
# def cool():
#     xy=200 # local variable
#     print(xy)   #200
# cool()

# Example 3:
# xy=100 # global variable
#
# def cool():
#     # global xy=200 # invalid syntax
#     global xy
#     xy=200 # global variable
#     print(xy)   #200
# cool()
# print(xy)

#Example 4:
# x=100
# def cool():
#     global x
#     x=500
#     print(x)
#
# cool()  #500
# print(x)  #100

# Example 5:
#There is no need to declare global variable outside the function.
#you can declare them global inside the function - globle
# def cool():
#     global x
#     x=100
#     print(x)
# cool()
# print(x)  # able to acceaa x bcoz it is global variable