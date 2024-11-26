#hw1
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("even")
else:
    print("odd")

#hw2
for i in range(1, 51):
    if i % 2 == 0:
        print(i)

#hw3
numbers = [4, 7, 12, 15, 3, 9, 18, 22, 8, 6]
for number in numbers:
    if number > 10:
        print(number)

#hw4
numbers = [5, 12, 9, 17, 3, 8, 6, 11, 15, 2]
first = numbers[0]
last = numbers[-1]

difference = first - last
total = first + last
multiplication = first * last

print(difference)
print(total)
print(multiplication)
