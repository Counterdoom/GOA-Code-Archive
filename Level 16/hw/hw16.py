# cw1
# append(): სიის ბოლოს ამატებს ახალ ელემენტს. არგუმენტი - ახალი ელემენტი ერთი ელემენტი.
# insert(): სიის მითითებულ ინდექსზე ამატებს ახალ ელემენტს. არგუმენტები - ინდექსი, ახალი ელემენტი.
# pop(): სიის მითითებული ინდექსის ელემენტს შლის და აბრუნებს. არგუმენტი - ინდექსი.
# len(): აბრუნებს სიის, სტრინგის ან სხვა ობიექტის ელემენტების რაოდენობას. არგუმენტი - ობიექტი.
# upper(): სტრინგის ყველა სიმბოლოს აქცევს დიდ ასოებად. არგუმენტი - არ აქვს.
# lower(): სტრინგის ყველა სიმბოლოს აქცევს პატარა ასოებად. არგუმენტი - არ აქვს.
# capitalize(): სტრინგის პირველ ასოს აქცევს დიდ ასოდ, ხოლო დანარჩენს პატარა ასოებად. არგუმენტი - არ აქვს.
# find(): აბრუნებს სტრინგში მითითებული პირველ ინდექსს ან -1-ს, თუ არ მოიძებნა. არგუმენტი - სტრინგი.

# cw2
surnames = ["Giorgadze", "Lomidze", "Kavtaradze", "Sharashidze", "Chikovani"]
name = input("David")

if len(name) > 7:
    surnames.append(name)
    print(surnames)
else:
    print("სახელი ძალიან მოკლეა")

# cw3
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = [numbers[i] for i in range(0, len(numbers), 2)]
print(numbers)

# cw4
string_variable = "HOMEWORK 16 TEST STRING"
print(len(string_variable))

# cw5
name = "David Manguashvili"
print(name.lower())

# cw5
surname = "matchavariani"
print(surname.upper())

# cw6
example_string = "example string"
print(example_string.capitalize())
