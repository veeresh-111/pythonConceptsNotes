# Example 1:
# def func(i,j):
#     print(i,j)
# # func(10,20)  # Positional arguments
# func(j=20,i=10) # Keyword arguments

# Example 2: default values assigned to positional arguments
# def func(i,j=20):
#     print(i,j)
# func(100,200) #100 200
# func(100)    #100 20

# Example 3: Keyword arguments
# def greetings(name,greetmsg):
#     print(greetmsg+" "+name)
# greetings(name='john',greetmsg='hello') # hello john
# greetings(greetmsg='hello',name='john') # hello john

# Example 4:
def my_func(a,b,c):
    print(a,b,c)
# my_func(10,20,30)  # positional arguments
# my_func(a=10,b=20,c=30) # Keyword arguments
# my_func(b=20,a=10,c=30) # keyword arguments
#
# my_func(10,20,c=30) # combination of key and positional arguments
# my_func(10,b=20,c=30)
# my_func(10,b=20,30) # This is wrong as positional arguments must appear before any keyword arguments
# my_func(10,20,b=30) # logical error

# Example 5: Fucntion can return multiple values
def largest(a,b):
    if a>b:
        return a,b
    else:
        return b,a
# print(largest(100,200)) # 200,100
# print(largest(20,10)) # 20,10
#
res=largest(10,20)
print(res)
print(type(res)) #tuple