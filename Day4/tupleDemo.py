# Example 1: creating tuple
mytuple=('apple','banana','apple','cherry')
print(mytuple)  # ('apple', 'banana', 'cherry')
# mytuple=()  # empty tuple

#Example 2: access tuple items
# mytuple=('apple','banana','cherry')
# print(mytuple[1])  # banana
# print(mytuple[-1])  # cherry

# Example 3: Range of indexes
# mytuple=('apple','banana','cherry','orange','kiwi','melon','mango')
# print(mytuple[2:5]) # ('cherry', 'orange', 'kiwi')
# print(mytuple[-4:-1]) # ('orange', 'kiwi', 'melon')

# Example 4: Changing tuple items
# by default tuple does not allow you change values because it is immutable
# but there is work around
# tuple---> list(modify)--> tuple  type casting from tuple to list then tuple

# mytuple=('apple','banana','cherry')
# mylist=list(mytuple)
# mylist[0]='orange'
# mytuple=tuple(mylist)
# print(mytuple) #  ('orange', 'banana', 'cherry')

# Example 5: Reading tuple items using loop
# mytuple=('apple','banana','cherry')
# for i in mytuple:
#     print(i)

# Example 6: check if item is present in the tuple
# mytuple = ('apple', 'banana', 'cherry')
# if "banana" in mytuple:
#     print("yes, banana is present")
# else:
#     print("No, banana is not present")

# Example 7: tuple length -- counting items in a tuple
# mytuple = ('apple', 'banana', 'cherry')
# print(len(mytuple))  # 3

# Example 8: add item to tuple - not possible bcoz tuple is immutable - cannot change values/items
# mytuple = ('apple', 'banana', 'cherry')
# mytuple[0]='orange'  # TypeError: 'tuple' object does not support item assignment
# print(mytuple)

# Example 9: copy tuples
# mytuple1 = ('apple', 'banana', 'cherry')
# mytuple2 = mytuple1
# print(mytuple2)  # ('apple', 'banana', 'cherry')

# Example 10: Remove item from the tuple -- not possible bcoz tuple is immutaple
mytuple = ('apple', 'banana', 'cherry')
# mytuple.remove('apple') # AttributeError: 'tuple' object has no attribute 'rem
# del mytuple
# print(mytuple) # NameError: name 'mytuple' is not defined

# Example 11: join/combine tuple
# tuple1=(10,20,30)
# tuple2=('a','b','c')
# tuple3=tuple1+tuple2
# print(tuple3)  # (10, 20, 30, 'a', 'b', 'c')

# Example 12: tuples compare
# tuple1=(10,20,30)
# #tuple2 = ('a', 'b', 'c')
# tuple2=(10,20,30)
# if tuple1 == tuple2:
#     print("tuples are equal")
# else:
#     print("tuples are not equal")


