# cw1
def multiply(num1, num2):
   result = num1 * num2
print(multiply(7, 8))

# cw2
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(even_or_odd(7))


# cw3
def greet(name):
    result = "Hello" + " " + str(name)
name = "david"
print(greet("david"))
name = "mike"
print(greet("mike"))

# cw4
def concatenate_strings(str1, str2):
    return str1 + " " + str2
print(concatenate_strings("Hello", "World"))
