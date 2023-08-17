# Example 1: creating set
# myset={'apple','banana','cherry'}
# print(myset) # {'apple', 'cherry', 'banana'}

# Example 2: Accessing items from set
# myset={'apple','banana','cherry'}
# for i in myset:
#     print(i)

# Example 3: Value exist in the set or mot
# myset = {'apple', 'banana', 'cherry'}
# print("banana" in myset)  #true
# print("banana2" in myset)  # false

# Example 4: adding item to set
# add()- add single item  update()-- add multiple item
# myset = {'apple', 'banana', 'cherry'}
# myset.add("orange") # add single item
# myset.update(['mango','graphs']) # add multi item
# print(myset) # {'orange', 'banana', 'apple', 'cherry'} # {'apple', 'graphs', 'banana', 'mango', 'cherry'}


# Example 5: find number of items in a set len()
# myset = {'apple', 'banana', 'cherry'}
# print(len(myset)) # 3

# Example 6: remove item from set -- remove() and discord()
# myset = {'apple', 'banana', 'cherry'}
# myset.remove('banana')
# print(myset)  # {'apple', 'cherry'}
# myset.remove('xyz')  # KeyError: 'xyz' if remove item not in the set

# myset.discard('banana')
# print(myset) # {'apple', 'cherry'}
# myset.discard('xyz')  # it will not through error

# Example 7: clear all item from the set
# myset = {'apple', 'banana', 'cherry'}
# myset.clear()
# print(myset) # set()
#
# del myset
# print(myset) # NameError: name 'myset' is not defined

# Example 8: join 2 sets  -- union()
# set1={'a','b','c'}
# set2={1,2,3}
# set3=set1.union(set2)
# print(set3)  # {1, 'a', 2, 3, 'c', 'b'}

 # using update()
# set1={'a','b','c'}
# set2={1,2,3}
 # set1.update(set2)
 # print(set1)  #  # {1, 'a', 2, 3, 'c', 'b'}


