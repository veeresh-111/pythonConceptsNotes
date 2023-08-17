# Example 1: How to create list

mylist1=[10,40,30,60,70,70]
mylist2=["apple",'banana','cherry','banana']
mylist3=["apple",20,"banana",30]
mylist=list() #empty list

print(mylist1)
print(mylist2)
print(mylist3)
print(mylist)

# Example 2: Accessing item from the list
# mylist = ["apple", 'banana', 'cherry']
#
# print(mylist[0])
# print(mylist[2])
# print(mylist[-1])
# print(mylist[-2])

# Example 3: Range of indexes
# mylist = ["apple", 'banana', 'cherry','orange','kiwi','melon','mango']
# print(mylist[2:5])  # ['cherry', 'orange', 'kiwi']
# print(mylist[-4:-1]) # ['orange', 'kiwi', 'melon']

# Example 4: Change item of values
# mylist=['apple','banana','cherry']
# print(mylist) # ['apple', 'banana', 'cherry']
# mylist[0]='orange'  # --it will change value on index basis
# print(mylist)  # ['orange', 'banana', 'cherry']

# Example 5: read list items by using loop
# mylist=['banana',"apple",'cherry',80,50]
# for i in mylist:
#     print(i)

# Example 6: check if the item is present in the list or not
# mylist=["apple",'banana','cherry']
# if 'apple' in mylist:
#     print('yes, cherry is present')
# else:
#     print("No, cherry is not present")

# Example 7: list length (counting number of items in a list)
# mylist=['apple','banana','cherry']
# print(len(mylist)) # 3

# Example 8: add new item in the list append() and insert()
# mylist=['apple','banana','cherry']
# mylist.append("orange")  # this add new value at end of list
# print(mylist)  # ['apple', 'banana', 'cherry', 'orange']
# mylist.insert(1,'kiwi')  # this add new item on indexed mentioned
# print(mylist)

# Example 9: Remove item from the list
#pop()
# mylist=['apple','banana','cherry']
# mylist.pop(0)   # here remove item on index basis
# print(mylist) # ['banana', 'cherry']

#del
# mylist=['apple','banana','cherry']
# del mylist[2]   # del will remove item based on index
# print(mylist)  # ['apple', 'banana']

# clear
# mylist=['apple','banana','cherry']
# mylist.clear()  # it will clear all items in the list
# print(mylist) # []

# Example 10: copy one list into another list
# approach 1 by using list()
# mylist1=['apple','banana','cherry']
# mylist2=list(mylist1)
# print(mylist1)  # ['apple', 'banana', 'cherry']
# print(mylist2)  # ['apple', 'banana', 'cherry']

# copy()
# mylist1=['apple','banana','cherry']
# mylist2=mylist1.copy()
# print(mylist1)  # ['apple', 'banana', 'cherry']
# print(mylist2)  # ['apple', 'banana', 'cherry']

#Example 11: combine lists
# using + operator
# list1=['a','b','c']
# list2=[1,2,3]
# list3=list1+list2
# print(list3)  #  ['a', 'b', 'c', 1, 2, 3]

#using loop statement
# list1=['a','b','c']
# list2=[1,2,3]
# for i in list2:
#     list1.append(i)
# print(list1)  # ['a', 'b', 'c', 1, 2, 3]

# using extend()
# list1=['a','b','c']
# list2=[1,2,3]
# list1.extend(list2)
# print(list1)  # ['a', 'b', 'c', 1, 2, 3]

# Example 12: lists compare
# list1=[10,20,30,50]
# #list2 = ['a', 'b', 'c']
# list2=[10,20,30,60]
# if list1 == list2:
#     print("lists are equal")
# else:
#     print("lists are not equal")