# Example 1: creating idctionary
# mydic={101:'x',102:'y',103:'z'}
# print(mydic)  # {101: 'x', 102: 'y', 103: 'z'}

# Example 2: accessing items from Dictionary
# mydic={
#     "brand": "Hyundai",
#     "model": "110",
#     "year": 2021
# }
# print(mydic['brand']) # Hyundai
# print(mydic['model']) # 110
#
# # using get()
# print(mydic.get("brand")) # Hyundai

# Example 3: change values in dictionary
# mydic={
#     "brand": "Hyundai",
#     "model": "110",
#     "year": 2020
# }
# print(mydic)  # {'brand': 'Hyundai', 'model': '110', 'year': 2020}
# mydic["year"]=2021  # new value
# print(mydic)  # {'brand': 'Hyundai', 'model': '110', 'year': 2021}

# Example 4: reading dictionary using loop
# mydic={
#     "brand": "Hyundai",
#     "model": "110",
#     "year": 2020
# }
#
# for i in mydic:
#     print(i) # it prints only keys from dictionary
#
# for i in mydic.keys():
#     print(i) # it prints only keys from dictionary
#
# for i in mydic:
#     print(mydic[i])  # it prints only values from dictionary
#
# for i in mydic.values():
#     print(i)   # it prints only values from dictionary
#
# for x,y in mydic.items():
#     print(x,y) # it prints keys alomg with values

# Example 5: check key is exist in dictionary or not
# mydic={
#     "brand": "Hyundai",
#     "model": "110",
#     "year": 2020
# }
# if 'model' in mydic:
#     print("exist")  # true
# else:
#     print("not exist")

# print('model' in mydic) # true

# Example 6: Find number of items in dictionary len()
# mydic={
#     "brand": "Hyundai",
#     "model": "110",
#     "year": 2020
# }
# print(len(mydic)) # 3

# Example 7: adding items to dictionary
# mydic={
#     "brand": "Hyundai",
#     "model": "110",
#     "year": 2020
# }
#
# mydic["color"]='red'
# print(mydic)  # {'brand': 'Hyundai', 'model': '110', 'year': 2020, 'color': 'red'}

# Example 8: Remove otem from dictionary
# mydic={
#     "brand": "Hyundai",
#     "model": "110",
#     "year": 2020
# }
# mydic.pop('year')
# print(mydic) # {'brand': 'Hyundai', 'model': '110'}

# del mydic['year']
# print(mydic) # {'brand': 'Hyundai', 'model': '110'}

# del mydic
# print(mydic)  # NameError: name 'mydic' is not defined

# mydic.clear()
# print(mydic) # {}

# Example 9: copy Dictionary
# mydic1={
#     "brand": "Hyundai",
#     "model": "110",
#     "year": 2020
# }
# without using copy()
# mydic2=mydic1
# print(mydic2) # {'brand': 'Hyundai', 'model': '110', 'year': 2020}

# using copy()
# mydic2=mydic1.copy()
# print(mydic2) # {'brand': 'Hyundai', 'model': '110', 'year': 2020}