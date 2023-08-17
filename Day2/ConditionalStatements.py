# conditional statements
#        if           if else      elif

#Example 1: Print a person is eligible for vote or not
# age>=18

# age=20
# if age>=18:
#     print("Eligible for vote")
# else:
#     print("Not Eligible for vote")

#Example 2:
# if True:
#     print("true condition")
# else:
#     print("false condition")

#Example 3:
# if 1:
#     print("one")
# else:
#     print("Not one")

# Example 4: Find a number is even/odd
# num=10
# if num%2==0:
#     print("number is even")
# else:
#     print("number is odd")

#Example 5: if else in single line (ternary operator)
# num=15
# print("Even number") if num%2==0 else print("odd number")

#Example 6: is else - Multiple statements in single line
# a=20
# {print("hello"),print("python")} if a>=10 else {print("hi"),print("java")}

#Example 7: Multiple condition using elif
weekno=7
if weekno==1:
    print("sunday")
elif weekno==2:
    print("monday")
elif weekno==3:
    print("tuesday")
elif weekno == 4:
    print("wednesday")
elif weekno == 5:
    print("thursday")
elif weekno == 6:
    print("friday")
elif weekno == 7:
    print("saturday")
else:
    print("invalid week number")
