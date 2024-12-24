# cw1
name = "saba"
choice = "capitalize"

if choice == "upper":
    print(name.upper())
elif choice == "lower":
    print(name.lower())
elif choice == "capitalize":
    print(name.capitalize())
else:
    print("other")

# cw2
surname = "manguashvili"
if surname.find("shvili"):
    print("როგორ ხარ?")
if surname.find("ia"):
    print("მუჭო რექ?")
else:
    print("Bye")

# cw3
names_list = ["nika", "sandro", "tako", "ana", "giorgi"]
new_name = "daviti"

if new_name.find("d" -1, -1) and new_name.find("i", -1, -1):
    names_list.append(new_name)
    print(names_list)
else:
    print("invalid")

# cw4
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_list.pop(8)
print(numbers_list)

# cw5
food_list = ["pizza", "burger", "salad", "pasta", "soup"]
number = 7
food = "chicken"
food_list.insert(number, food)
print(food_list)
