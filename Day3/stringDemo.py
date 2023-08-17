# create string variable

# Example 1: ways of creating string variable
# s="welcome"
# s='welcome'
# s=str("welcome")
# s=str('welcome')

#creating empty string variable
# name=""
# name=''
# name=str()

# Example 2: way of immutable and immutable
# mutable --- cannot change the value of variable
# immutable--  can change the value of the variale
# String is immutable
# if the value is changed after updation then it is immutable
# str1='welcome'
# print(id(str1))
# #
# str1=str1+"to python"
# print(id(str1))

# Example 3: + and * with string
# str='welcome'
# print(str+"to python") #  welcometo python
# print(str*3)   #   welcomewelcomewelcome

# Example 4: slicing []
# starting index 0
# ending index 1

# str='welcome'
# print(str[1:3])  # el
# print(str[:6])   #  welcom
# print(str[2:])   # lcome
# print(str[1:-1])  #   elcom
# print(str[1:-2])   #  elco


# Example 5: ord() and chr()
# print(ord('A')) #  65 returns ASCII values of A
# print(chr(65))  # A

# Example 6: max() min() len()
# print(max('abc'))  # c
# print(min('abc'))  # a
# print(len('welcome'))  # 7

# Example 7: in, not in operator -- return true/false
# s='welcome'
# print('come' in s) # true
# print('lome' in s) # false
#
# print('come' not in s) # false
# print('lome' not in s) # true

# Example 8: String comparision
# print('tim' == 'tie') #false
# print('free' != 'freedom') #true
# print('arrow' > 'aron') #true
# print('right' >= 'left') #true
# print('teeth' < 'tee') #false
# print('yellow' <= 'fellow') # false
# print('abc' > '') # true

# Example 9: Testing string true/false
# s='welcome to python 123'
# print(s.isalnum()) #false
# print('welcome'.isalpha()) #true
# print('2012'.isdigit())  #true
# print("first Number".isidentifier()) #false
# print(s.islower()) #true
# print('WELCOME'.isupper()) #true
# print(" ".isspace()) #true

# Example 10: searching for substring
# s='welcome to python'
# print(s.endswith('thon')) #true
# print(s.startswith('good')) #false
# print(s.find('come')) # 3
# print(s.find('become')) # -1 -- not found
# print(s.count('t')) #  2 -- count number of time this char is repeated in string

# Example 11: convertig string
# s='String in PYTHON'
# s1=s.capitalize()
# print(s1)     # String in python
#
# s2=s.title()
# print(s2)     # String In Python
#
# s3=s.lower()
# print(s3)     # string in python
#
# s4=s.upper()
# print(s4)     # STRING IN PYTHON
#
# s5=s.swapcase()
# print(s5)    # sTRING IN python
#
# s6=s.replace('in','on')
# print(s6)  # Strong on PYTHON

# interview quastion
# Example 12: reverse a given string
# method 1
# s='welcome'
# rev_str="" # w, ew, lew, clew, oclew, moclew, emoclew
# for i in s:
#     rev_str=i+rev_str #  w+"", e+w , l+ew, c+lew, o+clew, m+oclew, e+moclew
# print("reversed string is:",rev_str)  # emoclew
#
# # methon 2
s='welcome'
rev_str=s[::-1]
print("reversed string is:",rev_str) # emoclew



